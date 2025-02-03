from board import Board
from shape import Shape
from block import Block
from const import *

import pygame

def draw(screen:pygame.Surface, shape:Block):
    pygame.draw.rect(screen, shape.color, (shape.x*shape.w, shape.y*shape.h, shape.w-2, shape.h-2))

def event_handler():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False

            elif event.key == pygame.K_d:
                board.remove_shape(board.moving_shape)
                for block in board.moving_shape.blocks:
                    if block.x < 9:
                        block.move_right()
                board.add_shape(board.moving_shape)

            elif event.key == pygame.K_q:
                board.remove_shape(board.moving_shape)
                for block in board.moving_shape.blocks:
                    if block.x > 0:
                        block.move_left()
                board.add_shape(board.moving_shape)

            elif event.key == pygame.K_e:
                # rotation right
                pass
            
            elif event.key == pygame.K_a:
                # rotation left
                pass
    
    return True

def update():
    pass

def flip():
    for row in board.matrix:
        for cell in row:
            if type(cell) is Block:
                draw(screen, cell)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("LuTris")

# init data
running  = True
clock = pygame.time.Clock()
board = Board()

# TEST
board.moving_shape = Shape([Block(2,2, WHITE), Block(2,1, WHITE), Block(2,0, WHITE)])
board.add_shape(board.moving_shape)
###########

while running:
    screen.fill(BLACK)

    running = event_handler()
    
    update()
    
    flip()

    pygame.display.flip()
    clock.tick(30)

pygame.quit()