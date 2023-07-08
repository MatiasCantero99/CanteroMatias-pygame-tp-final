import pygame
from Funciones_laberinto import load_sprite_sheets
from Funciones_plataforma import *
from constantes import *
from class_disparo_plataforma import *

class Personaje(pygame.sprite.Sprite):
    def __init__(self,x,y,delay,nombre,width,height,escalar,screen):
        super().__init__()
        self.sprite = load_sprite_sheets("", "wizard pack", width, height,escalar, True)
        self.izquierda = False
        self.x = x
        self.y = y
        self.ataque = False
        self.defensa = False
        self.generar_escudo = False
        self.nombre_animacion = nombre
        self.rect = self.sprite[self.nombre_animacion + "_left"][0].get_rect(topleft=(self.x, self.y))
        self.animacion_delay = delay
        self.contador_animacion = 0
        self.contador = 0
        self.animacion_disparo = False
        self.cantidad_disparo = False
        self.vida = 10
        self.vida_anterior = 0
        #gravedad
        self.gravedad = 1
        self.potencia_salto = -30
        self.limite_caida = 12
        self.saltando = False
        self.cayendo = False
        self.desplazamiento_y = 0
        self.screen = screen
        self.movimiento = 50
        self.contador_plataformas = 0
        
    def update(self,plataforma_rectangulo):
        self.load_sprite()
        self.loop()
        self.aplicar_gravedad(plataforma_rectangulo)

    def load_sprite(self):
        if self.izquierda:
            self.rect = self.sprite[self.nombre_animacion + "_left"][0].get_rect(topleft=(self.x, self.y))
            self.image = self.sprite[self.nombre_animacion + "_left"][0]
        else:
            self.rect = self.sprite[self.nombre_animacion][0].get_rect(topleft=(self.x, self.y))
            self.image = self.sprite[self.nombre_animacion][0]
        #rectangulo bottom
        self.rectangulo_player = generar_rects(self.rect,"player")

    def loop(self):
        if self.izquierda:
            sprites = self.sprite[self.nombre_animacion + "_left"]
        else:
            sprites = self.sprite[self.nombre_animacion]
        self.sprite_index = (self.contador_animacion // self.animacion_delay) % len(sprites)
        self.image = sprites[self.sprite_index]

        self.contador_animacion += 1

        self.rect = self.image.get_rect(topleft=(self.rect.x, self.rect.y))
        # print(self.contador_animacion // self.animacion_delay)
        if self.contador_animacion // self.animacion_delay > len(sprites) and self.nombre_animacion != "attack1":
            self.contador_animacion = 0
        if self.contador_animacion // self.animacion_delay > len(sprites) and self.nombre_animacion == "attack1":
            self.contador_animacion = 130
            self.generar_escudo = True

    def disparo(self):
        if self.ataque:
            if self.sprite_index != 6:
                self.cantidad_disparo = False
            if self.sprite_index == 6 and not self.cantidad_disparo:
                self.cantidad_disparo = True
                if self.izquierda:
                    return Estaca(self.rect.left, self.rect.centery,4,30,10,pygame.image.load(r"Wizard Pack\power.png"),self.izquierda)
                                   
                else:
                    return Estaca(self.rect.right, self.rect.centery,4,30,10,pygame.image.load(r"Wizard Pack\power.png"),self.izquierda)

    

    def mover(self,accion,velocidad):
        self.animacion_delay = DELAY
        match accion:
            case "derecha":
                self.izquierda = False
                if not self.saltando:
                    self.nombre_animacion = "run"
                self.x += velocidad
            case "izquierda":
                self.izquierda = True
                if not self.saltando:
                    self.nombre_animacion = "run"
                self.x -= velocidad
            case "saltar":
                if not self.saltando:
                    self.saltando = True
                    self.desplazamiento_y = self.potencia_salto
                    self.animacion_delay = 40
                    self.nombre_animacion = "jump"
            case "quieto":
                if not self.saltando:
                    self.nombre_animacion = "idle"
            case "ataque":
                self.ataque = True
                self.nombre_animacion = "attack2"
            case "defensa":
                self.defensa = True
                self.nombre_animacion = "attack1"


    def aplicar_gravedad(self,plataforma_rectangulo):
        if self.saltando:
            if self.desplazamiento_y > 0:
                self.nombre_animacion = "fall"
            self.y += self.desplazamiento_y / 2
            if self.desplazamiento_y + self.gravedad < self.limite_caida:
                self.desplazamiento_y += self.gravedad

        if self.rectangulo_player["bottom"].colliderect(plataforma_rectangulo["top"]):
            self.saltando = False
            self.cayendo = False
            self.desplazamiento_y = 0
            self.rectangulo_player["bottom"] = plataforma_rectangulo["top"]

        else:

            self.contador_plataformas += 1
            if self.contador_plataformas > 7:
                self.cayendo = True
        if not self.rectangulo_player["bottom"].colliderect(plataforma_rectangulo["top"]) and not self.saltando:
            if self.desplazamiento_y > 0:
                self.nombre_animacion = "fall"
            self.y += self.desplazamiento_y / 2
            if self.desplazamiento_y + self.gravedad < self.limite_caida and self.cayendo:
                self.desplazamiento_y += self.gravedad
        print(self.desplazamiento_y)
        print(self.gravedad)

    def resetear_contador(self):
        if self.contador_plataformas >= 5:
            self.contador_plataformas = 0

    def colision(self,rect):
        if rect.colliderect(self.rectangulo_player["left"]) or rect.colliderect(self.rectangulo_player["right"]):
            self.vida -= 1
            if self.vida < 1:
                self.vivo = False
            return True
        return False

        # elif self.rectangulo_player["bottom"].colliderect(plataforma_rectangulo["top"]) and self.cayendo:
        #     self.desplazamiento_y += 1
        #     # print("entre")
        #     self.y += self.desplazamiento_y / 2
        #     if self.desplazamiento_y + self.gravedad < self.limite_caida:
        #         self.desplazamiento_y += self.gravedad / 2


        # if self.saltando:
        #     if self.desplazamiento_y >= 0:
        #         self.nombre_animacion = "fall"
        #     self.y += self.desplazamiento_y / 2
        #     self.desplazamiento_y += self.gravedad
        # else:
        #     self.y += self.desplazamiento_y / 2
        #     if self.desplazamiento_y + self.gravedad < self.limite_caida:
        #         self.desplazamiento_y += self.gravedad / 2
        
        # if self.rectangulo_player["bottom"][0] < plataforma_rectangulo["top"][0] -60 and self.rectangulo_player["bottom"][1] <= plataforma_rectangulo["top"][1] -11: #or self.rectangulo_player["bottom"][0] > plataforma_rectangulo["top"][0] +300:
        #     if self.desplazamiento_y >= 0:
        #         self.nombre_animacion = "fall"
        #     self.y += self.desplazamiento_y / 2
        #     if self.desplazamiento_y + self.gravedad < self.limite_caida:
        #         self.desplazamiento_y += self.gravedad
            # self.rect.bottom = plataforma_rectangulo["top"].top 
            # self.rect.bottom = plataforma_rectangulo["top"]
            # self.rectangulo_player["bottom"] = plataforma_rectangulo["top"].top 
            # self.desplazamiento_y = 0
    

