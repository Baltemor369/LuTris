from shape import Shape

class Board:
    def __init__(self):
        self.matrix = []
        # init the matrix
        for i in range(20): # height
            _ = []
            for i in range(10): # width
                _.append(None)
            self.matrix.append(_)
        
        # current moving shape
        self.moving_shape:Shape = None
    
    def add_shape(self, shape:Shape):
        for block in shape.blocks:
            self.matrix[block.x][block.y] = block
    
    def remove_shape(self, shape: Shape):
        for block in shape.blocks:
            self.matrix[block.x][block.y] = None