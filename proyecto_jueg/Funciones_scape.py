import pygame
from constantes import *
def load_map(path):
    f = open(path,'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

def draw_inventario(screen,x,y,cantidad,image):
        for i in range(cantidad):
            screen.blit(image,(x,y))
            x+= 65

def draw_key(screen,x,y,lista_image,flag_1,flag_2,flag_3):
        if flag_1:
            screen.blit(lista_image[0],(x,y))
            x+= 65
        if flag_2:
            screen.blit(lista_image[1],(x,y))
            x+= 65
        if flag_3:
            screen.blit(lista_image[2],(x,y))
            x+= 65
def screen_win_lose(screen,flag,path,color):
    running = True
    while running:
        screen.fill((0, 0, 0))
        font = pygame.font.Font(path, 40)
        if flag:
            text_lives = font.render("Ganaste, toca enter para continuar", True, color)
        else:
             text_lives = font.render("perdiste, toca enter para continuar", True, color)
        center = text_lives.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        screen.blit(text_lives,center)
        for event in pygame.event.get():
             if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    running = False
        pygame.display.flip()

def draw_text(texto,screen,posicion,tamaño,color):
    font = pygame.font.SysFont("Arial Narrow",tamaño)
    text = font.render(texto, True, color)
    screen.blit(text,posicion)
