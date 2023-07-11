import pygame
from Player_laberinto_class import Pokeball
# La línea `from Object_laberinto_class import Object` está importando la clase `Object` del módulo
# `Object_laberinto_class`. Esto permite que el código use la clase 'Objeto' definida en ese módulo.
from Object_laberinto_class import Object
from Goal_laberinto_class import Goal
from FireBall_laberinto_class import FireBall
from Muros_laberinto_class import Muro
from Funciones_laberinto import *
from Enemy_laberinto_class import Enemy
from constantes import *


def level_1(screen, clock,all_sprites_list,muro_list,objects_list,entei_list,goal_list):
    score = 0
    x= 100
    y = 205
    flag_win_lose = False
    x_pikachu = X_PIKACHU
    y_pikachu = Y_PIKACHU

    contador = 0
    
    fire_balls_list = pygame.sprite.Group()
    pokeball_list = pygame.sprite.GroupSingle()
    # Cargar imágenes de los muros y otros elementos
    image_ash = pygame.transform.scale(pygame.image.load(r"sprite juego\ash.png"), (100, 80)).convert_alpha()
    pokeball = Pokeball(x,y,screen)
    all_sprites_list.add(pokeball)
    pokeball_list.add(pokeball)
    image_pikachu = pygame.transform.scale(pygame.image.load(r"sprite juego\pikachu_cara.png"),(85,55)).convert_alpha()
    image_fondo = pygame.transform.scale(pygame.image.load(r"sprite juego\fondo_poke.png"),(1280,680)).convert_alpha()

    generar_musica(r"sonido\Pokemon_sound.wav",0.2)
    running = True
    while running:
        screen.blit(image_fondo, (0,0))
        keys = pygame.key.get_pressed()
        if flag_win_lose:
            for event in pygame.event.get():
                if pokeball.life < 1:
                    pokeball.kill()
                    score = 0
                    return  score,False
                elif pokeball.life >= 1:
                    return score,True
            
        elif not flag_win_lose:
            contador += 1
            if contador > 360:
                contador = 0

            # Dibujar los demás elementos
            pikachu_rotada = girar(image_pikachu,contador)
            draw_pika_life(screen,x_pikachu,y_pikachu,pokeball.life,pikachu_rotada)
            pokeball.power(score)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pokeball.kill()
                    score = 0
                    return score,False
                if event.type == pygame.KEYDOWN:
                    pokeball.move = True

            if pokeball.move:
                if keys[pygame.K_d]:
                    pokeball.modificar_velocidad(1.5,0) 
                elif keys[pygame.K_a]:
                    pokeball.izquierda = True
                    pokeball.modificar_velocidad(-2,0)
                elif keys[pygame.K_w]:
                    pokeball.modificar_velocidad(0,-2)
                elif keys[pygame.K_s]:
                    pokeball.modificar_velocidad(0,1.5)
                else:
                    pokeball.modificar_velocidad(0,0)

            for entei in entei_list:
                if entei.animacion_disparo and entei.contador == 1:
                    fire_balls = [FireBall(entei.rect.right, entei.rect.centery - 10) for entei in entei_list]
                    all_sprites_list.add(*fire_balls)
                    fire_balls_list.add(*fire_balls)
                    entei.animacion_disparo = False
                break

            for muro in muro_list:
                fire_balls_hit = pygame.sprite.spritecollide(muro,fire_balls_list,False)
                for fira in fire_balls_hit:
                    # loop("explosion_complete",30,fira.rect.x,fira.rect.y,screen)
                    fira.kill()
                    
            entei_hit = pygame.sprite.spritecollide(pokeball,entei_list,True)
            for entei in entei_hit:
                score += 1000
            
            objects_hit = pygame.sprite.spritecollide(pokeball,objects_list,True)
            for object in objects_hit:
                score += 100
            
            poke_hit = pygame.sprite.spritecollide(pokeball,fire_balls_list,False)
            for poke in poke_hit:
                pokeball.rect.x = x
                pokeball.rect.y = y
                pokeball.life -= 1
                score -= 500
            
            poke_list = pygame.sprite.spritecollide(pokeball,goal_list,False)
            for poke in poke_list:
                poke.kill()
                flag_win_lose = True
            if pokeball.life < 1:
                flag_win_lose = True

            muro_hit = pygame.sprite.spritecollide(pokeball,muro_list, False)	
            for muro in muro_hit:
                pokeball.move = False
                if pokeball.speed_x > 0:
                    pokeball.rect.x += -10
                    pokeball.speed_x = 0
                elif pokeball.speed_x < 0:
                    pokeball.rect.x += 10
                    pokeball.speed_x = 0
                if pokeball.speed_y > 0:
                    pokeball.rect.y += -10
                    pokeball.speed_y = 0
                elif pokeball.speed_y < 0:
                    pokeball.rect.y += 10
                    pokeball.speed_y = 0
                    
            entei_hit = pygame.sprite.spritecollide(pokeball,entei_list,True)
            for entei in entei_hit:
                generar_sonido(r"sonido\captura.wav",0.2).play(0)
                score += 1000
            Text(screen,"lives:","yellow",r"font\04b_30\04B_30__.TTF",posicion=(0,0))
            Text(screen,"score:","yellow",r"font\04b_30\04B_30__.TTF",score,posicion=(900,0))

            all_sprites_list.update()
            all_sprites_list.draw(screen)
            muro_list.draw(screen) 
            screen.blit(image_ash, (0, 200))

        clock.tick(FPS)
        pygame.display.flip()

