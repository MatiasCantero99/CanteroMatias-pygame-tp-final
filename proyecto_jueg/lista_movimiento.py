import pygame
from constantes import *

def escribir_pantalla(screen, texto,color,path,cantidad=".",posicion=None):
    font = pygame.font.Font(path, 50)
    text_lives = font.render(texto + "{0}".format(cantidad), True, color)
    if posicion is None:
        center = text_lives.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT/2))
        screen.blit(text_lives,center)
    elif posicion is not None:
        screen.blit(text_lives,posicion)

def actualizar_pantalla(pantalla, personaje,fondo):
    pantalla.blit(fondo,(0,0))
    #plataforma
    personaje.update(pantalla)

def reescalar_imagen(lista_imagenes,tamaño):
    for i in range(len(lista_imagenes)):
        lista_imagenes[i] = pygame.transform.scale(lista_imagenes[i],tamaño)

def obtener_rectangulos(principal)-> dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
    diccionario["righ"] = pygame.Rect(principal.right -2, principal.top, 2,principal.height)
    diccionario["left"] = pygame.Rect(principal.left , principal.top, 2,principal.height)
    diccionario["top"] = pygame.Rect(principal.left , principal.top, principal.width, 10)
    return diccionario

lista_dispara = [pygame.image.load(r"Super_Grotto_Escape_Files\Super Grotto Escape Files\Characters\Player\sprites\Player-shoot\player-shoot1.png"),
                 pygame.image.load(r"Super_Grotto_Escape_Files\Super Grotto Escape Files\Characters\Player\sprites\Player-shoot\player-shoot1.png"),
                 pygame.image.load(r"Super_Grotto_Escape_Files\Super Grotto Escape Files\Characters\Player\sprites\Player-shoot\player-shoot2.png"),
                 pygame.image.load(r"Super_Grotto_Escape_Files\Super Grotto Escape Files\Characters\Player\sprites\Player-shoot\player-shoot2.png"),
                 pygame.image.load(r"Super_Grotto_Escape_Files\Super Grotto Escape Files\Characters\Player\sprites\Player-shoot\player-shoot3.png"),
                 pygame.image.load(r"Super_Grotto_Escape_Files\Super Grotto Escape Files\Characters\Player\sprites\Player-shoot\player-shoot3.png")
]

lista_quieto_d = [pygame.image.load(r"proyecto_jueg\recursos\knight_spear\IDLE\_IDLE_000.png"),
              pygame.image.load(r"proyecto_jueg\recursos\knight_spear\IDLE\_IDLE_001.png"),
              pygame.image.load(r"proyecto_jueg\recursos\knight_spear\IDLE\_IDLE_002.png"),
              pygame.image.load(r"proyecto_jueg\recursos\knight_spear\IDLE\_IDLE_003.png"),
              pygame.image.load(r"proyecto_jueg\recursos\knight_spear\IDLE\_IDLE_004.png") ,
              pygame.image.load(r"proyecto_jueg\recursos\knight_spear\IDLE\_IDLE_005.png"),
              pygame.image.load(r"proyecto_jueg\recursos\knight_spear\IDLE\_IDLE_006.png") 
]
lista_camina= [pygame.image.load(r"proyecto_jueg\recursos\knight_spear\WALK\_WALK_000.png"),
                        pygame.image.load(r"proyecto_jueg\recursos\knight_spear\WALK\_WALK_001.png"),
                        pygame.image.load(r"proyecto_jueg\recursos\knight_spear\WALK\_WALK_002.png"),
                        pygame.image.load(r"proyecto_jueg\recursos\knight_spear\WALK\_WALK_003.png"),
                        pygame.image.load(r"proyecto_jueg\recursos\knight_spear\WALK\_WALK_004.png"),
                        pygame.image.load(r"proyecto_jueg\recursos\knight_spear\WALK\_WALK_005.png"),
                        pygame.image.load(r"proyecto_jueg\recursos\knight_spear\WALK\_WALK_006.png"),
]

lista_salta = [pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_000.png"),
               pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_000.png"),
               pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_001.png"),
               pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_001.png"),
               pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_002.png"),
               pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_002.png"),
               pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_003.png"),
               pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_003.png"),
               pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_004.png"),
               pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_004.png"),
               pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_005.png"),
               pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_005.png"),
               pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_006.png"),
               pygame.image.load(r"proyecto_jueg\recursos\knight_spear\JUMP\_JUMP_006.png"),
]






def update_sprite(self):
        sprite_sheet = 'idle'
        #5 Implementing hit animation (IMPORTANT TO PUT IT AT THE TOP)
        if self.hit:
            sprite_sheet = "hit"
        elif self.y_vel < 0:
            if self.jump_count == 1:
                sprite_sheet = 'jump'
            elif self.jump_count > 1:
                sprite_sheet = 'double_jump'
        elif self.y_vel > self.GRAVITY*2:
            sprite_sheet = "fall"
        elif self.x_vel != 0:
            sprite_sheet = 'run'

        sprite_sheet_name = sprite_sheet + "_" + self.direction
        sprites = self.SPRITES[sprite_sheet_name]
        
        sprite_index = (self.animation_count // self.ANIMATION_DELAY) % len(sprites)
        self.sprite = sprites[sprite_index] #updates every ANIMATION_DELAY frames
        self.animation_count += 1
        self.update()




#  def animar_personaje(self, pantalla):
#     # Asegurar que el índice esté dentro del rango válido
#     indice_imagen = self.cuentaPasos // self.velocidad_animacion % len(self.animacion)
    # pantalla.blit(pygame.transform.flip(self.animacion[indice_imagen], self.izquierda, False), self.rect)
    # pygame.transform.flip(image, self.izquierda,False)

