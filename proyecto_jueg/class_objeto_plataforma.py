import pygame

class Objeto(pygame.sprite.Sprite):
    def __init__(self, x, y,image):
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.animacion_disparo = False