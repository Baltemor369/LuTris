from shape import Shape
from block import Block

import random

BLOCK_SIZE = 30
NB_ROWS = 20
NB_COLS = 10

PANEL_WIDTH = 100
PANEL_HEIGHT = BLOCK_SIZE * NB_ROWS

SCREEN_HEIGHT = BLOCK_SIZE * NB_ROWS
SCREEN_WIDTH = BLOCK_SIZE * NB_COLS + PANEL_WIDTH

BLACK = (0,0,0)
WHITE = (255,255,255)

RED = (255,0,0)
ORANGE = (255,165,0)
PURPLE = (128,0,128)
BLUE = (0,0,255)
CYAN = (0,255,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
                         
shapes = [
    # line 1x4
    Shape([
        Block(5,0),
        Block(4,0),
        Block(6,0),
        Block(7,0)
    ], CYAN),
    # cube 2x2
    Shape([
        Block(3,0),
        Block(3,-1),
        Block(4,0),
        Block(4,-1)
    ], YELLOW, False),
    # L 3+2 left
    Shape([
        Block(4,0),
        Block(4,-1),
        Block(5,0),
        Block(6,0),
    ], BLUE),
    # L 3+2 right
    Shape([
        Block(6,0),
        Block(6,-1),
        Block(5,0),
        Block(4,0),
    ], ORANGE),
    # S 2+2 left
    Shape([
        Block(4,0),
        Block(5,0),
        Block(4,-1),
        Block(3,-1),
    ], RED),
    # S 2+2 right
    Shape([
        Block(4,0),
        Block(3,0),
        Block(4,-1),
        Block(5,-1),
    ], GREEN),
    # T 3+1
    Shape([
        Block(5,0),
        Block(4,0),
        Block(5,-1),
        Block(6,0),
    ], PURPLE)
]