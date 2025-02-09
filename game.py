from pygame import time
from datetime import datetime, timedelta

from player import Player
from board import Board
from const import *

class Game:
    def __init__(self):
        self.running  = True
        self.app_running = True
        self.paused = False
        self.clock = time.Clock()
        self.board = Board()
        self.player = Player("Lucifer")
        self.move_left = False
        self.move_right = False
        self.move_down = False
        self.last_drop_time = datetime.now()
        self.drop_interval = timedelta(seconds=1)
        self.records = {}
    
    def should_drop(self):
        current_time = datetime.now()
        if current_time - self.last_drop_time > self.drop_interval:
            self.last_drop_time = current_time
            return True
        return False

    def fall_blocks(self, index:int):
        for y in range(index, 0, - 1):
            for x in range(1, NB_COLS + 1):
                self.board.set(x, y, None)
                block = self.board.get(x,y-1)
                if  block is not None:
                    self.board.set(x, y-1, None)
                    block.move_down()
                    self.board.set(x, y, block)

    def move_shape_left(self):
        self.board.remove_shape()
        for block in self.board.moving_shape.blocks:
            block.move_left()
        self.board.add_shape()
    
    def move_shape_right(self):
        self.board.remove_shape()
        for block in self.board.moving_shape.blocks:
            block.move_right()
        self.board.add_shape()

    def move_shape_down(self):        
        self.board.remove_shape()
        for block in self.board.moving_shape.blocks:
            block.move_down()
        self.board.add_shape()
        
    def rotate_right(self): 
        self.board.remove_shape()
        self.board.moving_shape.rotate(self.board, clockwise=False)
        self.board.add_shape()
    
    def rotate_left(self):
        self.board.remove_shape()
        self.board.moving_shape.rotate(self.board, clockwise=True)
        self.board.add_shape()


    def is_empty_left(self):
        check = True
        self.board.remove_shape()

        for block in self.board.moving_shape.blocks:
            if block.x == 1: # left side touch
                check = False

            elif self.board.get(block.x-1, block.y) is not None: # detect smth on left
                check = False

        self.board.add_shape()

        return check
    
    def is_empty_right(self):
        check = True
        self.board.remove_shape()

        for block in self.board.moving_shape.blocks:
            if block.x == NB_COLS: # right side touch
                check = False

            elif self.board.get(block.x + 1, block.y) is not None: # detect smth on rgiht
                check = False

        self.board.add_shape()

        return check
    
    def is_empty_under(self):
        check = True
        self.board.remove_shape()

        for block in self.board.moving_shape.blocks:
            if block.y == 20: # bottom side touch
                check = False

            if self.board.get(block.x, block.y + 1) is not None: # detect smth under
                check = False

        self.board.add_shape()
        
        return check
    
    def check_full_lines(self):
        coef = 1
        for y in range(1,NB_ROWS + 1):
            if self.board.is_line_full(self.board.matrix[y][1:-1]):
                self.fall_blocks(y)
                self.player.score += 100 * coef
                coef += 1
    
    def save_record(self, key:str, val:str):
        self.records[key] = val