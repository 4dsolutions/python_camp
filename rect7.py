"""
Welcome to PyCamp by Coding with Kids

This is based on the example rect7.py in the Pygame docs.
https://pygame.readthedocs.io/en/latest/rect/rect.html

"""

import pygame
from pygame.locals import *
from random import randint

width = 500
height = 200

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)

BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
WHITE = (255, 255, 255)

dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.Font(None, 24)
running = True

# from rect import *

rect = Rect(50, 60, 200, 80)
moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect)
    if moving:
        pygame.draw.rect(screen, BLUE, rect, 4)
    pygame.display.flip()

pygame.quit()