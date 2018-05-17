#Note* must fix adjusting the ship speed. Marked ##

import sys

import pygame

#import the settings.py
from settings import Settings
from characters import Saitama
import gamefunctions as gf

def run_game():
#Initizalize game and create screen object
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("ONE PUNCH MAN")
    FPS = 500


    #Making the characters
    characters = Saitama(screen)
    ##Saitama = characters(ai_settings, screen)

    # defining some colors


    #The line below will start the main loop for the game.
    while True:
        gf.check_events(characters)
        characters.update()
        gf.update_screen(ai_settings, screen, characters)


    #Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        #redraws screen each time it passes through loop
        screen.fill(ai_settings.bg_color)
        characters.blitme()

        #This makes the recently drawn screen visible
        pygame.display.flip()

run_game()