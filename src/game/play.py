# import os
# import sys

## add the path to the folder with the protobuf files
# script_dir = sys.path[0]
# script_dir = script_dir[:-4]
# chat_path = os.path.join(script_dir, 'proto/')
# sys.path.insert(0, chat_path)

# from tcp_packet_pb2 import TcpPacket


# Import libraries
from threading import Thread
import pygame as pg
import socket
import time

# Import Files
from images import *
from variables import *
from displays.menu import Menu
from displays.lobby import Lobby
from utils.button import Button 

class Play:
    def __init__(self):
        # initialize
        pg.init()
        pg.mixer.init()
        pg.display.set_caption("Astro Party!")
        pg.display.set_icon(icon)
        
        # Flag to indicate game is running
        self.running = True
        self.username = ''
        self.currentDisplay = MAIN_MENU
        self.screen = pg.display.set_mode((1280, 720))
        self.clock = pg.time.Clock()
        self.currentPlayers = 0
        self.chatTranscript = []
        host = "" #TO DO: save here the host (only the host can click the start game)
        players = [] #TO DO: once startgame is clicked, get the final list of players

        # game variables
        # self.status = INTRO
        # self.running = True # game is running
        # self.initialized = False # initialized game in arena (with players)
        # self.created_chat = False 
        # self.name_available = True
        # self.player_count = 0
        # self.curr_player = ''
        # self.showed_end = False
        # self.restart_request = False

        # converted background images for optimized game loop
        # self.arena_bg = ARENA_BG.convert()
        # self.background = MENU.convert()

        # socket to UDP server
        # self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # multiple threads for the game and chat (chat is in join game)
        # self.game_thread = Thread(target=self.receive)
        # self.game_thread.daemon = True
        # self.game_thread.start()

    def update(self):
        # Check which display should be rendered
        if self.currentDisplay == MAIN_MENU:
            Menu(self)
        elif self.currentDisplay == PLAYER_LOBBY:
            Lobby(self)
######################## Server Functions ###################################
    # def sendData

game = Play()

while game.running:
    game.update()