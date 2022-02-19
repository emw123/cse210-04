from game.casting.fallen_item import Fallen_item


class Rock(Fallen_item):
    def __init__(self):
        super().__init__()
        self._message = ""    
        
    def reduce_points(self):
        pass