from pygame import time
from datetime import datetime, timedelta

from board import Board

class Game:
    def __init__(self):
        self.running  = True
        self.clock = time.Clock()
        self.board = Board()
        self.move_left = False
        self.move_right = False
        self.move_down = False
        self.last_drop_time = datetime.now()
        self.drop_interval = timedelta(seconds=1)
    
    def should_drop(self):
        current_time = datetime.now()
        if current_time - self.last_drop_time > self.drop_interval:
            self.last_drop_time = current_time
            return True
        return False

    def move_block_left(self):
        self.board.remove_shape(self.board.moving_shape)
        for block in self.board.moving_shape.blocks:
            block.move_left()
        self.board.add_shape(self.board.moving_shape)
    
    def move_block_right(self):
        self.board.remove_shape(self.board.moving_shape)
        for block in self.board.moving_shape.blocks:
            block.move_right()
        self.board.add_shape(self.board.moving_shape)

    def move_block_down(self):        
        self.board.remove_shape(self.board.moving_shape)
        for block in self.board.moving_shape.blocks:
            block.move_down()
        self.board.add_shape(self.board.moving_shape)
        
    def rotate_right(self): 
        self.board.remove_shape(self.board.moving_shape)
        self.board.moving_shape.rotate(self.board, clockwise=False)
        self.board.add_shape(self.board.moving_shape)
    
    def rotate_left(self):
        self.board.remove_shape(self.board.moving_shape)
        self.board.moving_shape.rotate(self.board, clockwise=True)
        self.board.add_shape(self.board.moving_shape)


    def is_empty_left(self):
        check = True
        self.board.remove_shape(self.board.moving_shape)

        for block in self.board.moving_shape.blocks:
            if block.x == 0: # left side touch
                check = False

            elif self.board.get(block.x-1, block.y) != None: # detect smth on left
                check = False

        self.board.add_shape(self.board.moving_shape)

        return check
    
    def is_empty_right(self):
        check = True
        self.board.remove_shape(self.board.moving_shape)

        for block in self.board.moving_shape.blocks:
            if block.x == 9: # right side touch
                check = False

            elif self.board.get(block.x+1, block.y) != None: # detect smth on rgiht
                check = False

        self.board.add_shape(self.board.moving_shape)

        return check
    
    def is_empty_under(self):
        check = True
        self.board.remove_shape(self.board.moving_shape)

        for block in self.board.moving_shape.blocks:
            if self.board.get(block.x, block.y+1) != None: # detect smth under
                check = False

        self.board.add_shape(self.board.moving_shape)
        
        return check