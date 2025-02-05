# Steps

[x] 1. Create a screen
[x] 2. Display the screen
[x] 3. Create a block
[x] 4. Display the block
[x] 5. Create a chaine
[x] 6. Display the chaine
[x] 7. Create a board to manage Chaines
[x] 8. Display the board
[x] 9. move to right or left the chaine
[x] 10. rotate to right or left the chaine
[x] 11. Keep pressing moving key, keep move the chaine
[x] 11.2 adjust the game clock speed
[x] 12. verify down collision
[x] 13. pressing down key, make fall faster the chaine
[x] 14. automatic fall for chaine (1 tile per 1/2second then faster)
[] 14.2 define all shape possible
[] 14.3 make random selection of the spawning shape 
[] 15. verify full line and destroy it
[] 16. player get a score
[] 17. 

# Error record 




je voudrais un moyen qui me permette d'ajuster la vitesse à laquelle tombe les blocks. plus le temps passe plus il tombe vite, comment faire ?

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
            if block.y == 19: # bottom side touch
                check = False

            if self.board.get(block.x, block.y+1) != None: # detect smth under
                check = False

        self.board.add_shape(self.board.moving_shape)
        
        return check