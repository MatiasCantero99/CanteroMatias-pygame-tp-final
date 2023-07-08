import pygame
from lista_movimiento import reescalar_imagen, obtener_rectangulos
class Personaje:
    def __init__(self, tamaño,animaciones, posicion_inicial,velocidad):
        #confeccion 
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
        #gravedad
        self.gravedad = 1
        self.potencia_salto = -18
        self.limite_caida = 15
        self.estado_salto = False
        #animaciones
        self.contador_pasos = 0
        self.hace = "quieto"
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.izquierda = False
        self.animacion_contador = 0
        self.delay = 10
        #rectangulo
        rectangulo = self.animaciones["quieto"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)
        #velocidad
        self.velocidad = velocidad
        self.desplazamiento_y = 0
        
        

    #quieto - salta - camina_derecha - camina_izquierda
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagen(self.animaciones[clave],(self.ancho,self.alto))

    def animar (self,pantalla, animacion_usar:str):
        
        sprite_index = (self.animacion_contador // self.delay) % len(self.animaciones[animacion_usar])
        # self.sprite = sprites[sprite_index] #updates every ANIMATION_DELAY frames
        self.animacion_contador += 1
        animacion = self.animaciones[animacion_usar]
        # largo = len(animacion)
        if self.contador_pasos >= sprite_index:
            self.animacion_contador = 0
            self.contador_pasos = 0
        pantalla.blit(pygame.transform.flip(animacion[self.contador_pasos],self.izquierda,False),self.lados["main"])
        self.contador_pasos += 1
    
    def mover(self,velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def aplicar_gravedad(self,pantalla, piso):
        if self.estado_salto:
            self.animar(pantalla, "salta")
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_caida:
                self.desplazamiento_y += self.gravedad

        if self.lados["bottom"].colliderect(piso["top"]):
            self.desplazamiento_y = 0
            self.estado_salto = False
            self.lados["main"].bottom = piso["main"].top

    def update(self,pantalla,lado_piso):
        match self.hace:
            case "derecha":
                if not self.estado_salto:
                    self.animar(pantalla,"camina_derecha")
                self.mover(self.velocidad)
            case "izquierda":
                if not self.estado_salto:
                    self.animar(pantalla,"camina_derecha")
                self.mover(self.velocidad * -1)
            case "salta":
                if not self.estado_salto:
                    self.estado_salto = True
                    self.desplazamiento_y = self.potencia_salto
            case "quieto":
                if not self.estado_salto:
                    self.animar(pantalla,"quieto")
            case "dispara":
                if not self.estado_salto:
                    self.animar(pantalla,"dispara")
        self.aplicar_gravedad(pantalla,lado_piso)
                


