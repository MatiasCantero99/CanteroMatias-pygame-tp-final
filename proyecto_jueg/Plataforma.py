import pygame
from constantes import *
from class_personaje_plataforma import *
from class_plataforma import *
from class_boss_plataforma import *
from class_disparo_plataforma import *
from class_enemy_plataforma import *
from class_objeto_plataforma import *
from Funciones_plataforma import *

def generar_player(lista_player):
    player = Personaje(lista_player["x"],lista_player["y"],DELAY,lista_player["nombre"],lista_player["width"],lista_player["height"],lista_player["escalar"])
    return player

def generar_boss(lista_boss):
    boss = Boss(lista_boss["x"],lista_boss["y"],DELAY,lista_boss["nombre"],lista_boss["width"],lista_boss["height"],lista_boss["escalar"],lista_boss["velocidad"])
    return boss

def generar_enemy(lista_enemy,grupo_enemy,all_sprite):
    for enemy in lista_enemy:
        enemigo = Enemy(enemy["x"],enemy["y"],enemy["delay"],enemy["nombre"],enemy["width"],enemy["height"],enemy["escalar"],enemy["velocidad"],enemy["posicion"])
        grupo_enemy.add(enemigo)
        all_sprite.add(enemigo)

def generar_plataforma(lista_plataforma,grupo_plataforma,all_sprite):
    for plataform in lista_plataforma:
        plataforma = Plataforma(plataform["x"],plataform["y"],plataform["x_escalar"],plataform["y_escalar"])
        grupo_plataforma.add(plataforma)
        all_sprite.add(plataforma)

def generar_objetos(lista_objetos,grupo_objetos,all_sprite):
    indice = 0
    for object in lista_objetos:
        objeto = Objeto(object["x"],object["y"],pygame.transform.scale(pygame.image.load(object["ruta"]).convert_alpha(),(25,25)),object["nombre"])
        grupo_objetos.add(objeto)
        all_sprite.add(objeto)

def level_3(screen,clock):
    ruta = r"proyecto_jueg\data_level.json"
    lista_nivel = leer_archivo(ruta)

    image_fondo = pygame.transform.scale(pygame.image.load(r"sprite juego\background_bosque.jpg"),(1280,680)).convert_alpha()
    score = 0
    flag_termine = False
    boss_recompensa = 0
    #Grupo
    all_sprites_list = pygame.sprite.Group()
    plataforma_list = pygame.sprite.Group()
    player_list = pygame.sprite.Group()
    boss_list = pygame.sprite.Group()
    boss_disparo_list = pygame.sprite.Group()
    player_disparo_list = pygame.sprite.Group()
    object_coin_list = pygame.sprite.Group()
    enemy_list = pygame.sprite.Group()

    player = generar_player(lista_nivel[0]["player"])
    player_list.add(player)
    boss = generar_boss(lista_nivel[1]["boss"])
    boss_list.add(boss)
    all_sprites_list.add(boss)
    generar_enemy(lista_nivel[2]["enemy"],enemy_list,all_sprites_list)
    generar_plataforma(lista_nivel[3]["plataforma"],plataforma_list,all_sprites_list)
    generar_objetos(lista_nivel[4]["coin"],object_coin_list,all_sprites_list)
    key = Objeto(1050,600,pygame.transform.scale(pygame.image.load(r"Wizard Pack\coin\key_0.png").convert_alpha(),(25,35)),"key")
    object_coin_list.add(key)
    image_escudo = pygame.transform.scale(pygame.image.load(r"sprite juego\escudo.png"),(310,310)).convert_alpha()
    generar_musica(r"sonido\level_3_tema.wav",0.1)
    running = True
    while running:
        screen.blit(image_fondo,(0,0))
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if player.vivo:
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                        player.mover("ataque",2)
                    elif event.type == pygame.MOUSEBUTTONUP:
                        player.ataque = False
                    if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[2]:
                        player.mover("defensa",2)
                    elif event.type == pygame.MOUSEBUTTONUP:
                        player.defensa = False
                        player.generar_escudo = False
        if not player.ataque and not player.defensa and player.nombre_animacion != "hit" and player.vivo:
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
                generar_sonido(r"sonido\disparo_mago.wav",0.1).play(0)
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
                    poder.kill()
            enemy_hit = pygame.sprite.spritecollide(poder,enemy_list,False)
            for enemy in enemy_hit:
                score += 150
                poder.kill()
                enemy.verifico_muerte()

        all_sprites_list.update()
        all_sprites_list.draw(screen)
        for plataform in plataforma_list:
            player_list.update(plataform.rectangulo)
        player.resetear_contador()

        
        disparo_hit_list = pygame.sprite.spritecollide(player,boss_disparo_list,player.generar_escudo)
        for disparo in disparo_hit_list:
            flag = player.colision_disparo(disparo.rect)
            if flag:
                disparo.kill()
        score,flag_termine = player.colision_objeto(object_coin_list,score)
        flag_player_vivo = player.verificar_animacion()
        if flag_player_vivo:
            score = 0
            return score, False
        if flag_termine:
            return score, True
        if len(boss_list) > 0:
            boss_recompensa = boss.muerte()
        else:
            all_sprites_list.add(key)
        if boss_recompensa != None:
            score += boss_recompensa
            boss_recompensa = None
        player_list.draw(screen)
        if player.generar_escudo:
            screen.blit(image_escudo,(player.rect.centerx - 120, player.rect.centery - 120))
        # pygame.draw.rect(screen, "orange", player.rectangulo_player["bottom"], 2)
        escribir_pantalla(screen,"lives:","red",r"font\dominican\DOMISC__.TTF",posicion=(0,-20))
        escribir_pantalla(screen,"score:","red",r"font\dominican\DOMISC__.TTF",score,posicion=(900,-20))
        draw_wizard_life(screen,130,0,player.vida,pygame.transform.scale(pygame.image.load(r"Wizard Pack\vida.png"),(40,40)).convert_alpha())
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
