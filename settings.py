class Settings():
    """Класс хранения настроек игры."""
    def __init__(self):
        """Инициализация настроек игры."""
        self.screen_width = 1200
        self.screen_heigh = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 2
        self.alien_speed = 1

        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
