import pygame
from pygame.locals import *

bg = pygame.image.load("background.jpeg")
screen = pygame.display.set_mode((850, 450))
pygame.init()
clock=pygame.time.Clock()
boxx=200
boxy=200
image = pygame.Surface([20,20]).convert_alpha()

speed = 5   # larger values will move objects faster
while True :
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT :
            pygame.quit()
            quit()
    image.scroll(10,10)
    screen.blit(bg, (0, 0))
    # I did modulus 720, the surface width, so it doesn't go off screen
    screen.blit(image,((boxx + speed) % 720, (boxy + speed) % 720))
    pygame.display.update()
    clock.tick(60)