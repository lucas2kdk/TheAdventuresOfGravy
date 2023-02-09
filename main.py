# lav en skærm (1200X600)

import pygame
from sys import exit
import math
pygame.init()

size = width, height = 1200, 600

origin = width/2, 0

white = 255, 255, 255
black = 0,0,0

screen = pygame.display.set_mode(size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    pygame.display.flip()

pygame.quit()
quit()