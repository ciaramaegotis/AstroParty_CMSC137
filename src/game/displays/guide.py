import sys
import pygame as pg

# move up one directory to be able to import the images
sys.path.append("..")
from utils.button import Button
from utils.variables import *
from utils.images import *

class Guide:
    def __init__(self, game):
        self.game = game
        # Get Username
        font = pg.font.Font(None, 100)
        instructions = [rotate, fire, rounds, wins, goodluck]
        counter = 0
        while (counter < len(instructions)):
            #textsurface = font.render(instructions[counter], False, (255, 140, 0))
            #continueG = font.render("Press space", False, (255, 140, 0))
            self.game.screen.blit(menuBackground, (0, 0))
            if counter < 2:
            	self.game.screen.blit(instructions[counter], (300, 150))
            elif counter == 2:
            	self.game.screen.blit(instructions[counter], (350, 150))
            elif counter == 3:
            	self.game.screen.blit(instructions[counter], (160, 150))
            else:
            	self.game.screen.blit(instructions[counter], (280, 120))
            self.game.screen.blit(next, (280, 600))
            pg.display.flip()
            Done = False
            while not Done:
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_SPACE:
                            print("space")
                            Done = True
                            break
            counter = counter + 1
        self.game.currentDisplay = MAIN_MENU
