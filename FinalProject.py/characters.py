import pygame

class Saitama():
    def __init__(self, screen):
        #initialize the character and set starting position
        self.screen = screen


        #loading images
        self.image = pygame.image.load("saitama.png")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.bottom = self.screen_rect.bottom


    def blitme(self):
        #draws characters current location
        self.screen.blit(self.image, self.rect)