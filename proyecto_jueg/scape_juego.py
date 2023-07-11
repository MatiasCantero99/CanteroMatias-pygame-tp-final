import pygame
import threading
from constantes import *
from class_arcade import Objeto
from galaga import level_2
from laberinto_posta import level_1
from Plataforma import level_3
from Button_class import Button

from Object_laberinto_class import Object
from Goal_laberinto_class import Goal
from Muros_laberinto_class import Muro
from Funciones_scape import *
from Enemy_laberinto_class import Enemy

def generar_laberinto_thread(screen,muro_list,all_sprites_list,entei_list,objects_list,goal_list):
    generar_laberinto(screen,muro_list,all_sprites_list,entei_list,objects_list,goal_list)


def generar_laberinto(screen,muro_list,all_sprites_list,entei_list,objects_list,goal_list):
    game_map = load_map(r"game_map.txt")
    cell_size = 40
    for row in range(len(game_map)):
            for col in range(len(game_map[row])):
                if game_map[row][col] == "0":
                    muro = Muro(col * cell_size,row * cell_size,screen)
                    muro_list.add(muro)
                elif game_map[row][col] == "1":
                    entei_1 = Enemy(col * cell_size,row * cell_size-22,1.6,screen,120,"entei_0",45,47)
                    all_sprites_list.add(entei_1)
                    entei_list.add(entei_1)
                elif game_map[row][col] == "2":
                    machoke_1 = Object(col * cell_size-10,row * cell_size-5,1.6,screen,60,"machoke_0",30,28)
                    all_sprites_list.add(machoke_1)
                    objects_list.add(machoke_1)
                elif game_map[row][col] == "3":
                    bulbasaur = Goal(col * cell_size-10,row * cell_size-5,1.6,screen,10,"bulbasaur_01",40,33)
                    all_sprites_list.add(bulbasaur)
                    goal_list.add(bulbasaur)

def scape_juego(screen,clock):
    score_global = 0
    score_nivel_1 = 0
    score_nivel_2 = 0
    score_nivel_3 = 0
    #Grupo de sprites para laberinto
    all_sprites_list = pygame.sprite.Group()
    muro_list = pygame.sprite.Group()
    entei_list = pygame.sprite.Group()
    objects_list = pygame.sprite.Group()
    goal_list = pygame.sprite.Group()
    laberinto_thread = threading.Thread(target=generar_laberinto_thread, args=(screen, muro_list, all_sprites_list, entei_list, objects_list,goal_list))
    laberinto_thread.start()
    #termina de formarse el laberinto

    running = True
    fondo_1 = pygame.transform.scale(pygame.image.load(r"sprite juego\background_scape.jpg"),(1280,680)).convert_alpha()
    fondo_2 = pygame.transform.scale(pygame.image.load(r"sprite juego\background_scape_1.jpg"),(1280,680)).convert_alpha()
    arcade_list = pygame.sprite.GroupSingle()
    puerta_list = pygame.sprite.GroupSingle()
    arcade = Objeto(pygame.transform.scale(pygame.image.load(r"sprite juego\arcade_machine_1.png"),(125,225)).convert_alpha(),X_ARCADE,Y_ARCADE)
    puerta = Objeto(pygame.transform.scale(pygame.image.load(r"sprite juego\door.png"),(350,500)).convert_alpha(),980,180)
    lista_image = [pygame.transform.rotozoom(pygame.image.load(r"sprite juego\key_1.png"),35,1),pygame.transform.rotozoom(pygame.image.load(r"sprite juego\key_2.png"),35,1),pygame.transform.rotozoom(pygame.image.load(r"sprite juego\key_3.png"),35,1)]
    arcade_list.add(arcade)
    puerta_list.add(puerta)
    inventario = pygame.image.load(r"sprite juego\inventory.jpg").convert_alpha()
    image_flecha_iz = pygame.transform.scale(pygame.image.load(r"sprite juego\flecha_iz.png"),(90,35)).convert_alpha()
    image_flecha_de = pygame.transform.scale(pygame.image.load(r"sprite juego\flecha_de.png"),(90,35)).convert_alpha()
    list_button = pygame.sprite.Group()
    flecha_de = Button(image_flecha_de,1230,SCREEN_HEIGHT / 2,"siguiente")
    flecha_iz = Button(image_flecha_iz,50,SCREEN_HEIGHT / 2,"siguiente")
    list_button.add(flecha_de)
    list_button.add(flecha_iz)
    flag_background = True
    flag_nivel_1 = False
    flag_nivel_2 = False
    flag_nivel_3 = False

    while running:
        mouse_pos = pygame.mouse.get_pos()
        if flag_background:
            screen.blit(fondo_1,(0,0))
            arcade_list.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and arcade.rect.collidepoint(mouse_pos):
                    if not flag_nivel_3 and flag_nivel_2:
                        score_nivel_3,flag_nivel_3 = level_3(screen,clock)
                        screen_win_lose(screen,flag_nivel_2,r"font\dominican\DOMISC__.TTF","green")
                        score_global += score_nivel_3
                    if not flag_nivel_2 and not flag_nivel_3 and flag_nivel_1:
                        score_nivel_2,flag_nivel_2 = level_2(screen,clock)
                        screen_win_lose(screen,flag_nivel_2,r"font\evil_spin\evilspinDEMO.otf","red")
                        score_global += score_nivel_2
                    if not flag_nivel_1:
                        score_nivel_3,flag_nivel_3 = level_3(screen,clock)
                        # score_nivel_1,flag_nivel_1 = level_1(screen,clock,all_sprites_list,muro_list,objects_list,entei_list,goal_list)
                        screen_win_lose(screen,flag_nivel_1,r"font\04b_30\04B_30__.TTF","yellow")
                        score_global += score_nivel_1
                if event.type == pygame.MOUSEBUTTONDOWN and flecha_de.rect.collidepoint(mouse_pos):
                    flag_background = False
        else:
            screen.blit(fondo_2,(0,0))
            puerta_list.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and puerta.rect.collidepoint(mouse_pos):
                    if flag_nivel_1:
                        return score_global
                if event.type == pygame.MOUSEBUTTONDOWN and flecha_iz.rect.collidepoint(mouse_pos):
                    flag_background = True

        draw_inventario(screen,1000,0,arcade.inventario,inventario)
        draw_key(screen,1003,3,lista_image,flag_nivel_1,flag_nivel_2,flag_nivel_3)
        list_button.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
