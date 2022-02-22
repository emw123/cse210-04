from game.casting.fallen_item import Fallen_Item


class Gem(Fallen_Item):
    def __init__(self):
        super().__init__()
        self._message = "A gem! +1"    
        
    def increase_points(self):
        pass