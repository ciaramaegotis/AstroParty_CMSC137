import sys
import pygame as pg

# move up one directory to be able to import the images
sys.path.append("..")
from utils.button import Button
from utils.variables import *
from utils.images import *

class Menu:
    def __init__(self, game):
        self.game = game
        create = Button('createlobButton', 310, 400, 263, 74)
        join = Button('joinlobButton', 685, 400, 263, 74)
        exitGame = Button('exitButton', 310, 510, 263, 74)
        guideButton = Button('nextButton', 685, 510, 263, 74)

        while self.game.currentDisplay == MAIN_MENU:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game.running = False
                    quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if create.raw.get_rect(topleft=(create.x,create.y)).collidepoint(event.pos):
                        self.game.currentDisplay = PLAYER_CREATELOBBY
                        break
                    elif join.raw.get_rect(topleft=(join.x,join.y)).collidepoint(event.pos):
                        self.game.currentDisplay = PLAYER_JOINLOBBY
                        break
                    elif guideButton.raw.get_rect(topleft=(guideButton.x,guideButton.y)).collidepoint(event.pos):
                        print("GUIDE")
                        self.game.currentDisplay = GUIDE
                        break
                    elif exitGame.raw.get_rect(topleft=(exitGame.x,exitGame.y)).collidepoint(event.pos):
                        self.game.running = False
                        quit()
                   
            self.game.screen.blit(menuBackground, (0,0))
            self.game.screen.blit(astroParty, (323, 100))
            self.game.screen.blit(create.raw, (create.x, create.y))
            self.game.screen.blit(join.raw, (join.x, join.y))
            self.game.screen.blit(exitGame.raw, (exitGame.x, exitGame.y))
            self.game.screen.blit(guideButton.raw, (guideButton.x, guideButton.y))
            pg.display.flip()
        
        # Get Username
        font = pg.font.Font(None, 100)
        input_box = pg.Rect(500, 355, 280, 82)
        text = ""
        Done = False
        while not Done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game.running = False
                    quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        self.game.username = text
                        Done = True
                        break
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if(len(text) < 5):
                            text += event.unicode
            txt_surface = font.render(text, True, pg.Color("white"))
            # Render Elements
            self.game.screen.blit(menuBackground, (0, 0))
            self.game.screen.blit(enterUsername, (225, 195))
            self.game.screen.blit(txt_surface, (input_box.x+15, input_box.y+10))
            pg.draw.rect(self.game.screen, pg.Color("#EB5500"), input_box, 2)
            pg.display.flip()