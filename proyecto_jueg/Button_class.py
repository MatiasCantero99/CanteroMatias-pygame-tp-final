import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self,image,x,y,text):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x,y))
        self.font = pygame.font.SysFont("Arial Narrow", 40)
        self.text = text
        self.text_render = self.font.render(self.text,True,"black")
        self.text_rect = self.text_render.get_rect(center=self.rect.center)
        self.select = False

    def update(self):
        if self.select:
            self.image = pygame.transform.scale(pygame.image.load(r"sprite juego\image_button_select.png"),(200,60)).convert_alpha()
        else:
            self.image = pygame.transform.scale(pygame.image.load(r"sprite juego\image_button.png"),(200,60)).convert_alpha()