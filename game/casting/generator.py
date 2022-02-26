from game.casting.gem import Gem
from game.casting.rock import Rock
from game.shared.color import Color
from game.shared.point import Point
from game.casting.fallen_item import Fallen_Item

import random

class Generator:
    def __init__(self):
        pass    
    
    def pop_fallen_items(cast, COLS, CELL_SIZE, FONT_SIZE):
        rock = Rock()
        gem = Gem()

        n= 0
        while n <= random.randint(1,5):
            r_or_g = random.randint(0,1)
            if r_or_g == 0:
                message = gem.get_message()
                text = "*"
            elif r_or_g == 1:
                message = rock.get_message()
                text = "©"

            x = random.randint(1, COLS - 1)
            y = 0
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = Color(r, g, b)
            
            f_item = Fallen_Item()
            f_item.set_text(text)
            f_item.set_font_size(FONT_SIZE)
            f_item.set_color(color)
            f_item.set_position(position)
            f_item.set_message(message)

            if r_or_g == 0:
                cast.add_actor("gems", f_item)
            elif r_or_g == 1:
                cast.add_actor("rocks", f_item)
            n += 1
            print("fitem populated")