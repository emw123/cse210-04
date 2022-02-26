from game.casting.actor import Actor
from game.casting.cast import Cast
from game.services.keyboard_service import KeyboardService
from game.services.video_service import  VideoService
from game.casting.generator import Generator
import random


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service: KeyboardService, video_service: VideoService):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._generator = Generator        
    def start_game(self, cast, COLS, CELL_SIZE, FONT_SIZE):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        
        self._video_service.open_window()
        while self._video_service.is_window_open():
            x = random.randint(1,12)
            if x == 12:
                self._generator.pop_fallen_items(cast, COLS, CELL_SIZE, FONT_SIZE)
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast: Cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot:Actor = cast.get_first_actor("robots")
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with falling items.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        rocks = cast.get_actors("rocks")
        gems = cast.get_actors("gems")
        border = cast.get_actors("borders")

        banner.set_text("")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        for gem in gems:
            gem.move_next(max_x,max_y)
        for rock in rocks:
            rock.move_next(max_x,max_y)
        for i in range(len(gems)):
            gem = gems[i]
            gem
            # y = gem.get_y()
            if robot.get_position().equals(gem.get_position()):
                message = gem.get_message()
                banner.set_text(message)
                cast.remove_actor("gems", gems[i])
            for n in range(len(border)):
                bord = border[n]
                if bord.get_position().equals(gem.get_position()):
                    cast.remove_actor("gems", gems[i])


        for i in range(len(rocks)):
            rock = rocks[i]
            if robot.get_position().equals(rock.get_position()):
                message = rock.get_message()
                banner.set_text(message)
                cast.remove_actor("rocks" , rocks[i])        
            for n in range(len(border)):
                bord = border[n]
                if bord.get_position().equals(rock.get_position()):
                    cast.remove_actor("rocks", rocks[i])
                    
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
        
        
   