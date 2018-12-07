import os
import sys
import pygame as pg

image_path = os.path.abspath(os.curdir) + '/images/buttons/'

class Button:
    def __init__(self, name, x, y, w, h):
        self.name = name
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.raw = pg.image.load(image_path + name + '.png')