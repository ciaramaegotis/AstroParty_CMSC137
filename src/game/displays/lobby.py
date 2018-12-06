import sys
import pygame as pg

# move up one directory to be able to import the images
sys.path.append("..")
from utils.button import Button
from variables import *
from images import *

class Lobby:
    def __init__(self, game):
        self.game = game
        back = Button('backButton', 530, 600, 224, 64)
        start = Button('nextButton', 950, 600, 220, 63)
        
        while self.game.currentDisplay == PLAYER_LOBBY:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game.running = False
                    quit()
                
                if event.type == pg.MOUSEBUTTONDOWN:
                    if back.raw.get_rect(topleft=(back.x,back.y)).collidepoint(event.pos):
                        self.game.currentDisplay = MAIN_MENU
                        break
                    elif start.raw.get_rect(topleft=(start.x,start.y)).collidepoint(event.pos):
                        print("Start Pressed!")
                        # break
            
            self.game.screen.blit(menuBackground, (0,0))
            self.game.screen.blit(chatPanel, (-20, 33))
            self.game.screen.blit(waitOtherPlayers, (415, 70))
            self.game.screen.blit(player1, (600, 200))
            self.game.screen.blit(noPlayer, (900, 200))
            self.game.screen.blit(noPlayer, (600, 350))
            self.game.screen.blit(noPlayer, (900, 350))
            self.game.screen.blit(back.raw, (back.x, back.y))
            self.game.screen.blit(start.raw, (start.x, start.y))
            
            pg.display.flip()