import pygame, random, time
from galaga_class import *
from constantes import *
from Funciones_galaga import *


def level_2(screen,clock):
	running = True
	flag_power = False
	score = 0
	contador = 120
	contador_enemy = 0

	poder = None
	star_time = None

	enemies_list = pygame.sprite.Group()
	all_sprite_list = pygame.sprite.Group()
	laser_list = pygame.sprite.Group()
	power_list = pygame.sprite.Group()
	player_list = pygame.sprite.GroupSingle()
	laser_enemies_list = pygame.sprite.Group()


	for row in range(1,NUM_ROWS):
		for col in range(NUM_ENEMIES_PER_ROW):
			meteor_x = col * METEOR_SPACING_X
			meteor_y = row * METEOR_SPACING_Y
			enemies = Enemies(meteor_x, meteor_y)
			enemies_list.add(enemies)
			all_sprite_list.add(enemies)
	player = Player()
	player_list.add(player)
	all_sprite_list.add(player)
	fondo = pygame.image.load(r"sprite juego\fondo.jpg").convert_alpha()
	fondo_escalar = pygame.transform.scale(fondo,(SCREEN_WIDTH,SCREEN_HEIGHT))
	poder_aleatorio = random.randint(10,15)

	while running:
		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and len(laser_list) < 1:
					laser = Laser(player.rect.centerx - 5,player.rect.top -30)
					laser_list.add(laser)
					all_sprite_list.add(laser)
				if event.key == pygame.K_2:
					player.image = pygame.transform.scale(pygame.image.load(r"sprite juego\julio.png"),(90,90)).convert_alpha()
					for enemi in enemies_list:
						enemi.image = pygame.transform.scale(pygame.image.load(r"sprite juego\iglesia.png"),(80,50)).convert_alpha()
		
		if keys[pygame.K_d]:
			player.modificar_velocidad(5)
		elif keys[pygame.K_a]:
			player.modificar_velocidad(-5)
		else:
			player.modificar_velocidad(0)
		
		if contador_enemy > poder_aleatorio and poder is None:
			poder = Poder(ALEATORIO_X,ALEATORIO_Y)
			all_sprite_list.add(poder)
			power_list.add(poder)

		
		if pygame.sprite.spritecollide(player, power_list, True):
			flag_power = True
			star_time = time.time()
			score += 100
		if flag_power:
			for laser in laser_list:
				laser.power = True
		if star_time != None:
			tiempo_transcurrido = time.time() - star_time
			if tiempo_transcurrido >= 5:
				flag_power = False

		all_sprite_list.update() 

		for laser in laser_list:
			enemies_hit_list = pygame.sprite.spritecollide(laser, enemies_list, True)	
			for enemies in enemies_hit_list:
				all_sprite_list.remove(laser)
				laser_list.remove(laser)
				score += 50
				contador_enemy += 1
			if laser.rect.y < -10:
				all_sprite_list.remove(laser)
				laser_list.remove(laser)

		for laser in laser_enemies_list:
			player_hit = pygame.sprite.spritecollide(laser,player_list, False)	
			for single in player_hit:
				player.lives -= 1
				all_sprite_list.remove(laser)
				laser_enemies_list.remove(laser)
			if laser.rect.y > 680:
				all_sprite_list.remove(laser)
				laser_enemies_list.remove(laser)

		contador -= 1
		if len(enemies_list) > 0:
			enemigo = random.choice(list(enemies_list))
			if contador == 0:
				laser = enemigo.dispara()
				all_sprite_list.add(laser)
				laser_enemies_list.add(laser)
				contador = 120
		
		if player.lives > 0 or len(enemies_list) > 0:
			screen.blit(fondo_escalar,(0,0))
			escribir_pantalla(screen,"score: ","White",r"font\evil_spin\evilspinDEMO.otf",score,(0,0))
			escribir_pantalla(screen,"lives: ","White",r"font\evil_spin\evilspinDEMO.otf",player.lives,(1000,0))
			all_sprite_list.draw(screen)
		if player.lives < 1:
			score = 0
			return score,False
		if len(enemies_list) < 1:
			return score,True


		clock.tick(FPS)
		pygame.display.flip()
