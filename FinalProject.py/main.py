import pygame
import math

#MIGHT MAKE A ONE PUNCH MAN GAME


pygame.init()
width, height = 640,420
playerpos = [100,100]
screen = pygame.display.set_mode((width, height))
badtimer = 0

linkmap = pygame.image.load("zeldamap.jpg")
saitama = pygame.image.load("saitama.png")


while 1:
    badtimer = -1
    screen.fill(0)
    for x in range(int(width / linkmap.get_width() + 1)):
        for y in range(int(height / linkmap.get_height() + 1)):
            screen.blit(linkmap, (x * 100, y * 100))


    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
    playerrot = pygame.transform.rotate(saitama, 360 - angle * 57.29)
    playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
    screen.blit(playerrot, playerpos1)