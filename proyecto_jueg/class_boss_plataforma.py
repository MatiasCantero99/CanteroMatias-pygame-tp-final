import pygame
from Funciones_laberinto import load_sprite_sheets
from Funciones_plataforma import *
from constantes import *

class Boss(pygame.sprite.Sprite):
    def __init__(self,x,y,delay,nombre,width,height,escalar,velocidad):
        super().__init__()
        self.sprite = load_sprite_sheets("", "frost", width, height,escalar, True)
        self.quieto = False
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.ataque = False
        self.nombre_animacion = nombre
        self.rect = self.sprite[self.nombre_animacion + "_left"][0].get_rect(topleft=(self.x, self.y))
        self.animacion_delay = delay
        self.contador_animacion = 0
        self.contador = 0
        self.cantidad_disparo = False
        self.vida = 10
        self.vivo = True
        self.ataque_accion = 120 

    def update(self):
        self.load_sprite()
        self.loop()
        self.mover()
        self.muerte()

    def load_sprite(self):
            # self.rect = self.sprite[self.nombre_animacion + "_left"][0].get_rect(topleft=(self.x, self.y))
            # self.image = self.sprite[self.nombre_animacion + "_left"][0]
        self.rect = self.sprite[self.nombre_animacion][0].get_rect(topleft=(self.x, self.y))
        self.image = self.sprite[self.nombre_animacion][0]
        #rectangulo left
        self.rectangulo_boss = generar_rects(self.rect,"boss")

    def loop(self):
        sprites = self.sprite[self.nombre_animacion]
        self.sprite_index = (self.contador_animacion // self.animacion_delay) % len(sprites)
        self.image = sprites[self.sprite_index]
        if self.quieto:
            if self.contador >= self.ataque_accion:
                self.nombre_animacion = "attack"
            if self.nombre_animacion == "attack" and self.sprite_index == 7 and not self.cantidad_disparo:
                self.ataque = True
                self.cantidad_disparo = True
            if self.nombre_animacion == "attack" and self.sprite_index == 13:
                self.nombre_animacion = "idle"
                self.cantidad_disparo = False
                self.contador = 0
        self.contador += 1


        self.contador_animacion += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        if self.contador_animacion // self.animacion_delay > len(sprites):
            self.contador_animacion = 0

    def mover(self):
        if not self.quieto:
            if self.x > 800:
                self.nombre_animacion = "walk"
                self.x -= 3
                # self.x -= 0.6
            else:
                self.quieto = True
                self.nombre_animacion = "idle"

    def colision(self,bala_rect):
        if bala_rect.colliderect(self.rectangulo_boss["left"]):
            self.vida -= 1
            if self.vida < 6 and self.vida > 0:
                self.ataque_accion = 40
            elif self.vida < 1:
                print("entre")
                self.vivo = False
            return True
        return False

    def muerte(self):
        if not self.vivo:
            self.animacion_delay = 15
            self.nombre_animacion = "death"
            if self.sprite_index == 15:
                self.kill()
                self.rectangulo_boss["left"] = None

