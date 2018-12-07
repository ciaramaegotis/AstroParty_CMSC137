import sys
import pygame as pg

# move up one directory to be able to import the images
sys.path.append("..")
from utils.button import Button
from utils.variables import *
from utils.images import *

class Game:
    def __init__(self, game):
        self.game = game
        create = Button('createlobButton', 310, 400, 263, 74)
        join = Button('joinlobButton', 685, 400, 263, 74)
        exitGame = Button('exitButton', 500, 510, 263, 74)

        while self.game.currentDisplay == MAIN_MENU:
            for event in pg.event.get():
                # pos = pg.mouse.get_pos()
                if event.type == pg.QUIT:
                    self.game.running = False
                    quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if create.raw.get_rect(topleft=(create.x,create.y)).collidepoint(event.pos):
                        self.game.currentDisplay = PLAYER_LOBBY
                        break
                    elif join.raw.get_rect(topleft=(join.x,join.y)).collidepoint(event.pos):
                        self.game.currentDisplay = PLAYER_LOBBY
                        break
                    elif exitGame.raw.get_rect(topleft=(exitGame.x,exitGame.y)).collidepoint(event.pos):
                        self.game.running = False
                        quit()
                   
            self.game.screen.blit(menuBackground, (0,0))
            self.game.screen.blit(astroParty, (323, 100))
            self.game.screen.blit(create.raw, (create.x, create.y))
            self.game.screen.blit(join.raw, (join.x, join.y))
            self.game.screen.blit(exitGame.raw, (exitGame.x, exitGame.y))
            pg.display.flip()
        
