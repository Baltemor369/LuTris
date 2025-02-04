from shape import Shape
from block import Block

BLOCK_SIZE = 30

SCREEN_HEIGHT = BLOCK_SIZE * 20
SCREEN_WIDTH = BLOCK_SIZE * 10

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
ORANGE = (255,165,0)
PINK = (255,255,0)
BLUE = (0,0,255)
CYAN = (0,255,255)
GREEN = (0,255,0)
YELLOW = (255,0,255)

shapes = [
    # line 1x4
    Shape([Block(i,0,BLUE) for i in range(2,6)],1),
    # cube 2x2
    Shape([
        Block(2,0,CYAN),
        Block(3,0,CYAN),
        Block(2,-1,CYAN),
        Block(3,-1,CYAN)
    ],1),
    # cube 3x3
    Shape([
        Block(2,0,ORANGE),
        Block(3,0,ORANGE),
        Block(4,0,ORANGE),
        Block(2,-1,ORANGE),
        Block(3,-1,ORANGE),
        Block(4,-1,ORANGE),
        Block(2,-2,ORANGE),
        Block(3,-2,ORANGE),
        Block(4,-2,ORANGE)
    ],4),
    # rect 4x2
    Shape([
        Block(2,0,YELLOW),
        Block(3,0,YELLOW),
        Block(4,0,YELLOW),
        Block(5,0,YELLOW),
        Block(2,-1,YELLOW),
        Block(3,-1,YELLOW),
        Block(4,-1,YELLOW),
        Block(5,-1,YELLOW)
    ]),
    # L 3+2 left
    # L 3+2 right
    # S 2+2 left
    # S 2+2 right
    # T 3+1
]