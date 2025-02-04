from game import Game
from shape import Shape
from block import Block
from const import *

import pygame

def draw(screen:pygame.Surface, shape:Block):
    pygame.draw.rect(screen, shape.color, (shape.x*shape.w, shape.y*shape.h, shape.w-2, shape.h-2))

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

            elif event.key == pygame.K_e:
                # rotation right
                game.board.remove_shape(game.board.moving_shape)
                game.board.moving_shape.rotate(game.board, clockwise=False)
                game.board.add_shape(game.board.moving_shape)
            
            elif event.key == pygame.K_a:
                # rotation left
                game.board.remove_shape(game.board.moving_shape)
                game.board.moving_shape.rotate(game.board,clockwise=True)
                game.board.add_shape(game.board.moving_shape)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                game.move_right = False

            elif event.key == pygame.K_q:
                game.move_left = False

    return True

def update(game:Game):
    if game.move_left:
        check_collision = False

        for block in game.board.moving_shape.blocks:
            if block.x == 0:
                check_collision = True

        if not check_collision:
            game.board.remove_shape(game.board.moving_shape)

            for block in game.board.moving_shape.blocks:
                block.move_left()

            game.board.add_shape(game.board.moving_shape)

    elif game.move_right:
        check_collision = False

        for block in game.board.moving_shape.blocks:
            if block.x == 9:
                check_collision = True

        if not check_collision:
            game.board.remove_shape(game.board.moving_shape)

            for block in game.board.moving_shape.blocks:
                block.move_right()

            game.board.add_shape(game.board.moving_shape)
    
    return True

def refresh_graphic(game:Game):
    for row in game.board.matrix:
        for cell in row:
            if type(cell) is Block:
                draw(screen, cell)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("LuTris")

# init data
game = Game()

# TEST
game.board.moving_shape = Shape([Block(3,i, WHITE) for i in range(2,6)], 1)
game.board.add_shape(game.board.moving_shape)
###########

while game.running:
    screen.fill(BLACK)

    game.running = event_handler(game)
    game.running = game.running and update(game)
    refresh_graphic(game)

    pygame.display.flip()
    game.clock.tick(15)

pygame.quit()