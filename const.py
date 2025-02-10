from shape import Shape
from block import Block

SCORE_FILE = "score.json"

BLOCK_SIZE = 30
NB_ROWS = 20
NB_COLS = 10

GAME_WIDTH = BLOCK_SIZE * NB_COLS
GAME_HEIGHT = BLOCK_SIZE * NB_ROWS

PANEL_WIDTH = 200
PANEL_HEIGHT = GAME_HEIGHT


SCREEN_HEIGHT = GAME_HEIGHT
SCREEN_WIDTH = GAME_WIDTH + PANEL_WIDTH

BLACK = (0,0,0)
WHITE = (255,255,255)

RED = (255,0,0)
ORANGE = (255,165,0)
PURPLE = (128,0,128)
BLUE = (0,0,255)
CYAN = (0,255,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)

#                           (x,y,w,h)
start_button_rect = (GAME_WIDTH + 10, 10, 80, 40)
rename_button_rect = (GAME_WIDTH + 10, 60, 120, 40)
quit_button_rect = (GAME_WIDTH + 10, SCREEN_HEIGHT - 50, 100, 40)
                         
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