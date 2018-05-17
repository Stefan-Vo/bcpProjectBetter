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

        #Store decimal value
        ##self.center = float(self.rect.centerx)



        #movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1

        #Update rect object from self.center
        ##self.rect.centerx = self.center


    def blitme(self):
        #draws characters current location
        self.screen.blit(self.image, self.rect)