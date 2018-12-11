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

all_sprite_list = pg.sprite.Group()

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

        player = Player(50, 50, all_sprite_list)
        player.walls = wall_list
         
        all_sprite_list.add(player)
         
        clock = pg.time.Clock()
         
        done = False
         
        while not done:
         
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
         
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_r:
                        player.rotate()
                    elif event.key == pg.K_e:
                        player.fire()
         
            all_sprite_list.update()
            self.game.screen.blit(menuBackground, (0,0))
            all_sprite_list.draw(self.game.screen)
            pg.display.flip()
            clock.tick(60)
         
        pg.quit()

