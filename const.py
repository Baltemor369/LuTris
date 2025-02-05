from shape import Shape
from block import Block

import random

BLOCK_SIZE = 30
NB_ROWS = 20
NB_COLS = 10

SCREEN_HEIGHT = BLOCK_SIZE * NB_ROWS
SCREEN_WIDTH = BLOCK_SIZE * NB_COLS

BLACK = (0,0,0)
WHITE = (255,255,255)

RED = (255,0,0)
ORANGE = (255,165,0)
PURPLE = (128,0,128)
BLUE = (0,0,255)
CYAN = (0,255,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
PINK = (255,192,203)
                         
shapes = [
    # line 1x4
    Shape([Block(i,-1) for i in range(3,7)],1, CYAN),
    # cube 2x2
    Shape([
        Block(2,-1),
        Block(3,-1),
        Block(2,-2),
        Block(3,-2)
    ],1, YELLOW),
    # cube 3x3
    Shape([
        Block(2,-3),
        Block(3,-3),
        Block(4,-3),
        Block(2,-2),
        Block(3,-2),
        Block(4,-2),
        Block(2,-1),
        Block(3,-1),
        Block(4,-1)
    ],4, PINK),
    # L 3+2 left
    Shape([
        Block(4,-2),
        Block(4,-1),
        Block(5,-1),
        Block(6,-1),
    ],3, BLUE),
    # L 3+2 right
    Shape([
        Block(6,-2),
        Block(6,-1),
        Block(5,-1),
        Block(4,-1),
    ],3, ORANGE),
    # S 2+2 left
    Shape([
        Block(3,-2),
        Block(4,-2),
        Block(4,-1),
        Block(5,-1),
    ], 1, RED),
    # S 2+2 right
    Shape([
        Block(5,-2),
        Block(4,-2),
        Block(4,-1),
        Block(3,-1),
    ], 1, GREEN),
    # T 3+1
    Shape([
        Block(5,-2),
        Block(4,-1),
        Block(5,-1),
        Block(6,-1),
    ],0, PURPLE)
]