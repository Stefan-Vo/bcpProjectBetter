import sys
import characters
import pygame

def check_events(characters):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
            #move ship to the right.
                characters.moving_right = True
            elif event.key == pygame.K_LEFT:
                characters.moving_left = True


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                characters.moving_right = False
            elif event.key == pygame.K_LEFT:
                characters.moving_left = False

def update_screen(ai_settings,screen,Saitama):
    screen.fill(ai_settings.bg_color)
    Saitama.blitme()

    pygame.display.flip()