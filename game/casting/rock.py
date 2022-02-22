from game.casting.fallen_item import Fallen_Item


class Rock(Fallen_Item):
    def __init__(self):
        super().__init__()
        self._message = "A rock! -1"    
        
    def reduce_points(self):
        pass