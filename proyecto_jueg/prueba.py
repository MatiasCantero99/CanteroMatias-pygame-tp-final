import pygame, random
from pygame.locals import *
from lista_movimiento import *
from class_personaje import *
from modo import *

def actualizar_pantalla(pantalla, personaje,fondo,lados_piso):
    pantalla.blit(fondo,(0,0))
    #plataforma
    personaje.update(pantalla, lados_piso)




#Ventana de juego
screen_width = 1280
screen_height = 680
screen = pygame.display.set_mode([screen_width,screen_height])
FPS = 60
#fondo
fondo = pygame.image.load(r"Recursos Pygame-20230619T170728Z-001\\Recursos Pygame\Assets\\locations\set_bg_05\\1_game_background\\1_game_background.png")
fondo_escalar = pygame.transform.scale(fondo,(screen_width,screen_height))


pygame.init()
clock = pygame.time.Clock()

#personaje
posicion_inicial = (0,screen_height-220)
tamaño = (150,150)
diccionario_animacion = {}
diccionario_animacion["quieto"] = lista_quieto_d
diccionario_animacion["camina_derecha"] = lista_camina
diccionario_animacion["salta"] = lista_salta
diccionario_animacion["dispara"] = lista_dispara

player = Personaje(tamaño,diccionario_animacion,posicion_inicial, 3)

#piso
piso = pygame.Rect(0,0,screen_width,20)
piso.top = player.lados["main"].bottom
lado_piso = obtener_rectangulos(piso)

running = True
while running:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_TAB:
            cambiar_modo()

    if keys[pygame.K_d]:
        player.izquierda = False
        player.hace = "derecha"
    elif keys[pygame.K_a]:
        player.izquierda = True
        player.hace = "izquierda"
    elif keys[pygame.K_w]:
        player.hace = "salta"
    elif keys[pygame.K_z]:
        player.hace = "dispara"
    else:
        player.hace = "quieto"
    actualizar_pantalla(screen,player,fondo_escalar, lado_piso)
    
    if get_modo():
        for lado in lado_piso:
            pygame.draw.rect(screen,"Orange", lado_piso[lado],3)

        for lado in player.lados:
            pygame.draw.rect(screen, "Blue", player.lados[lado],3)
    clock.tick(FPS)
    

    pygame.display.flip()

pygame.quit()
