from game import Game
from block import Block
from const import *

import pygame
import random

def get_random_shape():
    return random.choice(shapes)

def draw(screen:pygame.Surface, shape:Block):
    pygame.draw.rect(screen, shape.color, (shape.x * BLOCK_SIZE - BLOCK_SIZE, shape.y * BLOCK_SIZE - BLOCK_SIZE, BLOCK_SIZE - 2, BLOCK_SIZE - 2))

def draw_text(screen: pygame.Surface, text: str, font: pygame.font.Font, x: int, y: int, color:tuple[int,int,int]=WHITE):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def draw_rect(screen: pygame.Surface, color, x: int, y: int, width: int, height: int):
    pygame.draw.rect(screen, color, (x, y, width, height))

def event_handler(game:Game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # player want to exit the app
            game.running = False
            game.app_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # player want to quit the game
                if not game.running:
                    game.app_running = False
                game.running = False
            elif event.key == pygame.K_p:
                # player want to pause the game
                game.running = not game.running
                game.paused = not game.paused
                

            if game.running:
                if event.key == pygame.K_d:
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
            if game.running:
                if event.key == pygame.K_d:
                    game.move_right = False

                elif event.key == pygame.K_q:
                    game.move_left = False
                
                elif event.key == pygame.K_s:
                    game.move_down = False

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
    
    # end game check
    if game.board.is_line_full(game.board.matrix[1]):
        # stop the game
        game.running = False
        # record the score
        if game.player.name in game.records:
            if game.player.score > game.records[game.player.name]:
                game.save_record(game.player.name, game.player.score)
            else:
                game.save_record(game.player.name, game.player.score)


def refresh_graphic(game:Game, font: pygame.font.Font):
    # draw panel
    draw_rect(screen, (50, 50, 50), NB_COLS * BLOCK_SIZE, 0, PANEL_WIDTH, PANEL_HEIGHT)


    # draw game board
    for row in game.board.matrix[1:-1]:
        for cell in row[1:-1]:
            if type(cell) is Block:
                draw(screen, cell)
    
    if not game.running:
        draw_text(screen, "Pause", font, GAME_WIDTH / 2 - 20 , GAME_HEIGHT / 2 - 20)

    # display score
    draw_text(screen, f'Score: {game.player.score}', font, NB_COLS * BLOCK_SIZE + 5, 10)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("LuTris")

# Initialisez le module font
pygame.font.init()
font = pygame.font.SysFont(None, 30)

# init data
game = Game()
game.board.set_moving_shape(get_random_shape().copy())

while game.app_running:
    screen.fill(BLACK)

    event_handler(game)
    if game.running:
        update(game)
    refresh_graphic(game, font)

    pygame.display.flip()
    game.clock.tick(10)

pygame.quit()