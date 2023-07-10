import sqlite3
import pygame
from Funciones_scape import *

def save_score(player_name, score):
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT,
            score INTEGER
        )
    ''')
    cursor.execute('INSERT INTO scores (player_name, score) VALUES (?, ?)', (player_name, score))
    conn.commit()
    conn.close()


def mostrar_datos(screen):
    y= 150
    image_menu = pygame.transform.scale(pygame.image.load(r"sprite juego\scape_menu.png"),(1280,680)).convert_alpha()
    conn = sqlite3.connect('scores.db')
    cursor = conn.cursor()
    contador = 1

    cursor.execute('SELECT * FROM scores ORDER BY score DESC')
    rows = cursor.fetchall()
    running = True
    while running:
        screen.blit(image_menu,(0,0))
        draw_text("SCORE",screen,(300,100),60,"white")
        draw_text("PLAYER",screen,(600,100),60,"white")
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
        for row in rows:
            draw_text(str(row[2]),screen,(300,y),40,"red")
            draw_text(str(row[1]),screen,(600,y),40,"blue")
            y += 50
        y = 150

        pygame.display.flip()
    conn.close()