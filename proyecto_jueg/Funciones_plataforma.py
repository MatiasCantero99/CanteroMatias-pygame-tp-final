import pygame
from constantes import *
import json



def escribir_pantalla(screen, texto,color,path,cantidad=".",posicion=None):
    font = pygame.font.Font(path, 50)
    text_lives = font.render(texto + "{0}".format(cantidad), True, color)
    if posicion is None:
        center = text_lives.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        screen.blit(text_lives,center)
    elif posicion is not None:
        screen.blit(text_lives,posicion)

def draw_wizard_life(screen,x,y,cantidad,image):
        for i in range(cantidad):
            screen.blit(image,(x,y))
            x+= 30

def generar_rects(principal,para):
    diccionario = {}
    match para:
        case "player":
            diccionario["bottom"] = pygame.Rect(principal.left + 85, principal.bottom - 17, principal.width / 4, 10)
            diccionario["left"] = pygame.Rect(principal.left + 75 , principal.top + 40, 2,principal.height - 50)
            diccionario["right"] = pygame.Rect(principal.right -85, principal.top + 40, 2,principal.height - 50)
        case "boss":
            diccionario["left"] = pygame.Rect(principal.left + 110 , principal.top + 60, 2,principal.height - 100)
        case "plataforma":
            diccionario["top"] = pygame.Rect(principal.left , principal.top, principal.width, 15)
    # match posicion:
    #     case "bottom":
    #         pass
    #     case "top":
    #         diccionario["main"] = principal
    #     case "left":
    #         diccionario["left"] = pygame.Rect(principal.left + 110 , principal.top, 2,principal.height)

    # diccionario["righ"] = pygame.Rect(principal.right -2, principal.top, 2,principal.height)
    return diccionario

def leer_archivo(archivo_json:str) -> list:
    lista_nivel = []
    with open(archivo_json,"r") as archivo:
        diccionario = json.load(archivo)
        lista_nivel = diccionario["niveles"]["level_3"]
    return lista_nivel

def generar_musica(path: str, volumen: float):
    '''
    Función que se encarga de generar una música de fondo para mi juego
    Recibe el path donde se ubique mi música y el volumen de la misma
    '''
    pygame.mixer.music.stop()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volumen)

def generar_sonido(path: str, volumen: float):
    '''
    Función que se encarga de generar un sondi
    Recibe el path en donde se encuentra ese sonido y el volumen del mismo
    Retorna el sonido para esperar a que se ejecute
    '''
    sonido = pygame.mixer.Sound(path)
    sonido.set_volume(volumen)
    return sonido
