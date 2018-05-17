# 1 - Import library
import pygame
from pygame.locals import *
import math
import _random
import random

# 2 - Initialize the game
pygame.init()
width, height = 760, 680
keys = [False, False, False, False]
playerpos=[100,100]
screen=pygame.display.set_mode((width, height))
acc=[0,0]
arrows=[]
bullet=[]
pygame.display.set_caption('SASAGEYO SASAGEYO')
badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194
myname = input("What is your name: ")
# 3 - Load images
#energyball = pygame.image.load("Ki.png")
player = pygame.image.load("lolga.png")
field = pygame.image.load("gridblue.png")
castle = pygame.image.load("hq.jpg")
energyblast = pygame.image.load("doritto.png")
badguyimg1 = pygame.image.load("coke2.png")
badguyimg = badguyimg1
#boros = pygame.image.load("pepe2.png")
healthbar = pygame.image.load("healthbar.png")
health = pygame.image.load("health.png")
arrow = pygame.image.load("bullet.png")
gameover = pygame.image.load("wasted.png")
youwin = pygame.image.load("opmm.jpg")
#sasagey = pygame.image.load("BELLARMINEJ.png")
dew = pygame.image.load("dew.jpg")
dewb = pygame.image.load("dewb.jpg")
#dorito = pygame.image.load("dorrito.png")

#sound
# mission =  pygame.mixer.Sound('Mission.mp3')
# mission.set_volume(0.9)
# shoot = pygame.mixer.Sound("mlg.mp3")
# shoot.set_volume(0.05)

black =(0,0,0)
end_it=False
while (end_it==False):
    screen.fill(black)
    myfont=pygame.font.SysFont("Britannic Bold", 50)
    nlabel=myfont.render("Welcome "+myname+" " "Click to play", 1, (255, 0, 0))
    for event in pygame.event.get():
        if event.type==MOUSEBUTTONDOWN:
            end_it=True
    screen.blit(dew, (10, 100))
    screen.blit(nlabel,(200,100))
    pygame.display.flip()
pygame.mixer.music.load('aotsasageyo.mp3')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.55)


