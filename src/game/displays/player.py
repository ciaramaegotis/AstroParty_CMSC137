import pygame as pg
import random


from utils.button import Button
from utils.variables import *
from utils.images import *
from .bullet import Bullet

WHITE = (255, 255, 255)
ORANGE = (255, 140, 0)

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, all_sprite_list, pname):
        super().__init__()
        #player
        self.playerName = pname
        self.image = rocket_ship
        self.image = pg.transform.scale(self.image, (100, 50))
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.all_sprite_list = all_sprite_list

        self.direction = 1
        self.walls = None

    def rotate(self):
        self.image = pg.transform.rotate(self.image, 270)
        self.direction = 1 if self.direction == 4 else self.direction+1
    
    def fire(self):
        bullet = Bullet(self.rect.x, self.rect.y, self.direction, self.walls)
        self.all_sprite_list.add(bullet)

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