class GameStats():
    """Отслеживание статистики игры."""
    def __init__(self, ai_game):
        """Инициализация статистики."""
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """Инициализация статистики, меняющейся в процессе игры."""
        self.ships_left = self.settings.ship_limit
