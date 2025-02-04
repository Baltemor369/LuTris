from block import Block

class Shape:
    def __init__(self, blocks:list[Block]=[], center:int=None):
        self.blocks:list[Block] = blocks
        self.center = center if center is not None and 0 <= center < len(blocks) else 0
            
    def __str__(self):
        return f"Shape({self.center})"

    def rotate(self, board, clockwise=True):
        if not self.blocks:
            return
        
        # Prendre le point central pour la rotation
        center = self.blocks[self.center]
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
            if x < 0 or x >= 10 or y < 0 or y >= 20 or board.get(x,y) is not None:
                return  # Annuler la rotation en cas de collision
            
        # Mettre à jour les positions des blocs
        for i, block in enumerate(self.blocks):
            block.x, block.y = new_positions[i]