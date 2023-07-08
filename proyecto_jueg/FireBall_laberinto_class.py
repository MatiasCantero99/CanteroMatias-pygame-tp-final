import pygame
from os.path import join, isfile
from os import listdir
from Funciones_laberinto import load_sprite_sheets

class FireBall(pygame.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"sprite juego\fuego.png"),(50,30)).convert_alpha()
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.power = False

    def update(self):
        self.rect.x += self.speed
    
