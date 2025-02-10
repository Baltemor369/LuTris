from game import Game
from block import Block
from const import *

import pygame
import datetime
import random
import os
import json
from cryptography.fernet import Fernet

def get_random_shape():
    _ = [random.choice(shapes) for i in range(10)]
    return random.choice(_)

def draw(screen:pygame.Surface, shape:Block):
    pygame.draw.rect(screen, shape.color, (shape.x * BLOCK_SIZE - BLOCK_SIZE, shape.y * BLOCK_SIZE - BLOCK_SIZE, BLOCK_SIZE - 2, BLOCK_SIZE - 2))

def draw_text(screen: pygame.Surface, text: str, font: pygame.font.Font, x: int, y: int, color:tuple[int,int,int]=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_rect(screen: pygame.Surface, color, x: int, y: int, width: int, height: int):
    pygame.draw.rect(screen, color, (x, y, width, height))

def draw_button(screen: pygame.Surface, color, x: int, y: int, width: int, height: int, text: str, font: pygame.font.Font):
    text_surface = font.render(text, True, BLACK)
    w = text_surface.get_width()
    h = text_surface.get_height()
    pygame.draw.rect(screen, color, (x, y, w + 20, h + 20))
    screen.blit(text_surface, (x + 10, y + 10))

def is_button_clicked(x: int, y: int, width: int, height: int, mouse_pos):
    mouse_x, mouse_y = mouse_pos
    return x <= mouse_x <= x + width and y <= mouse_y <= y + height

# Générer ou charger la clé de chiffrement
def load_or_generate_key():
    key_file = "key.key"
    if os.path.exists(key_file):
        with open(key_file, 'rb') as f:
            key = f.read()
    else:
        key = Fernet.generate_key()
        with open(key_file, 'wb') as f:
            f.write(key)
    return key

# Chiffrer le contenu
def encrypt_data(data: bytes, key: bytes) -> bytes:
    fernet = Fernet(key)
    return fernet.encrypt(data)

# Déchiffrer le contenu
def decrypt_data(data: bytes, key: bytes) -> bytes:
    fernet = Fernet(key)
    return fernet.decrypt(data)

# Sauvegarder les scores chiffrés
def save_scores(scores: dict, key: bytes):
    data = json.dumps(scores).encode('utf-8')
    encrypted_data = encrypt_data(data, key)
    with open(SCORE_FILE, 'wb') as f:
        f.write(encrypted_data)

# Charger les scores déchiffrés
def load_scores(key: bytes) -> dict:
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, 'rb') as f:
            encrypted_data = f.read()
        data = decrypt_data(encrypted_data, key)
        return json.loads(data.decode('utf-8'))
    return {}

def input_box(screen, font, x, y, width, height, text):
    pygame.draw.rect(screen, (200, 200, 200), (x, y, width, height))
    txt_surface = font.render(text, True, (0, 0, 0))
    screen.blit(txt_surface, (x + 5, y + 5))

