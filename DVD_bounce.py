import pygame, time, sys

print(sys.version) # 3.6.9

pygame.init()
width, height = 800, 600
dvdLogoSpeed = [1, 1]
backgroundColor = 0, 0, 0

screen = pygame.display.set_mode((width, height))

dvdLogo = pygame.image.load("dvd-logo-white.png")
dvdLogoRect = dvdLogo.get_rect()

while True:
    screen.fill(backgroundColor)

    screen.blit(dvdLogo, dvdLogoRect)
    dvdLogoRect = dvdLogoRect.move(dvdLogoSpeed)

    if dvdLogoRect.left < 0 or dvdLogoRect.right > width:
        dvdLogoSpeed[0] = -dvdLogoSpeed[0]
    if dvdLogoRect.top < 0 or dvdLogoRect.bottom > height:
        dvdLogoSpeed[1] = -dvdLogoSpeed[1]

    pygame.display.flip()
    time.sleep(10 / 1000)
