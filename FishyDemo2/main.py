"""
Copy this code to your local platform once you get Pygame working.

In the context of Repl.it, not all the key commands will do anything
(f for fullscreen not an option)

The d key is lethal to Fish (not all of them)
A mouse click begets a new Fish
"""

import pygame
from pygame.locals import *
from fish import *
import sys

pygame.init()

size = (width, height) = (pygame.display.Info().current_w, pygame.display.Info().current_h)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0, 127, 255)
fishes = pygame.sprite.Group()


def main():
    global screen
    for i in range(10):
        fishes.add(Fish((width / 2, height / 2)))
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                fishes.add(Fish(event.pos))
            if event.type == KEYDOWN:
                if event.key == K_d:
                    sprites = fishes.sprites()
                    for i in range(len(fishes) // 2):
                        sprites[i].kill()
                elif event.key == K_f:
                    screen = pygame.display.set_mode(size, FULLSCREEN)
                elif event.key == K_ESCAPE:
                    screen = pygame.display.set_mode(size)
        fishes.update()
        screen.fill(color)
        fishes.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
