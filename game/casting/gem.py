from game.casting.fallen_item import Fallen_item


class Gem(Fallen_item):
    def __init__(self):
        super().__init__()
        self._message = ""    
        
    def increase_points(self):
        pass