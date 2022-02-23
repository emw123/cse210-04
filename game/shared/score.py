from game.casting.cast import Cast


class Score:
    def __init__(self):
        """Constructs the scoring system for collecting gems with the actor"""
        self._score = self.total_score
        
       
        

    def score(self, cast: Cast):
        """Set score to 0, add 50 points for every gem collected and remove 50 points for every rock hit. Update score."""
        self.total_score = 0
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        rock = cast.get_actors("rocks")
        gem = cast.get_actors("gems")
        for gem in artifacts:
            if robot.get_position().equals(gem.get_position()):
                self.total_score += 50
            else:
                pass
        for rock in artifacts:
            if robot.get_position().equals(rock.get_position()):
                self.total_score -= 50
            else: 
                pass

        return self.total_score
        
        pass