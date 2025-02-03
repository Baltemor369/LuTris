from const import BLOCK_SIZE

class Block:
    def __init__(self, x, y, c="black"):
        self.x = x
        self.y = y
        self.w = BLOCK_SIZE
        self.h = BLOCK_SIZE
        self.color = c
    
    def move_down(self):
        self.y += 1
    
    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1