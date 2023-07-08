#Caida a la locura
from typing import Any
import pygame
from Funciones_plataforma import *


class Plataforma(pygame.sprite.Sprite):
    def __init__(self,x,y,x_escalar,y_escalar):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"sprite juego\0.png"),(x_escalar,y_escalar)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #rectangulo top
        self.rectangulo = generar_rects(self.rect,"plataforma")

    def update(self):
        pass