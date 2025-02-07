from block import Block

class Shape:
    def __init__(self, blocks:list[Block]=[], c="WHITE", allow_rotate=True):
        self.blocks:list[Block] = blocks
        self.color:str = c
        self.allow_rotate:bool = allow_rotate
        for b in self.blocks:
            b.color = c

    def copy(self):
        new_blocks = [Block(b.x, b.y, b.color) for b in self.blocks]
        return Shape(new_blocks, self.color, self.allow_rotate)

    def rotate(self, board, clockwise=True):
        if self.allow_rotate is False or not self.blocks:
            return
        
        center = self.blocks[0]
        new_positions = []

        for block in self.blocks:
            rel_x, rel_y = block.x - center.x, block.y - center.y
            if clockwise:
                new_x, new_y = rel_y, -rel_x
            else:
                new_x, new_y = -rel_y, rel_x
            
            new_positions.append((center.x + new_x, center.y + new_y))
        
        # Vérifier les nouvelles positions
        for x, y in new_positions:
            if x < 1 or x >= 11 or y < 1 or y >= 21 or board.get(x,y) is not None:
                return  # Annuler la rotation en cas de collision
            
        # Mettre à jour les positions des blocs
        for i, block in enumerate(self.blocks):
            block.x, block.y = new_positions[i]