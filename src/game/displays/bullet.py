import pygame as pg
import random

from utils.button import Button
from utils.variables import *
from utils.images import *

class Bullet(pg.sprite.Sprite):
    def __init__(self, x, y, direction, wall_list):
        super().__init__()
 
        self.image = bullet
        self.image = pg.transform.scale(self.image, (10, 10))
        self.walls = wall_list
 
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