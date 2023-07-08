import pygame
from os.path import join, isfile
from os import listdir

def draw_pika_life(screen,x,y,cantidad,image):
        for i in range(cantidad):
            screen.blit(image,(x,y))
            x+= 65

def girar(imagen,frames):
    return pygame.transform.rotozoom(imagen,frames,1)


def normalize_png(png_name: str) -> str:
    return png_name.replace(".png", "").split(" ")[0].lower()

def flip(sprites):
    return [pygame.transform.flip(sprite, True, False) for sprite in sprites]

def load_sprite_sheets(dir1, dir2, width, height,escalar, direction=False):
    path = join(dir1, dir2)
    images = [f for f in listdir(path) if isfile(join(path, f))]

    all_sprites = {}
    for image in images:
        sprite_sheet = pygame.image.load(join(path, image)).convert_alpha()
        sprites = []
        
        for i in range(sprite_sheet.get_width() // width):
            surface = pygame.Surface((width, height), pygame.SRCALPHA, 32)
            rect = pygame.Rect(i * width, 0, width, height)
            surface.blit(sprite_sheet, (0,0), rect)
            sprites.append(pygame.transform.rotozoom(surface,0,escalar))

        if direction:
            #all_sprites[image.replace(".png", "") + "_right"] = sprites
            #all_sprites[image.replace(".png", "") + "_left"] = flip(sprites)
            all_sprites[normalize_png(image)] = sprites #borre + "_right"
            all_sprites[normalize_png(image) + "_left"] = flip(sprites)
        else:
            #all_sprites[image.replace(".png", "")] = sprites
            all_sprites[normalize_png(image)] = sprites

    return all_sprites

def Text(screen,text,x,y,valor):
    if valor == None:
        font = pygame.font.Font(r"font\04b_30\04B_30__.TTF", 40)
        text_lives = font.render(text, True, "yellow")
        screen.blit(text_lives,(x,y))        
    else:
        font = pygame.font.Font(r"font\04b_30\04B_30__.TTF", 40)
        text_lives = font.render(text+" {0}".format(valor), True, "yellow")
        screen.blit(text_lives,(x,y))     

def generar_musica(path: str, volumen: float):
    '''
    Función que se encarga de generar una música de fondo para mi juego
    Recibe el path donde se ubique mi música y el volumen de la misma
    '''
    pygame.mixer.music.stop()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(volumen)

def explosion(rect_x,rect_y):
        animacion_delay = 20
        contador_animacion = 0
        loop()

# def loop(nombre_animacion,animacion_delay,rect_x,rect_y,screen):
    # flag = False
    # if not flag:
    #     contador_animacion = 0
    #     flag = True
    # sprite = load_sprite_sheets("", "sprite juego", 262, 263, 0.2, False)
    # for i in range(len(sprite[nombre_animacion])):
    #     rect = sprite[nombre_animacion][0].get_rect(topleft=(rect_x, rect_y))
    #     image = sprite[nombre_animacion][0]
    #     sprites = sprite[nombre_animacion]
    #     # sprite_index = (contador_animacion // animacion_delay) % len(sprites)
    #     sprite_index = contador_animacion
    #     print(contador_animacion)
    #     image = sprites[sprite_index]

    #     # if sprite_index == 1:
    #     #     animacion_disparo = True
    #     #     self.contador += 1
    #     # if self.animacion_delay >= 120:
    #     #     if self.contador > 60:
    #     #         self.contador_animacion = 0
    #     #         self.contador = 0

    #     screen.blit(image,rect)
    #     contador_animacion += 1

    #     rect = image.get_rect(topleft=(rect_x, rect_y))
    #     # if contador_animacion // animacion_delay > len(sprites):
    #     #     contador_animacion = 0
def loop(nombre_animacion, animacion_delay, rect_x, rect_y, screen):
    sprite = load_sprite_sheets("", "sprite juego", 262, 263, 0.2, False)
    sprites = sprite[nombre_animacion]
    total_sprites = len(sprites)
    contador_animacion = 0

    if contador_animacion // animacion_delay >= total_sprites:
        # La animación ha terminado, se puede restablecer el flag si es necesario
        flag = False
        return

    image = sprites[contador_animacion // animacion_delay]

    screen.blit(image, (rect_x, rect_y))
    contador_animacion += 1


def load_map(path):
    f = open(path,'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    game_map = []
    for row in data:
        game_map.append(list(row))
    return game_map

