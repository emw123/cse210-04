import os

from game.casting.actor import Actor
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point
from game.shared.score import Score


FRAME_RATE = 12
MAX_X = (56 * 48) #CHANGE FIRST NUMBER TO CHANGE WINDOW SIZE
MAX_Y = (37 * 48) #CHANGE FIRST NUMBER TO CHANGE WINDOW SIZE
CELL_SIZE = 48
FONT_SIZE = 48
COLS = 60
ROWS = 40
CAPTION = "Robot Finds Kitten"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
#DEFAULT_ARTIFACTS = 40


def main():
    
    # create the cast
    cast = Cast()
    scoreboard = Score( "Score", 600, 400, 10, 10)
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create bottom border
    border_cells = MAX_X / 48
    i = 0
    while i <= border_cells:
        border = Actor()
        border.set_position(Point(i * 48 , 1728))
        cast.add_actor("borders", border)
        i += 1
    
    # create the robot
    x = int(MAX_X / 2)
    y = 1680
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    

        # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    scoreboard.open_window()
    director.start_game(cast, COLS, CELL_SIZE, FONT_SIZE)
if __name__ == "__main__":
    main()