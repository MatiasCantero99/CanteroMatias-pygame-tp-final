import pygame
from menu import menu
from constantes import *

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption("Arcade")
    clock = pygame.time.Clock()

    menu(screen,clock)

    pygame.quit()