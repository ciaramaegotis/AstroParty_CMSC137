import pygame as pg
import random

from utils.button import Button
from utils.variables import *
from utils.images import *

WHITE = (255, 255, 255)
ORANGE = (255, 140, 0)

class Wall(pg.sprite.Sprite):
    """ Wall the player can run into. """
    def __init__(self, x, y, width, height):
        """ Constructor for the wall that the player can run into. """
        # Call the parent's constructor
        super().__init__()
 
        self.image = pg.Surface([width, height])
        self.image.fill(ORANGE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x