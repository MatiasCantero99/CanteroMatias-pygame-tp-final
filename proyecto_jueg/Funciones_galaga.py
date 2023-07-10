import pygame
from constantes import *



def escribir_pantalla(screen, texto,color,path,cantidad="",posicion=None):
    font = pygame.font.Font(path, 50)
    text_lives = font.render(texto + "{0}".format(cantidad), True, color)
    if posicion is None:
        center = text_lives.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        screen.blit(text_lives,center)
    elif posicion is not None:
        screen.blit(text_lives,posicion)

def draw_nave_life(screen,x,y,cantidad,image):
        for i in range(cantidad):
            screen.blit(image,(x,y))
            x+= 65