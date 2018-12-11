import sys
import pygame as pg
import random

WHITE = (255, 255, 255)
ORANGE = (255, 140, 0)

# move up one directory to be able to import the images
sys.path.append("..")
from utils.button import Button
from utils.variables import *
from utils.images import *
from .wall import Wall
from .player import Player
from .bullet import Bullet
from chat import Chat
from .ChatBox import ChatBox

all_sprite_list = pg.sprite.Group()

class GamePlay:
    def __init__(self, game):
        self.game = game
        
        #instantiate chat
        #self.game.chat = Chat(self.game)
        
        pg.init()         
        wall_list = pg.sprite.Group()
         
        wall = Wall(0, 0, 10, 600)
        wall_list.add(wall)
        all_sprite_list.add(wall)
         
        wall = Wall(10, 0, 790, 10)
        wall_list.add(wall)
        all_sprite_list.add(wall)


        wall = Wall(790, 0, 10, 600)
        wall_list.add(wall)
        all_sprite_list.add(wall)

        wall = Wall(10, 590, 790, 10)
        wall_list.add(wall)
        all_sprite_list.add(wall)

        #randomized maze
        maze_number = 1#random.randint(1,4)
        if (maze_number == 1):#cross maze (vertical)
            wall = Wall(400, 150, 10, 300)
            wall_list.add(wall)
            all_sprite_list.add(wall)

            wall = Wall(200, 300, 400, 10)
            wall_list.add(wall)
            all_sprite_list.add(wall)

        player = Player(50, 50, all_sprite_list)
        player.walls = wall_list
         
        all_sprite_list.add(player)
         
        clock = pg.time.Clock()
         
        active = True
        message = ""
        chatbox = ChatBox(850, 10, 400, 700)
        all_sprite_list.add(chatbox)
        while (True):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                if (event.type == pg.MOUSEBUTTONDOWN):
                    if chatbox.rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                        break
                elif event.type == pg.KEYDOWN:
                    if (active):
                        if event.key == pg.K_RETURN:
                            try:
                                if(message == "dc()"):
                                    self.game.disconnectChat(self.game.userID)
                                elif(message == "list()"):
                                    self.game.chat.listPlayers()
                                else:
                                    self.game.chat.sendMessage(message)
                            except OSError:
                                print("\nError")
                            message = ''
                        elif event.key == pg.K_BACKSPACE:
                            message = message[:-1]
                        else:
                            message += event.unicode
                    else:
                        if event.key == pg.K_r:
                            player.rotate()
                        elif event.key == pg.K_e:
                            player.fire()
            
            font = pg.font.Font(None, 28)

            all_sprite_list.update()
            self.game.screen.blit(menuBackground, (0,0))
            all_sprite_list.draw(self.game.screen)
            input_box = pg.Rect(860, 655, 380, 30)
            pg.draw.rect(self.game.screen, pg.Color("white"), input_box, 2)
            # Print text in chat box
            if (len(message) > 25):
                message = message[0:28]
                txt_surface = font.render(message, True, pg.Color("white"))
                self.game.screen.blit(txt_surface, (865, 660))
            else:
                txt_surface = font.render(message, True, pg.Color("white"))
                self.game.screen.blit(txt_surface, (865, 660))

            # Print text in chat panel
            start_y = 50
            panelFont = pg.font.Font(None, 25)
            for content in self.game.chatTranscript:
                label = panelFont.render(content, 1, (255,255,255))
                self.game.screen.blit(label, (865, start_y))
                start_y += 20
            pg.display.flip()
            clock.tick(60)
         
        pg.quit()
