import pygame
from Button_class import Button

def help(screen):
    page_1 = pygame.image.load(r"sprite juego\help_1.jpg").convert_alpha()
    page_2 = pygame.image.load(r"sprite juego\help_2.jpg").convert_alpha()
    image_flecha_iz = pygame.transform.scale(pygame.image.load(r"sprite juego\flecha_iz.png"),(80,30)).convert_alpha()
    image_flecha_de = pygame.transform.scale(pygame.image.load(r"sprite juego\flecha_de.png"),(80,30)).convert_alpha()
    list_button = pygame.sprite.Group()
    flecha_de = Button(image_flecha_de,1230,615,"siguiente")
    flecha_iz = Button(image_flecha_iz,1130,615,"siguiente")
    list_button.add(flecha_de)
    list_button.add(flecha_iz)
    run_help = True
    flag_page_1 = True
    flag_page_2 = False
    flag_page_3 = False

    while run_help:
        mouse_pos = pygame.mouse.get_pos()
        if flag_page_1:
            screen.blit(page_1,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    run_help = False
                if event.type == pygame.MOUSEBUTTONDOWN and flecha_de.rect.collidepoint(mouse_pos):
                    flag_page_1 = False
                    flag_page_2 = True
        if flag_page_2:
            screen.blit(page_2,(0,0))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    run_help = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if flecha_de.rect.collidepoint(mouse_pos):
                        flag_page_2 = False
                        flag_page_3 = True
                    if flecha_iz.rect.collidepoint(mouse_pos):
                        flag_page_2 = False
                        flag_page_1 = True
        if flag_page_3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_help = False

        list_button.draw(screen)
        pygame.display.flip()

