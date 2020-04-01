# SPACE INVADERS
import pygame, sys, random

pygame.init()
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
random_numbers = [random.randint(1, 500) for number in range(500)]
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Space Invaders Simplified")

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel
    if keys[pygame.K_DOWN] and y < 500 - height:
        y += vel
    if keys[pygame.K_UP] and y > 0:
        y -= vel

    player = pygame.draw.rect(win, red, (x, y, width, height))
    enemy = pygame.draw.rect(win, blue, (enemy_start_pos, random_numbers[i], width, height))

    enemy_start_pos -= 0.5
    pygame.display.update()

    win.fill((0, 0, 0))

    if enemy_start_pos == 50:
        i += 1
        enemy_start_pos = 500

    hitbox_x_enemy = [b + enemy_start_pos for b in range(width + 1)]
    hitbox_y_enemy = [b + random_numbers[i] for b in range(height + 1)]

    if x in hitbox_x_enemy and y in hitbox_y_enemy:
        run = False

pygame.quit()