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
