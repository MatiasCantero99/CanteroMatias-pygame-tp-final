import pygame
from constantes import *
from class_personaje_plataforma import *
from class_plataforma import *
from class_boss_plataforma import *
from class_disparo_plataforma import *
from class_enemy_plataforma import *
from class_objeto_plataforma import *
from Funciones_plataforma import *

pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()
image_fondo = pygame.transform.scale(pygame.image.load(r"sprite juego\background_bosque.jpg"),(1280,680)).convert_alpha()
#Grupo
all_sprites_list = pygame.sprite.Group()
plataforma_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
boss_list = pygame.sprite.Group()
boss_disparo_list = pygame.sprite.Group()
player_disparo_list = pygame.sprite.Group()
object_coin_list = pygame.sprite.Group()
object_poison_list = pygame.sprite.Group()
enemy_list = pygame.sprite.Group()

player = Personaje(50,475,DELAY,"idle",231,150,1,screen)
player_list.add(player)
boss = Boss(1200,348,DELAY,"idle",192,128,2.5,0.6)
boss_list.add(boss)
all_sprites_list.add(boss)
enemy = Enemy(20,50,10,"flying",32,32,2,2,False)
enemy_1 = Enemy(1100,100,10,"flying",32,32,2,2,True)
enemy_2 = Enemy(50,250,10,"flying",32,32,2,2,False)
enemy_list.add(enemy)
enemy_list.add(enemy_1)
enemy_list.add(enemy_2)
all_sprites_list.add(enemy)
all_sprites_list.add(enemy_1)
all_sprites_list.add(enemy_2)

plataforma = Plataforma(0,620,1280,40)
plataforma_1 = Plataforma(400,450,300,40)
plataforma_2 = Plataforma(200,300,300,40)
plataforma_3 = Plataforma(500,150,300,40)
plataforma_list.add(plataforma)
plataforma_list.add(plataforma_1)
plataforma_list.add(plataforma_2)
plataforma_list.add(plataforma_3)
all_sprites_list.add(plataforma)
all_sprites_list.add(plataforma_1)
all_sprites_list.add(plataforma_2)
all_sprites_list.add(plataforma_3)

coin = Objeto(plataforma_3.rect.centerx,plataforma_3.rect.centery - 33,pygame.transform.scale(pygame.image.load(r"Wizard Pack\coin\gem_amber__x1_iconic_png_1354831638.png"),(25,25)))
all_sprites_list.add(coin)
coin_1 = Objeto(plataforma_3.rect.centerx + 50,plataforma_3.rect.centery - 33,pygame.transform.scale(pygame.image.load(r"Wizard Pack\coin\gem_ruby__x1_iconic_png_1354831651.png"),(25,25)))
all_sprites_list.add(coin_1)
poison = Objeto(plataforma_2.rect.centerx - 50,plataforma_2.rect.centery - 33,pygame.transform.scale(pygame.image.load(r"Wizard Pack\poison\poison.png"),(25,35)))
all_sprites_list.add(poison)

image_escudo = pygame.transform.scale(pygame.image.load(r"sprite juego\escudo.png"),(310,310)).convert_alpha()
running = True
while running:
    screen.blit(image_fondo,(0,0))
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                player.mover("ataque",2)
            elif event.type == pygame.MOUSEBUTTONUP:
                player.ataque = False
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
                player.mover("defensa",2)
            elif event.type == pygame.MOUSEBUTTONUP:
                player.defensa = False
                player.generar_escudo = False
    if not player.ataque and not player.defensa:
        if keys[pygame.K_d]:
            player.mover("derecha",3)
        elif keys[pygame.K_a]:
            player.mover("izquierda",3)
        elif keys[pygame.K_SPACE]:
            player.mover("saltar",3)
        else:
            player.mover("quieto",3)
    if boss.ataque:
        ataque_boss = Estaca(boss.rect.left - 100,boss.rect.centery + 10,-4,50,30,pygame.image.load(r"frost\arm.png"),False)
        all_sprites_list.add(ataque_boss)
        boss_disparo_list.add(ataque_boss)
        boss.ataque = False

    if player.ataque:
        disparo = player.disparo()
        if disparo != None:
            all_sprites_list.add(disparo)
            player_disparo_list.add(disparo)

    for enemy in enemy_list:
            ataque_enemy = enemy.disparo()
            if ataque_enemy != None:
                all_sprites_list.add(ataque_enemy)
                boss_disparo_list.add(ataque_enemy)

    for poder in player_disparo_list:
        if boss.vivo:
            flag = boss.colision(poder.rect)
            if flag:
                all_sprites_list.remove(poder)
                player_disparo_list.remove(poder)
        enemy_hit = pygame.sprite.spritecollide(poder,enemy_list,False)
        for enemy in enemy_hit:
            poder.kill()
            enemy.verifico_muerte()
            #enemy.vivo = False  #Puede ser un metodo

    all_sprites_list.update()
    all_sprites_list.draw(screen)
    # print(player.contador_plataformas)
    for plataform in plataforma_list:
        player_list.update(plataform.rectangulo)
    player.resetear_contador()
    pygame.sprite.spritecollide(player,boss_disparo_list,player.generar_escudo)
    
    player_list.draw(screen)
    if player.generar_escudo:
        screen.blit(image_escudo,(player.rect.centerx - 120, player.rect.centery - 120))
    if len(player_disparo_list) > 0:
        for disparo in player_disparo_list:
            pygame.draw.rect(screen,"sky blue",disparo.rect,1)
    escribir_pantalla(screen,"lives:","red",r"font\dominican\DOMISC__.TTF",posicion=(0,-20))
    draw_wizard_life(screen,130,0,player.vida,pygame.transform.scale(pygame.image.load(r"Wizard Pack\vida.png"),(40,40)).convert_alpha())
    # pygame.draw.rect(screen,"sky blue",enemy.rect,1)
    pygame.draw.rect(screen,"orange",player.rectangulo_player["bottom"],1)
    pygame.draw.rect(screen,"orange",player.rectangulo_player["left"],1)
    pygame.draw.rect(screen,"orange",player.rectangulo_player["right"],1)
    pygame.draw.rect(screen,"orange",plataforma.rectangulo["top"],1)
    pygame.draw.rect(screen,"orange",plataforma_1.rectangulo["top"],1)
    # pygame.draw.rect(screen,"orange",boss.rectangulo_boss["left"],1)
    # print(plataforma_1.rectangulo["top"],"2")
    # print(player.rectangulo_player["bottom"].colliderect(plataforma.rectangulo["top"]))
    # print(player.rectangulo_player["bottom"].colliderect(plataforma_1.rectangulo["top"]))
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
