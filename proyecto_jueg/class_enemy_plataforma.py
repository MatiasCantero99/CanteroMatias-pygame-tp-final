import pygame
from Funciones_laberinto import load_sprite_sheets
from Funciones_plataforma import *
from class_disparo_plataforma import *

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y,delay,nombre,width,height,escalar,velocidad,posicion):
        super().__init__()
        self.posicion = posicion
        self.sprite = load_sprite_sheets("", "enemy_bat", width, height,escalar, True)
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.y_inicial = y
        self.nombre_animacion = nombre
        self.rect = self.sprite[self.nombre_animacion + "_left"][0].get_rect(topleft=(self.x, self.y))
        self.animacion_delay = delay
        self.contador_animacion = 0
        self.contador = 0
        self.rango = 60
        self.direccion = 1
        self.vida = 1
        self.vivo = True
        self.sprite_index = 3

    def update(self):
        print(self.vivo)
        self.load_sprite()
        self.loop()
        self.mover()
        self.muerte()

    def load_sprite(self):
        if self.posicion:
            self.rect = self.sprite[self.nombre_animacion + "_left"][0].get_rect(topleft=(self.x, self.y))
            self.image = self.sprite[self.nombre_animacion + "_left"][0]
        else:
            self.rect = self.sprite[self.nombre_animacion][0].get_rect(topleft=(self.x, self.y))
            self.image = self.sprite[self.nombre_animacion][0]

    def loop(self):
        if self.posicion:
            sprites = self.sprite[self.nombre_animacion + "_left"]
        else:
            sprites = self.sprite[self.nombre_animacion]
        self.sprite_index = (self.contador_animacion // self.animacion_delay) % len(sprites)
        self.image = sprites[self.sprite_index]

        self.contador_animacion += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        if self.contador_animacion // self.animacion_delay > len(sprites):
            self.contador_animacion = 0


    
    def mover(self):
        if self.vivo:
            if self.direccion == 1:
                if self.y > self.y_inicial - self.rango:
                    self.nombre_animacion = "flying"
                    self.y -= self.velocidad
                else:
                    self.direccion = -1
            else:
                if self.y < self.y_inicial + self.rango:
                    self.nombre_animacion = "flying"
                    self.y += self.velocidad
                else:
                    self.direccion = 1
    
    def disparo(self):
        if self.vivo:
            if self.contador >= 160 and self.sprite_index == 3:
                if self.posicion:
                    self.contador = 0
                    return Estaca(self.rect.left, self.rect.centery,4,30,10,pygame.image.load(r"enemy_bat\arm.png"),self.posicion)
                                    
                else:
                    self.contador = 0
                    return Estaca(self.rect.right, self.rect.centery,4,30,10,pygame.image.load(r"enemy_bat\arm.png"),self.posicion)
            self.contador += 1
    
    def muerte(self):
        if not self.vivo:
            self.nombre_animacion = "death"
            self.y += 2
            if self.sprite_index == 9:
                self.kill()
    
    def verifico_muerte(self):
        print("entre")
        self.vida -= 1
        if self.vida < 1:
            self.vivo = False