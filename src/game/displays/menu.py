import sys
import pygame as pg

# move up one directory to be able to import the images
sys.path.append("..")
from utils.button import Button
from variables import *
from images import *

class Menu:
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
                    if join.raw.get_rect(topleft=(join.x,join.y)).collidepoint(event.pos):
                        self.game.currentDisplay = PLAYER_LOBBY
                        break
                    # elif guide.isOver(pos):
                    #     self.game.status = GUIDE
                    #     break
                    # elif about.isOver(pos):
                    #     self.game.status = ABOUT
                    #     break

                # if event.type == pg.MOUSEMOTION:
                #     start.isOver(pos)
                #     guide.isOver(pos)
                #     about.isOver(pos)
            self.game.screen.blit(menuBackground, (0,0))
            self.game.screen.blit(astroParty, (323, 100))
            self.game.screen.blit(create.raw, (create.x, create.y))
            self.game.screen.blit(join.raw, (join.x, join.y))
            self.game.screen.blit(exitGame.raw, (exitGame.x, exitGame.y))
            pg.display.flip()
        
        # Get Username
        font = pg.font.Font(None, 100)
        input_box = pg.Rect(370, 355, 550, 82)
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
                        if(len(text)<10):
                            text += event.unicode
            txt_surface = font.render(text, True, pg.Color("white"))
            # Render Elements
            self.game.screen.blit(menuBackground, (0, 0))
            self.game.screen.blit(txt_surface, (input_box.x+15, input_box.y+10))
            self.game.screen.blit(enterUsername, (225, 195))
            pg.draw.rect(self.game.screen, pg.Color("#EB5500"), input_box, 2)
            pg.display.flip()