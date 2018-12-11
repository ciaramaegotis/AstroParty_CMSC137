import sys
import pygame as pg
import random
import time

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
    def __init__(self, game, x, y, playernum):
        super().__init__()
        #player
        if(playernum == 0):
            self.image = ship1
            self.direction = 1
        if(playernum == 1):
            self.image = ship2
            self.direction = 3
            self.image = pg.transform.rotate(self.image, 540)
        if(playernum == 2):
            self.image = ship3
            self.direction = 1
        if(playernum == 3):
            self.image = ship4
            self.direction = 3
            self.image = pg.transform.rotate(self.image, 540)
        # self.image = pg.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.game = game
        self.rect.x = x
        self.id = 0
        self.walls = None
        self.collisions = None
        self.rotated = False

    def rotate(self):
        self.image = pg.transform.rotate(self.image, 270)
        self.direction = 1 if self.direction == 4 else self.direction+1
    
    def fire(self):
        self.bullet = Bullet(self.game, self.rect.x, self.rect.y, self.direction, self.walls, self.collisions)
        all_sprite_list.add(self.bullet)

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
    def __init__(self, game, x, y, direction, wall_list, collisions):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
        self.image = bullet
        self.game = game
        self.image = pg.transform.scale(self.image, (10, 10))
        self.walls = wall_list
        self.collisions = collisions
        self.id = 0
 
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
        block_hit_list = pg.sprite.spritecollide(self, self.collisions, False)
        if (len(block_hit_list) >= 1):
            for col in block_hit_list:
                self.game.killScore(col.id, self.id)
            self.kill()
            self.game.updatePlayerList()
            print("bullet hit!")
            print(self.game.playersList)
            print(self.game.score)

class GamePlay:
    def __init__(self, game):
        self.game = game
        self.gameFinished = False
        self.remotePlayers = []
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
        # Create the player paddle object
        if(self.game.userID == 0):
            self.game.player = Player(self.game, 50, 50, 0)
        elif(self.game.userID == 1):
            self.game.player = Player(self.game, 550, 50, 1)
        elif(self.game.userID == 2):
            self.game.player = Player(self.game, 50, 350, 2)
        elif(self.game.userID == 3):
            self.game.player = Player(self.game, 550, 350, 3)
        self.game.player.walls = wall_list
        all_sprite_list.add(self.game.player)

        self.game.sendPlayerStats(self.game.player.rect.x, self.game.player.rect.y, self.game.userID, False)
            
        time.sleep(0.5)
        # Get list of other players from server
        self.game.updatePlayerList()

        while len(self.game.playersList) <= 0:
            print("nope")

        collide_list = pg.sprite.Group()
        for p in self.game.playersList:
            newPlayer = Player(self.game, p['x'], p['y'], p['id'])
            newPlayer.walls = wall_list
            newPlayer.id = p['id']
            newPlayer.status = p["status"]
            wall_list.add()
            self.remotePlayers.append(newPlayer)
            collide_list.add(self.remotePlayers[len(self.remotePlayers)-1])
            all_sprite_list.add(self.remotePlayers[len(self.remotePlayers)-1])
        
        self.game.player.collisions = collide_list
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
                            self.game.player.rotate()
                            self.game.player.rotated = True
                        elif event.key == pg.K_e:
                            self.game.player.fire()
                            self.game.sendBulletStats(self.game.player.bullet.rect.x, self.game.player.bullet.rect.y, self.game.userID, self.game.player.direction)


            font = pg.font.Font(None, 28)
            
            # Send coords to server
            self.game.sendPlayerStats(self.game.player.rect.x, self.game.player.rect.y, self.game.userID, self.game.player.rotated)
            
            # Get coordinates
            self.game.updatePlayerList()
            self.game.updateBulletList()
            
            doneFlag = 1
            for sprite in self.remotePlayers:
                for p in self.game.playersList:
                    if p['r'] == 'True':
                        sprite.image = pg.transform.rotate(sprite.image, 270)
                        sprite.rotated = False
                    if p['id'] == sprite.id:
                        if p["status"] == 'alive':
                            doneFlag = 0    
                        if p["status"] == 'dead':
                            all_sprite_list.remove(sprite)
                        sprite.rect.x = p['x']
                        sprite.rect.y = p['y']
            for p in self.game.playersList:
                if p['id'] == self.game.userID:
                    if p["status"] == 'dead':
                        print("IM DEAD DEDADADAEDAED")
                        doneFlag = 1

            for bullet in self.game.bulletsList:
                newBullet = Bullet(self.game, int(bullet['x']), int(bullet['y']), int(bullet['dir']), self.game.player.walls, self.game.player.collisions)
                newBullet.id = int(bullet['id'])
                all_sprite_list.add(newBullet)
                self.game.bulletsList = []
                self.game.purgeBullets()

            self.game.player.rotated = False
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

            
            pg.font.init()
            myfont = pg.font.Font(None, 50)
            text = self.game.username + '\'s SCORE: ' + str(self.game.score)    
            txt_surf = myfont.render(text, False, (255,255,255))

            self.game.screen.blit(txt_surf, (50, 600))
            
            pg.display.flip()
            if doneFlag == 1:
                print("GAMEOVER")
                self.game.currentDisplay == MAIN_MENU
                break
            clock.tick(60)
        input_box = pg.Rect(860, 655, 380, 30)
        pg.draw.rect(self.game.screen, pg.Color("white"), input_box, 2)
        pg.display.flip()
        # pg.quit()