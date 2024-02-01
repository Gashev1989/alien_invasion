import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Класс для управления ресурсами игры."""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_heigh)
        )
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)

    def run_game(self):
        """Запуск игры."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Обработка нажатия клавиш и событий мыши."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    sys.exit()
    
    def _update_screen(self):
        """Обновление изображения на экране и отображение нового экрана."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
