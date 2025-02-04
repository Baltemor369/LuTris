from pygame import time

from board import Board

class Game:
    def __init__(self):
        self.running  = True
        self.clock = time.Clock()
        self.board = Board()
        self.move_left = False
        self.move_right = False
        self.move_down = False