import pygame

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
