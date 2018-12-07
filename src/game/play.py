# Import libraries
from threading import Thread
import pygame as pg
import socket
import time

# Import Files
from utils.images import *
from utils.variables import *
from displays.menu import Menu
from displays.lobby import Lobby
from utils.button import Button 

from chat import Chat

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

    def update(self):
        # Check which display should be rendered
        self.checkDisplay()

    def checkDisplay(self):
        if self.currentDisplay == MAIN_MENU:
            Menu(self)
        elif self.currentDisplay == PLAYER_LOBBY:
            Lobby(self)
######################## Server Functions ###################################
    # def sendData

game = Play()

while game.running:
    game.update()