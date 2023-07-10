import pygame
from Button_class import Button
from constantes import *
from Help import help
from scape_juego import scape_juego
from SQLite import mostrar_datos,save_score

def menu(screen,clock):
    image_menu = pygame.transform.scale(pygame.image.load(r"sprite juego\scape_menu.png"),(1280,680)).convert_alpha()
    image_escape = pygame.transform.scale(pygame.image.load(r"sprite juego\Escape.png"),(300,100)).convert_alpha()
    play_button = Button(pygame.transform.scale(pygame.image.load(r"sprite juego\image_button.png"),(200,60)).convert_alpha(),SCREEN_WIDTH/2,300,"PLAY")
    quit_button = Button(pygame.transform.scale(pygame.image.load(r"sprite juego\image_button.png"),(200,60)).convert_alpha(),SCREEN_WIDTH/2,400,"QUIT")
    help_button = Button(pygame.transform.scale(pygame.image.load(r"sprite juego\image_button.png"),(200,60)).convert_alpha(),SCREEN_WIDTH/2,500,"HELP")
    name_button = Button(pygame.transform.scale(pygame.image.load(r"sprite juego\image_button.png"),(200,60)).convert_alpha(),1100,50,"NAME")
    rank_button = Button(pygame.transform.scale(pygame.image.load(r"sprite juego\image_button.png"),(200,60)).convert_alpha(),90,50,"RANKING")
    list_button = pygame.sprite.Group()
    list_button.add(quit_button)
    list_button.add(play_button)
    list_button.add(help_button)
    list_button.add(name_button)
    list_button.add(rank_button)
    name = ""
    score = 0
    menu = True
    while menu:
        screen.blit(image_menu,(0,0))
        screen.blit(image_escape,(SCREEN_WIDTH/2-150,100))
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.TEXTINPUT:
                if len(name) < 6:
                    name += event.text
            if event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            if event.type == pygame.QUIT:
                menu = False
            if event.type == pygame.MOUSEBUTTONDOWN and play_button.rect.collidepoint(mouse_pos):
                score = scape_juego(screen,clock)
            elif event.type == pygame.MOUSEBUTTONDOWN and help_button.rect.collidepoint(mouse_pos):
                help(screen)
            elif event.type == pygame.MOUSEBUTTONDOWN and rank_button.rect.collidepoint(mouse_pos):
                mostrar_datos(screen)
            elif event.type == pygame.MOUSEBUTTONDOWN and quit_button.rect.collidepoint(mouse_pos):
                menu = False
        if name != "" and score != 0 and score != None:
            save_score(name,score)
            name = ""
            score = 0
        if name != "":
            name_button.text = name
            name_button.text_render = name_button.font.render(name, True, "black")
            name_button.text_rect = name_button.text_render.get_rect(center=name_button.rect.center)
        else:
            name_button.text = "NAME"
            name_button.text_render = name_button.font.render("NAME", True, "black")
            name_button.text_rect = name_button.text_render.get_rect(center=name_button.rect.center)
        list_button.draw(screen)
        list_button.update()
        for button in list_button:
            screen.blit(button.text_render,button.text_rect)
            if button.rect.collidepoint(mouse_pos):
                button.select = True
            else:
                button.select = False
        clock.tick(FPS)
        pygame.display.flip()


