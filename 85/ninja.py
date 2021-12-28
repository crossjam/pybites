scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
ranks = "white yellow orange green blue brown black paneled red".split()
BELTS = dict(zip(scores, ranks))


class NinjaBelt:
    def __init__(self, score=0):
        self._score = score
        self._last_earned_belt = None

    def _get_belt(self, new_score):
        """Might be a useful helper"""
        new_belt = None
        for score, belt in BELTS.items():
            if score <= new_score:
                new_belt = belt
        return new_belt

    def _get_score(self):
        return self._score

    def _set_score(self, new_score):
        if not isinstance(new_score, int):
            raise ValueError("Score takes an int")
        elif new_score < self._score:
            raise ValueError("Cannot lower score")
        else:
            self._score = new_score
            next_belt = self._get_belt(new_score)
            if next_belt != self._last_earned_belt:
                print(
                    f"Congrats, you earned {self.score} points obtaining the PyBites Ninja {next_belt.title()} Belt"
                )
            else:
                print(f"Set new score to {self.score}")
            self._last_earned_belt = next_belt

    score = property(_get_score, _set_score)
