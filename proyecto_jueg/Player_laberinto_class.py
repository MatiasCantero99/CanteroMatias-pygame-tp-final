import pygame

class Pokeball(pygame.sprite.Sprite):
    def __init__(self,x,y,screen):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(r"sprite juego\pokeball.png"), (30, 30)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.life = 3
        self.screen = screen
        self.izquierda = False
        self.izquierda_presionada = False
        self.transform = False
        self.move = False
        self.power_active = False
    
    def posicion(self):
        if self.izquierda and not self.izquierda_presionada:
            self.image = pygame.transform.flip(self.image,self.izquierda,False)
            self.izquierda_presionada = True
        elif  not self.izquierda and self.izquierda_presionada:
            self.image = pygame.transform.flip(self.image, self.izquierda_presionada, False)
            self.izquierda_presionada = False

    
    def modificar_velocidad(self, x:0,y:0):
        self.speed_x = x
        self.speed_y = y
    
    def power(self,score):
        if score > 1500 and not self.power_active:
            if not self.izquierda:
                self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(r"sprite juego\superball.png"), (30, 30)).convert_alpha(),True,False)
                self.power_active = True
            else:
                self.image = pygame.transform.scale(pygame.image.load(r"sprite juego\superball.png"), (30, 30)).convert_alpha()
                self.power_active = True
        elif score < 1500 and self.power_active:
            self.image = pygame.transform.scale(pygame.image.load(r"sprite juego\pokeball.png"), (30, 30)).convert_alpha()
            self.power_active = False


    def update(self):
        if self.rect.x < 95 and self.rect.y < 215:
            self.rect.x += 5
        else:
            self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.posicion()
        self.izquierda = False