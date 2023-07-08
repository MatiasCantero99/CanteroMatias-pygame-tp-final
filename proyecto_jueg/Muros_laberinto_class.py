import pygame


class Muro(pygame.sprite.Sprite):
    def __init__(self,x,y,screen):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"sprite juego\madera.png"), (33, 33)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y