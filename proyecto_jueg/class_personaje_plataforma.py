import pygame
from Funciones_laberinto import load_sprite_sheets
from Funciones_plataforma import *
from constantes import *
from class_disparo_plataforma import *

class Personaje(pygame.sprite.Sprite):
    def __init__(self,x,y,delay,nombre,width,height,escalar):
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
        self.vivo = True
        self.vida = 10
        self.vida_anterior = 0
        #gravedad
        self.gravedad = 1
        self.potencia_salto = -30
        self.limite_caida = 12
        self.saltando = False
        self.cayendo = False
        self.desplazamiento_y = 0
        self.movimiento = 50
        self.contador_plataformas = 0
        
    def update(self,plataforma_rectangulo):
        """
        Recibe por parametro la plataforma del rectangulo
        Recorre otros metodos llamandolos a funcion del personaje
        No devuelve nada
        """
        self.load_sprite()
        self.loop()
        self.aplicar_gravedad(plataforma_rectangulo)

    def load_sprite(self):
        """
        -No recibe nada por parametro
        -Carga los sprite generados en la funcion load_sprite_sheets, se pregunta si el personaje
        esta a la izquierda o no y en base a eso toma la imagen y el rect, despues genera unos rectangulos
        a los costados del personaje para hacer las colisiones mas precisas
        -No devuelve nada
        """
        if self.izquierda:
            self.rect = self.sprite[self.nombre_animacion + "_left"][0].get_rect(topleft=(self.x, self.y))
            self.image = self.sprite[self.nombre_animacion + "_left"][0]
        else:
            self.rect = self.sprite[self.nombre_animacion][0].get_rect(topleft=(self.x, self.y))
            self.image = self.sprite[self.nombre_animacion][0]
        #rectangulo bottom
        self.rectangulo_player = generar_rects(self.rect,"player")

    def loop(self):
        """
        -No recibe nada por parametro
        -Se pregunta si esta a la izquierda o no, entra por clave a un diccionario y toma la imagen dentro
        hace una cuenta donde el resultado siempre es 0,1,2,3... para saber que imagen tomar para las animaciones
        y las coloca en el self.image, por ultimo se pregunta si el personaje esta usando la animacion attack1 
        que en este caso es un escudo defensivo para el personaje asi lo mantiene siempre en la misma animacion
        -No devuelve nada
        """
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
        """
        -No recibe nada por parametro
        -Verifica que si el personaje esta atacando y el index (la posicion de la imagen) es el 6 va a generar
        un disparo para que se vea el disparo justo cuando el mago extiende la mano
        -Retorna un disparo a la izquierda o derecha (el disparo es generado en otra clase)
        """
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
        """
        -Recive por parametro la accion del personaje y su velocidad
        -Reinicia siempre el delay a su estado base y le cambia la animacion al personaje en base a la 
        accion generado por nosotros al movernos
        -No retorna nada
        """
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
        """
        -Recibe el rectangulo de la plataforma por parametro
        -Verifica que si salta aplica un impulso hacia arriba hasta cierto limita y despues baja, cuando cae
        la animacion pasa a ser "fall". Luego se pregunta si no esta chocando con ninguna platafarma y su contador
        es mayor a 7 entonces el personaje esta cayendo y va a caer
        -No retorna nada
        """
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

    def resetear_contador(self):
        """
        -No recibe nada por parametro
        -Verifica que si el contador de plataformas en mayor o igual a 5 lo vuelva a poner a 0
        -No retorna nada
        """
        if self.contador_plataformas >= 5:
            self.contador_plataformas = 0

    def colision_disparo(self,rect):
        """
        -Recibe un rect por parametro
        -Verifica si el disparo del enemigo impacta en el personaje con los rects creados antes, de ser asi se le resta
        vida y en el caso de ser 0 la vida entonces el estado vivo pasa False y genera animacion de "death"
        -Retorna un True o False para verificar el estado del personaje y verificar su muerte
        """
        if rect.colliderect(self.rectangulo_player["left"]) or rect.colliderect(self.rectangulo_player["right"]):
            self.vida -= 1
            self.nombre_animacion = "hit"
            self.animacion_delay = 40
            if self.vida < 1:
                self.vivo = False
                self.nombre_animacion = "death"
                self.animacion_delay = 40
            return True
        return False

    def colision_objeto(self,objeto_list,score):
        """
        -Recibe una lista de objetos y el score por parametro
        -Verifico la colision con el objeto con los rects generados antes, le doy puntos al personaje si el objeto es
        un "ambar" o "ruby" y si es el "veneno" entonces se le restara una vida, cuando obtenga la llave el score
        aumenta y tambien se termina el juego por eso el flag pasa a True
        -Rertorna un True o False para verificar si se termino el juego
        """
        flag = False
        for objeto in objeto_list:
            if objeto.rect.colliderect(self.rectangulo_player["left"]) or objeto.rect.colliderect(self.rectangulo_player["right"]):
                if objeto.nombre == "ruby":
                    score += 200
                elif objeto.nombre == "ambar":
                    score += 150
                elif objeto.nombre == "veneno":
                    self.vida -= 1
                elif objeto.nombre == "key":
                    score += 250
                    flag = True
                objeto.kill()
        return score, flag


    
    def verificar_animacion(self):
        """
        -No recibe nada por parametro
        -Verifica dos animaciones especificas, el "hit" para que cuando se termine su animacion automaticamente pase a estado de "idle"
        y "death", en este caso se genera el sonido de muerte y cuando la animacion sea la ultima entonces devuelve un flag
        True y elimino al personaje de la lista
        -Retorna un flag True o False, en caso de ser True el juego se termina porque el personaje ya termino su 
        animacion de muerte
        """
        flag = False
        if self.nombre_animacion == "hit":
            if self.sprite_index == 3:
                self.nombre_animacion = "idle"
        elif self.nombre_animacion == "death":
            generar_sonido(r"sonido\muerte_wizard.wav",0.2).play(0)
            if self.sprite_index == 6:
                flag = True
                self.kill()
        return flag


    