def event_handler(game:Game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # player want to exit the app
            game.app_running = False

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                if not game.input_active:
                    game.game_running = not game.game_running

            if game.game_running:
                if event.key in [pygame.K_d, pygame.K_RIGHT]:
                    game.move_right = True

                elif event.key in [pygame.K_q, pygame.K_LEFT]:
                    game.move_left = True
                
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    game.move_down = True

                elif event.key in [pygame.K_e, pygame.K_UP]:
                    # rotation right
                    game.rotate_right()
                
                elif event.key == pygame.K_a:
                    # rotation left
                    game.rotate_left()
            if game.input_active:
                if event.key == pygame.K_RETURN:
                    game.player.name = game.tmp.capitalize()
                    game.input_active = False

                elif event.key == pygame.K_BACKSPACE:
                    game.tmp = game.tmp[:-1]

                else:
                    game.tmp += event.unicode

        elif event.type == pygame.KEYUP:
            if game.game_running:
                if event.key in [pygame.K_d, pygame.K_RIGHT]:
                    game.move_right = False

                elif event.key in [pygame.K_q, pygame.K_LEFT]:
                    game.move_left = False
                
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    game.move_down = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if is_button_clicked(*start_button_rect, event.pos):
                    if not game.input_active:
                        if game.game_end:
                            game.restart()
                            game.board.set_moving_shape(get_random_shape().copy())
                        else:
                            game.game_running = True

                    
                if is_button_clicked(*quit_button_rect, event.pos):
                    game.app_running = False
                
                if is_button_clicked(*rename_button_rect, event.pos):
                    game.game_running = False
                    game.input_active = not game.input_active
                    game.tmp = ""
                
                    
def update(game:Game):
    if game.game_running:
        if game.move_left:
            if game.is_empty_left():
                game.move_shape_left()

        elif game.move_right:
            if game.is_empty_right():
                game.move_shape_right()
        
        if game.move_down:
            if game.is_empty_under():
                game.move_shape_down()
        
        if game.should_drop():
            if game.is_empty_under():
                game.move_shape_down()
            else:
                # new block generation
                # 1. check full lines
                game.check_full_lines()
                # 2. generate a new as current moving shape
                game.board.set_moving_shape(get_random_shape().copy())
        
                game.drop_interval -= datetime.timedelta(milliseconds=10)
        
        # end game check
        game.board.remove_shape()
        if not game.board.is_line_empty(game.board.matrix[1][1:-1]):
            # stop the game
            game.game_end = True
            game.game_running = False

            # record the score
            if game.player.name in game.records:
                if game.player.score > game.records[game.player.name]:
                    game.save_record(game.player.name, game.player.score)
            else:
                game.save_record(game.player.name, game.player.score)
            game.records = dict(sorted(game.records.items(), key=lambda item: item[1]))
        game.board.add_shape()


def refresh_graphic(game:Game, screen:pygame.Surface, font:pygame.font.Font):
    # draw panel
    # background
    draw_rect(screen, (50, 50, 50), NB_COLS * BLOCK_SIZE, 0, PANEL_WIDTH, PANEL_HEIGHT)
    # buttons
    draw_button(screen, (41, 150, 139), *start_button_rect, "Start", font)
    draw_button(screen, (41, 150, 139), *rename_button_rect, "Rename", font)
    draw_button(screen, (41, 150, 139), *quit_button_rect, "Quitter", font)
    # stats
    if game.input_active:
        draw_text(screen, f"=>{game.tmp}", font, GAME_WIDTH + 10, 120)
    draw_text(screen, f'Player: {game.player.name}', font, GAME_WIDTH + 10, 150)
    draw_text(screen, f'Score: {game.player.score}', font, GAME_WIDTH + 10, 180)

    i = 0
    for key, val in game.records.items():
        draw_text(screen, f'{key}: {val}', font, GAME_WIDTH + 10, SCREEN_HEIGHT // 2 + 35 * i)
        i += 1

    # draw game board
    if game.game_running:
        draw_rect(screen, RED, 0,BLOCK_SIZE*1-1, GAME_WIDTH,1)

        for row in game.board.matrix[1:-1]:
            for cell in row[1:-1]:
                if type(cell) is Block:
                    draw(screen, cell)
    
    if not game.game_end and not game.game_running:
        draw_text(screen, "Pause", font, GAME_WIDTH / 2 - 20 , GAME_HEIGHT / 2 - 20)
    if game.game_end:
        draw_text(screen, "End", font, GAME_WIDTH / 2 - 20 , GAME_HEIGHT / 2 - 20)



pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("LuTris")

# Initialisez le module font
pygame.font.init()
font = pygame.font.SysFont(None, 36)

# init data
game = Game()
key = load_or_generate_key()
game.records = load_scores(key)
game.board.set_moving_shape(get_random_shape().copy())

while game.app_running:
    screen.fill(BLACK)

    event_handler(game)
    update(game)
    refresh_graphic(game, screen, font)

    pygame.display.flip()
    game.clock.tick(10)

save_scores(game.records, key)
pygame.quit()