#  keep looping through
running = 1
exitcode = 0
while running:
    badtimer-=1
    # clear the screen before drawing it again
    screen.fill(0)
    #  draw the screen elements
    for x in range(int(width / field.get_width()+ 1)):
        for y in range(int(height / field.get_height()+ 1)):
            screen.blit(field, (x * 100, y * 100))
    screen.blit(castle, (0, 30))
    #screen.blit(castle, (0, 135))
    #screen.blit(castle, (0, 240))
    #screen.blit(castle, (0, 345))
    #screen.blit(energyball, (-300,-200))
    #screen.blit(boros, (50,400))
    #screen.blit(sasagey, (0,100))
    screen.blit(dewb, ((600,50)))
    #  - Set player position and rotation
    position = pygame.mouse.get_pos()
    angle = math.atan2(position[1] - (playerpos[1] + 32), position[0] - (playerpos[0] + 26))
    playerrot = pygame.transform.rotate(player, 360 - angle * 57.29)
    playerpos1 = (playerpos[0] - playerrot.get_rect().width / 2, playerpos[1] - playerrot.get_rect().height / 2)
    screen.blit(playerrot, playerpos1)
    #  - Drawing the arrows
    for bullet in arrows:
        index = 0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] >760 or bullet[2] < -64 or bullet[2] > 680:
            arrows.pop(index)
        index += 1
        for projectile in arrows:
            arrow1 = pygame.transform.rotate(energyblast, 360 - projectile[0] * 57.29)
            screen.blit(arrow1, (projectile[1], projectile[2]))

    # for bul in bullet:
    #     index = 0
    #     velx = math.cos(bul[0]) * 10
    #     vely = math.sin(bul[0]) * 10
    #     bul[1] += velx
    #     bul[2] += vely
    #     if bul[1] < -34 or bullet[1] >540 or bullet[2] < -34 or bullet[2] > 380:
    #         bullet.pop(index)
    #     index +=1
    #     for projectile in bullet:
    #         bullet1 = pygame.transform.rotate(arrow, 360 - projectile[0] * 57.29)
    #         screen.blit(bullet1, (projectile[1], projectile[2]))
            # 6.3 - Draw badgers
    if badtimer == 0:
        badguys.append([640, random.randint(50, 430)])
        badtimer = 100 - (badtimer1 * 2)
        if badtimer1 >= 35:
            badtimer1 = 35
        else:
            badtimer1 += 5
    index = 0
    for badguy in badguys:
        if badguy[0] < -64:
            badguys.pop(index)
        badguy[0] -= 7
            # 6.3.1 - Attack castle
        badrect = pygame.Rect(badguyimg.get_rect())
        badrect.top = badguy[1]
        badrect.left = badguy[0]
        if badrect.left < 64:
            healthvalue -= random.randint(5, 20)
            badguys.pop(index)
                    #  - Check for collisions
        index1 = 0
        for bullet in arrows:
            bullrect = pygame.Rect(energyblast.get_rect())
            bullrect.left = bullet[1]
            bullrect.top = bullet[2]
            if badrect.colliderect(bullrect):
                acc[0] += 1
                badguys.pop(index)
                arrows.pop(index1)
            index1 += 1
        # - Next bad guy
        index += 1
    for badguy in badguys:
        screen.blit(badguyimg, badguy)
        # - Draw clock

        font = pygame.font.Font(None, 24)
        survivedtext = font.render(str((90000 - pygame.time.get_ticks()) / 60000) + ":" + str(
            (90000 - pygame.time.get_ticks()) / 1000 % 60).zfill(2), True, (0, 0, 0))
        textRect = survivedtext.get_rect()
        textRect.topright = [635, 5]
        screen.blit(survivedtext, textRect)

        #  - Draw health bar
    screen.blit(healthbar, (5, 5))
    for health1 in range(healthvalue):
        screen.blit(health, (health1 + 8, 8))


    # - update the screen
    pygame.display.flip()
    # - loop through the events
    for event in pygame.event.get():
        # check if the event is the X button
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            elif event.key == K_a:
                keys[1] = True
            elif event.key == K_s:
                keys[2] = True
            elif event.key == K_d:
                keys[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys[0] = False
            elif event.key == pygame.K_a:
                keys[1] = False
            elif event.key == pygame.K_s:
                keys[2] = False
            elif event.key == pygame.K_d:
                keys[3] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.mixer.music.load("mlg.mp3")
            pygame.mixer.music.play(0)
            position = pygame.mouse.get_pos()
            acc[1] += 1
            arrows.append(
                [math.atan2(position[1] - (playerpos1[1] + 32), position[0] - (playerpos1[0] + 26)), playerpos1[0] + 32,
                 playerpos1[1] + 32])
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_r:
        #         position = pygame.mouse.get_pos()
        #     acc[1] += 1
        #     bullet.append(
        #         [math.atan2(position[1] - (playerpos1[1] + 32), position[0] - (playerpos1[0] + 26)) , playerpos1[0] + 32,
        #          playerpos1[1] + 32])


        #  Move player
    if keys[0]:
        playerpos[1] -= 5
    elif keys[2]:
        playerpos[1] += 5
    if keys[1]:
        playerpos[0] -= 5
    elif keys[3]:
        playerpos[0] += 5

 # Win/Lose check
    if pygame.time.get_ticks()>=90000:
        running=0
        exitcode=1
    if healthvalue<=0:
        running=0
        exitcode=0
    if acc[1]!=0:
        accuracy=acc[0]*1.0/acc[1]*100
    else:
        accuracy=0
# Win/lose display
if exitcode==0:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(gameover, (140,100))
    screen.blit(text, textRect)
    # mission.play()
    pygame.mixer.music.load("Mission.mp3")
    pygame.mixer.music.play(0)
else:
    pygame.font.init()
    font = pygame.font.Font(None, 24)
    text = font.render("Accuracy: "+str(accuracy)+"%", True, (0,255,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery+24
    screen.blit(youwin, (0,0))
    screen.blit(text, textRect)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
    pygame.display.flip()

