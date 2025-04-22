class GameStats:
    """ Class for handling & reseting the game stats """

    def __init__(self, ai_game):
        # Initialize stats
        self.settings = ai_game.settings
        self.reset_stats()
        self.high_score = 0

    def reset_stats(self):
        # Initialize ingame stats
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1