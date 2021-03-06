# Import libraries
from threading import Thread
import pygame as pg
import socket
import time
import json

# Import Files
from utils.images import *
from utils.variables import *
from displays.menu import Menu
from displays.lobby import Lobby
from displays.gameplay import GamePlay
from displays.guide import Guide
from utils.button import Button 

from chat import Chat

import sys
    
host = sys.argv[1]

class Play:
    def __init__(self):
        # initialize
        pg.init()
        pg.mixer.init()
        pg.display.set_caption("Astro Party!")
        pg.display.set_icon(icon)
        
        # Flag to indicate game is running
        self.running = True
        self.gameStart = 0
        self.username = ''
        self.currentDisplay = MAIN_MENU
        self.screen = pg.display.set_mode((1280, 720))
        self.clock = pg.time.Clock()
        self.currentPlayers = 0
        self.score = 0
        self.chatTranscript = []
        self.playersList = []
        self.bulletsList = []
        # host = "" #TO DO: save here the host (only the host can click the start game)
        # players = [] #TO DO: once startgame is clicked, get the final list of players

        # Start UDP server thread
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.UDP_thread = Thread(target=self.evaluateData)
        self.UDP_thread.daemon = True
        self.UDP_thread.start()
    
    def update(self):
        # Check which display should be rendered
        self.checkDisplay()

    def checkDisplay(self):
        if self.currentDisplay == MAIN_MENU:
            Menu(self)
        elif self.currentDisplay == PLAYER_CREATELOBBY:
            Lobby(self, 'create')
        elif self.currentDisplay == PLAYER_JOINLOBBY:
            Lobby(self, 'join')
        elif self.currentDisplay == GUIDE:
            Guide(self)
        elif self.currentDisplay == GAMEPLAY:
            GamePlay(self)
########################################## Server Functions ##############################################
    # Function that listens to server
    def evaluateData(self):
        while self.running:
            data, address = self.sock.recvfrom(1024)
            # if data
            payload = data.decode().split(' ')
            payloadType = payload[0]
            # print(payload)
            if payloadType == 'CREATE_LOBBY':
                print("Created Lobby: " + self.lobby_id)
                self.userID = int(payload[1])
            elif payloadType == 'JOIN_LOBBY':
                self.chat.connectToLobby(payload[1], self.username)
                self.userID = int(payload[2])
            elif payloadType == 'GET_PLAYERS':
                self.currentPlayers = int(payload[1])
            elif payloadType == 'UPDATE_GAME':
            	print("Update Game!")
                #self.currentPlayers = int(payload[1])
            elif payloadType == 'DISCONNECT':
                self.chat.disconnectChat()
            elif payloadType == 'GET_GAME':
                self.gameStart = int(payload[1])
            elif payloadType == 'UPDATE_PLAYER_LIST':
                payload = data.decode()
                payload = payload.strip("UPDATE_PLAYER_LIST ")
                self.playersList = json.loads(payload)['listP']
                for d in self.playersList:
                    if int(d.get('id')) == self.userID:
                        self.score = int(d["score"])
                self.playersList[:] = [d for d in self.playersList if int(d.get('id')) != self.userID]
            elif payloadType == 'UPDATE_BULLET_LIST':
                payload = data.decode()
                payload = payload.strip("UPDATE_BULLET_LIST ")
                self.bulletsList = json.loads(payload)['listB']
                self.bulletsList[:] = [d for d in self.bulletsList if int(d.get('id')) != self.userID]    

    def sendToServer(self, data):
        self.sock.sendto(str.encode(data), (host, 10000))

    def createLobby(self, id, username):
        payload = 'CREATE_LOBBY ' + str(id) + ' ' + username
        self.sendToServer(payload)

    def joinLobby(self, username):
        payload = 'JOIN_LOBBY ' + username
        self.sendToServer(payload)
    
    def getPlayers(self):
        self.sendToServer('GET_PLAYERS')
    
    def disconnectChat(self, userID):
        payload = 'DISCONNECT ' + str(userID)
        self.sendToServer(payload)
    
    def startGame(self):
    	payload = 'START_GAME'
    	self.sendToServer(payload)

    def getGame(self):
        self.sendToServer('GET_GAME')

    def updateGame(self):
    	payload = 'UPDATE_GAME'
    	self.sendToServer(payload)
    
    def getPlayerStats(self):
        payload = 'GET_PLAYER_STATS'
    
    def sendPlayerStats(self, x, y, id, rotated):
        payload = 'SEND_PLAYER_STATS ' + str(x) + ' ' + str(y) + ' ' + str(id) + ' ' + str(rotated)
        self.sendToServer(payload)

    def sendBulletStats(self, x, y, id, dir):
        payload = 'SEND_BULLET_STATS ' + str(x) + ' ' + str(y) + ' ' + str(id) + ' ' + str(dir)
        self.sendToServer(payload)
    
    def updatePlayerList(self):
        self.sendToServer('UPDATE_PLAYER_LIST')

    def updateBulletList(self):
        self.sendToServer('UPDATE_BULLET_LIST')

    def purgeBullets(self):
        self.sendToServer('PURGE_BULLETS')
    
    def killScore(self, killed, killer):
        payload = 'KILL_SCORE ' + str(killed) + ' ' + str(killer) 
        self.sendToServer(payload)

game = Play()

while game.running:
    game.update()