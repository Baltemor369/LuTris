class Block:
    def __init__(self, x, y, c="black"):
        self.x = x
        self.y = y
        self.color = c
    
    def __str__(self):
        return f"Block({self.x}, {self.y})"
    
    def move_down(self):
        self.y += 1
    
    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1
