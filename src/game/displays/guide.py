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
        instructions = ['Press R to rotate', 'Press E or Space to fire', 'You have a total of 5 rounds', 'You must have the most number of wins', 'Goodluck!']
        counter = 0
        while (counter < len(instructions)):
            textsurface = font.render(instructions[counter], False, (255, 140, 0))
            continueG = font.render("Press space", False, (255, 140, 0))
            self.game.screen.blit(menuBackground, (0, 0))
            self.game.screen.blit(textsurface, (0, 0))
            self.game.screen.blit(continueG, (0, 200))
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