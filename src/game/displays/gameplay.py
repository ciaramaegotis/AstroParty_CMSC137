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

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, playernum):
        super().__init__()
        #player
        self.image = rocket_ship
        self.image = pg.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        if(playernum == 1):
            self.direction = 3
        else:
            self.direction = 1
        self.walls = None

    def rotate(self):
        print("ROTATE!")
        self.image = pg.transform.rotate(self.image, 270)
        self.direction = 1 if self.direction == 4 else self.direction+1
    
    def fire(self):
        print("FIRE!")
        print(self.rect.x)
        print(self.rect.y)
        bullet = Bullet(self.rect.x, self.rect.y, self.direction, self.walls)
        all_sprite_list.add(bullet)

    def changespeed(self, direction):
        """ Change the speed of the player. """
        self.direction = direction
 
    def update(self):
        """ Update the player position. """
        # Move left/right
        change_x = 0
        change_y = 0
        if (self.direction == 1):
            change_x = 3
        elif (self.direction == 2):
            change_y = 3
        elif (self.direction == 3):
            change_x = -3
        elif (self.direction == 4):
            change_y = -3
        
        self.rect.x += change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pg.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += change_y
 
        # Check and see if we hit anything
        block_hit_list = pg.sprite.spritecollide(self, self.walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
 
 
class Wall(pg.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        # Make a blue wall, of the size specified in the parameters
        self.image = pg.Surface([width, height])
        self.image.fill(ORANGE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x


class Bullet(pg.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, direction, wall_list):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        self.image = bullet
        self.image = pg.transform.scale(self.image, (10, 10))
        self.walls = wall_list
 
        # Make our top-left corner the passed-in location.
        self.direction = direction
        self.rect = self.image.get_rect()
        if (direction == 2):
            self.rect.y = y + 100
            self.rect.x = x + 15
        elif (direction == 1):#done
            self.rect.y = y + 22
            self.rect.x = x + 100
        elif (direction == 3):#done
            self.rect.y = y + 20
            self.rect.x = x - 20
        elif (direction == 4):#done
            self.rect.y = y - 10
            self.rect.x = x + 20

    def update(self):
        """ Update the player position. """
        # Move left/right
        change_x = 0
        change_y = 0
        if (self.direction == 1):
            change_x = 5
        elif (self.direction == 2):
            change_y = 5
        elif (self.direction == 3):
            change_x = -5
        elif (self.direction == 4):
            change_y = -5

        if (self.rect.x > 800 or self.rect.x < 0 or self.rect.y > 600 or self.rect.y < 0):
            self.kill()
        self.rect.x += change_x
        self.rect.y += change_y
        block_hit_list = pg.sprite.spritecollide(self, self.walls, False)
        if (len(block_hit_list) >= 1):
            self.kill()

class GamePlay:
    def __init__(self, game):
        self.game = game
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
        # elif (maze_number == 2):#slanted cross maze

        # elif (maze_number == 3):#spiral

        # Create the player paddle object
        if(self.game.userID == 0):
            player = Player(50, 50, 0)
            player.walls = wall_list
            all_sprite_list.add(player)
        elif(self.game.userID == 1):
            player2 = Player(550, 50, 1)
            player2.walls = wall_list
            all_sprite_list.add(player2)
        
        


        # Get list of players from server
        self.game.updatePlayerList()

        for p in self.game.playersList:
            if(p['id'] == 0):
                player = Player(550, 50, 1)
                player.walls = wall_list
                all_sprite_list.add(player)
            if(p['id'] == 1):
                player2 = Player(550, 50, 1)
                player2.walls = wall_list
                all_sprite_list.add(player2)
            
            # if(player['id'] == 2):
            # if(player['id'] == 3):
            
        # Add all players

        # player2 = Player(150, 150)
        # player2.walls = wall_list
        
        # all_sprite_list.add(player2)
         
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