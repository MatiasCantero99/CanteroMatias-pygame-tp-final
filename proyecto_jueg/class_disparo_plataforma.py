import pygame

class Estaca(pygame.sprite.Sprite):
	def __init__(self,x, y,velocidad,escalar_x,escalar_y,image,flip):
		super().__init__()
		self.flip = flip
		self.image = pygame.transform.flip(pygame.transform.scale(image,(escalar_x,escalar_y)),self.flip,False).convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speed = velocidad
		self.power = False

	def update(self):
		if self.flip:
			self.rect.x -= self.speed
		else:
			self.rect.x += self.speed
		if self.rect.x > 1280 or self.rect.x < 0:
			self.kill()