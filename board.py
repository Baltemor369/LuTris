from shape import Shape
from block import Block
from const import NB_COLS,NB_ROWS

class Board:
    def __init__(self):
        self.matrix:list[list[Block]] = []
        # init the matrix
        for i in range(NB_ROWS+2): # height
            _ = []
            for j in range(NB_COLS+2): # width
                _.append(None)
            self.matrix.append(_)
        # current moving shape
        self.moving_shape:Shape|None = None
    
    def get(self, x:int, y:int):
        return self.matrix[y][x]
    
    def set(self, x:int, y:int, val:Block|None):
        self.matrix[y][x] = val
    
    def set_moving_shape(self, shape:Shape):
        self.moving_shape = shape
        self.add_shape()
        
    def add_shape(self):
        for block in self.moving_shape.blocks:
            self.set(block.x, block.y, block)
    
    def remove_shape(self):
        for block in self.moving_shape.blocks:
            self.set(block.x, block.y, None)
    
    def is_line_full(self, line:list[Block]):
        for b in line:
            if b is None:
                return False
        return True
    
    def is_line_empty(self, line:list[Block]):
        for b in line:
            if b is not None:
                return False
        return True