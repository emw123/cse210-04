<<<<<<< HEAD
import pyray

class Score:
    def __init__(self, caption, width, height, cell_size, frame_rate, debug = False):
        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def get_cell_size(self):
        """Gets the video screen's cell size.
        
        Returns:
            Grid: The video screen's cell size.
        """
        return self._cell_size

    def get_height(self):
        """Gets the video screen's height.
        
        Returns:
            Grid: The video screen's height.
        """
        return self._height

    def get_width(self):
        """Gets the video screen's width.
        
        Returns:
            Grid: The video screen's width.
        """
        return self._width

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)
=======
from game.casting.cast import Cast


class Score:
    def __init__(self):
        """Constructs the scoring system for collecting gems with the actor"""
        self._score = self.total_score
        
       
        

    def score(self, cast: Cast):
        """Set score to 0, add 1 point for every gem collected and remove 1 point for every rock hit. Update score."""
        self.total_score = 0
        robot = cast.get_first_actor("robots")
        #artifacts = cast.get_actors("artifacts")
        rock = cast.get_actors("rocks")
        gem = cast.get_actors("gems")
        for gem in gem:
            if robot.get_position().equals(gem.get_position()):
                self.total_score += 1
            else:
                pass
        for rock in rock:
            if robot.get_position().equals(rock.get_position()):
                self.total_score -= 1
            else: 
                pass

        return self.total_score
        
        pass
>>>>>>> 832d0f40f7349333d147d8695e1351cfd74fadd9
