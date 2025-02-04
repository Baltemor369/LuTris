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
            game.move_block_left()

    elif game.move_right:
        if game.is_empty_right():
            game.move_block_right()
    
    if game.move_down:
        if game.is_empty_under():
            game.move_block_down()
    
    if game.should_drop():
        if game.is_empty_under():
            game.move_block_down()
        else:
            # generate a new Shape as current moving shape
            game.board.set_moving_shape(Shape([Block(i,0, BLUE) for i in range(2,6)]))
        
    
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

game.board.set_moving_shape(Shape([Block(5,0, BLUE)]))
game.board.add_shape(Shape([Block(7,i, WHITE) for i in range(3,6)], 1))
game.board.add_shape(Shape([Block(1,i, RED) for i in range(0,6)], 1))
###########

while game.running:
    screen.fill(BLACK)

    game.running = event_handler(game)
    game.running = game.running and update(game)
    refresh_graphic(game)

    pygame.display.flip()
    game.clock.tick(15)

pygame.quit()