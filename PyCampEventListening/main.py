"""
Welcome to PyCamp by Coding with Kids

This is based on an example in the Pygame docs.
https://pygame.readthedocs.io/en/latest/1_intro/intro.html

"""
import pygame
import random  # commented out where I might use it (below)
import time
import sys
from pygame.locals import K_k, K_r, K_g, K_b, K_y, K_c, K_m, K_w
from pygame.locals import KEYUP, KEYDOWN

# check console for this output
print("-----------------")
print(sys.version_info)
print(pygame.__version__)  # 1,9.6
print("-----------------")

pygame.init()
width, height = 800, 600
dvdLogoSpeed = [1, 1]
backgroundColor = 0, 0, 0

screen = pygame.display.set_mode((width, height))

# color tuples (R, G, B)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

_trash_dict = {
    K_k: BLACK,
    K_r: RED,
    K_g: GREEN,
    K_b: BLUE,
    K_y: YELLOW,
    K_c: CYAN,
    K_m: MAGENTA,
    K_w: WHITE
}

key_dict = {
    107: BLACK,
    114: RED,
    103: GREEN,
    98: BLUE,
    121: YELLOW,
    99: CYAN,
    109: MAGENTA,
    119: WHITE
}

colors = [BLACK, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, WHITE]

dvdLogo = pygame.image.load("camping.png")
dvdLogoRect = dvdLogo.get_rect()

playing = True

while playing:

    for event in pygame.event.get():

        if event.type == KEYUP:
            # check console for this output
            print(event.key)
            if event.key in key_dict:
                backgroundColor = key_dict[event.key]
        # backgroundColor = random.choice(colors)

        # useful if using same code outside of REPL
        if event.type == pygame.QUIT:
            playing = False

    screen.fill(backgroundColor)

    screen.blit(dvdLogo, dvdLogoRect)
    dvdLogoRect = dvdLogoRect.move(dvdLogoSpeed)

    if dvdLogoRect.left < 0 or dvdLogoRect.right > width:
        dvdLogoSpeed[0] = -dvdLogoSpeed[0]
    if dvdLogoRect.top < 0 or dvdLogoRect.bottom > height:
        dvdLogoSpeed[1] = -dvdLogoSpeed[1]

    pygame.display.flip()
    time.sleep(10 / 1000)

credits = \
"""
DVD bouncing logo tutorial here on repl.it:
https://repl.it/talk/learn/A-Starter-Guide-to-Pygame/11741

and

<div>
Icon made by 
<a href="https://www.flaticon.com/authors/freepik" 
title="Freepik">
Freepik
</a> 

from 

<a href="https://www.flaticon.com/" title="Flaticon">
www.flaticon.com
</a>
</div>
"""
