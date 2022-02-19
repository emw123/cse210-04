from game.casting.actor import Actor

# TODO: Implemented the falling item here

class Fallen_item(Actor):
    def __init__(self):
        super().__init__()
        self._message = ""    
        
    def set_message(self, message):
        self._message = message
        
    def get_message(self):
        return self._message