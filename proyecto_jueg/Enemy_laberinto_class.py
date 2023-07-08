import pygame
from Funciones_laberinto import load_sprite_sheets

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, escalar,screen,delay,nombre,width,hight):
        super().__init__()
        self.sprite = load_sprite_sheets("", "sprite juego", width, hight, escalar, False)
        self.nombre_animacion = nombre
        self.rect = self.sprite[self.nombre_animacion][0].get_rect(topleft=(x, y))
        self.animacion_delay = delay
        self.contador_animacion = 0
        self.contador = 0
        self.animacion_disparo = False
        self.image = self.sprite[self.nombre_animacion][0]
        self.screen = screen

    def update(self):
        self.loop()

    def loop(self):
        sprites = self.sprite[self.nombre_animacion]
        sprite_index = (self.contador_animacion // self.animacion_delay) % len(sprites)
        self.image = sprites[sprite_index]
        if sprite_index == 1:
            self.animacion_disparo = True
            self.contador += 1
        if self.animacion_delay >= 120:
            if self.contador > 60:
                self.contador_animacion = 0
                self.contador = 0

        self.contador_animacion += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        if self.contador_animacion // self.animacion_delay > len(sprites):
            self.contador_animacion = 0
