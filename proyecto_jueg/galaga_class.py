from typing import Any
import pygame
from constantes import *
class Enemies(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load(r"sprite juego\enemigo.png"),(80,50)).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speed = 2

	def dispara(self):
		laser = Laser(self.rect.centerx,self.rect.bottom)
		laser.speed *= -1
		return laser
	
	def update(self):
		self.rect.x += self.speed 
		if self.rect.x > 1200 or self.rect.x < 0:
			self.speed *= -1
			self.rect.y += 60


class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load(r"sprite juego\player.png"),(90,90)).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x += (SCREEN_WIDTH / 2) - 90
		self.speed_x = 0
		self.lives = 4
		
	def modificar_velocidad(self, x):
		self.speed_x = x

	def update(self):
		self.rect.x += self.speed_x
		self.rect.y = 510

class Laser(pygame.sprite.Sprite):
	def __init__(self,x, y):
		super().__init__()
		self.image = pygame.image.load(r"sprite juego\laser.png").convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speed = SPEED_BALA
		self.power = False

	def update(self):
		if not self.power:
			self.rect.y += self.speed
		if self.power:
			self.rect.y += self.speed * 2.5

class Poder(pygame.sprite.Sprite):
	def __init__(self,x, y):
		super().__init__()
		self.image = pygame.image.load(r"sprite juego\poder.jpg").convert_alpha()
		self.image.set_colorkey((130,132,119))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speed = SPEED_POWER

	def update(self):
		self.rect.y += self.speed
