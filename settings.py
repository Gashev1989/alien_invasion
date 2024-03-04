class Settings():
    """Класс хранения настроек игры."""
    def __init__(self):
        """Инициализация настроек игры."""
        self.screen_width = 1200
        self.screen_heigh = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 2
        self.ship_limit = 3
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализация меняющихся настроек игры."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0
        self.fleet_direction = 1

    def increase_speed(self):
        """Увеличение настроек скорости."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
