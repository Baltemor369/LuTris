from game import Game
from block import Block
from const import *

import pygame
import random

def get_random_shape():
    return random.choice(shapes)

def draw(screen:pygame.Surface, shape:Block):
    pygame.draw.rect(screen, shape.color, (shape.x * BLOCK_SIZE - BLOCK_SIZE, shape.y * BLOCK_SIZE - BLOCK_SIZE, BLOCK_SIZE - 2, BLOCK_SIZE - 2))

def draw_text(screen: pygame.Surface, text: str, font: pygame.font.Font, x: int, y: int):
    text_surface = font.render(text, True, WHITE)
    screen.blit(text_surface, (x, y))

def event_handler(game:Game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False

            elif event.key == pygame.K_d:
                game.move_right = True

            elif event.key == pygame.K_q:
                game.move_left = True
            
            elif event.key == pygame.K_s:
                game.move_down = True

            elif event.key == pygame.K_e:
                # rotation right
                game.rotate_right()
            
            elif event.key == pygame.K_a:
                # rotation left
                game.rotate_left()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                game.move_right = False

            elif event.key == pygame.K_q:
                game.move_left = False
            
            elif event.key == pygame.K_s:
                game.move_down = False

    return True

def update(game:Game):
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
            # 1. check full lines and destroy them
            game.check_full_lines()
            # 2. generate a new as current moving shape
            game.board.set_moving_shape(get_random_shape().copy())
    
    return True

def refresh_graphic(game:Game, font: pygame.font.Font):
    for row in game.board.matrix[1:-1]:
        for cell in row[1:-1]:
            if type(cell) is Block:
                draw(screen, cell)
    
    # Afficher le score
    draw_text(screen, f'Score: {game.player.score}', font, 10, 10)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("LuTris")

# Initialisez le module font
pygame.font.init()
font = pygame.font.SysFont(None, 36)

# init data
game = Game()
game.board.set_moving_shape(get_random_shape().copy())

while game.running:
    screen.fill(BLACK)

    game.running = event_handler(game)
    game.running = game.running and update(game)
    refresh_graphic(game, font)

    pygame.display.flip()
    game.clock.tick(10)

pygame.quit()