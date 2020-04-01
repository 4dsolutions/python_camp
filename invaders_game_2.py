"""
Rect attributes

x,y
top, left, right, bottom
topleft, bottomleft, topright, bottomright
midtop, midleft, midbottom, midright
center, centerx, centery
size, width, height
w,h
"""

# SPACE INVADERS

import pygame, sys, random

pygame.init()
clock = pygame.time.Clock()

width = 50
height = 30
x = 250
y = 250
enemy_start_pos = 500
blue = (0, 0, 255)
red = (255, 0, 0)
run = True
vel = 1

i = 0  # an index of random numbers

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Space Invaders Simplified")

enemy_y = random.randint(0, 500)

player = pygame.Rect(10,  10,  width, height)
enemy =  pygame.Rect(500, enemy_y, width, height)

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        player.x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        player.x += vel
    if keys[pygame.K_DOWN] and y < 500 - height:
        player.y += vel
    if keys[pygame.K_UP] and y > 0:
        player.y -= vel

    pygame.draw.rect(win, red, player)
    pygame.draw.rect(win, blue, enemy)

    enemy.x -= 0.5
    pygame.display.update()

    win.fill((0, 0, 0))

    if enemy.left <= 50:
        i += 1
        enemy.right = 500

    # print("Horiz:", player.x, enemy.left, enemy.right)
    # print("Vert:",  player.y, enemy.top, enemy.bottom)

    if (enemy.left <= player.x <= enemy.right) and \
        (enemy.top <= player.y <= enemy.bottom):
        print("Collision detected!")
        run = False

    clock.tick()

pygame.quit()