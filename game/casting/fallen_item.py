from game.casting.actor import Actor
from game.shared.point import Point

# TODO: Implemented the falling item here

class Fallen_Item(Actor):
    def __init__(self):
        super().__init__()
        self._message = ""    
        self._velocity = Point(0, 48)
        
    def set_message(self, message):
        self._message = message
        
    def get_message(self):
        return self._message
    
    def fall(self):
        self.set_velocity
    
    
    
    
