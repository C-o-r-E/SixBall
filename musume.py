import pygame
import math

class Musume(pygame.sprite.Sprite):
    
    def __init__(self, imgPath, init_pos):
        pygame.sprite.Sprite.__init__(self)
        
        self.orig = pygame.image.load(imgPath).convert_alpha()
        self.image = self.orig.copy()

        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos


class Okuu(pygame.sprite.Sprite):
    
    def __init__(self, imgPath, init_pos):
        pygame.sprite.Sprite.__init__(self)
        
        self.orig = pygame.image.load(imgPath).convert_alpha()
        self.image = self.orig.copy()

        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.lastUpdate = 0

    def update(self):
        if pygame.time.get_ticks() > self.lastUpdate + 15:
            self.rect.centerx = 100 * math.cos(self.lastUpdate)
            self.lastUpdate = pygame.time.get_ticks()
        

class Orin(pygame.sprite.Sprite):
    
    def __init__(self, imgPath, init_pos):
        pygame.sprite.Sprite.__init__(self)
        
        self.orig = pygame.image.load(imgPath).convert_alpha()
        self.image = self.orig.copy()

        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
