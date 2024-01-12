# -- coding: utf-8 --
# level.py
import pygame


class Platform(pygame.Rect):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)

class Level:
    def __init__(self):
        self.block_size = 40
        self.platforms = []
        self.level_data = [
            "-------------------------------------------------",
            "-                                               -",
            "-                                               -",
            "-                                               -",
            "-                                               -",
            "-                                               -",
            "-                                               -",
            "-                                               -",
            "-                                               -",
            "-                                               -",
            "-                                               -",
            "-     ---                                       -",
            "-            ------      -------                -",
            "-            -    -      -     -                -",
            "-            -    -      -     -    --------    -",
            "-            -    -      -     -    -      -    -",
            "-            -    -      -     -    -      -    -",
            "-            -    -      -     -    -      -    -",
            "-            -    -      -     -    -      -    -",
            "-            -    -      -     -    -      -    -",
            "-            -    -      -     -    -      -    -",
            "-            -    -      -     -    -      -    -",
            "-            -    -      -     -    -      -    -",
            "-            -    -      -     -    -      -    -",
            "-            -    -      -     -    -      -    -",
            "-************------******-------****--------****-"

        ]
        self.level_color = (0, 0, 0)

    def check_collision(self, player_rect):
        for platform in self.platforms:
            if platform.colliderect(player_rect.x, player_rect.y + 1, player_rect.width, player_rect.height):
                return True
        return False

    def check_boundary(self, player):
        # Проверка границы и загрузка нового уровня
        pass

    def get_background_color(self):
        # Возвращает цвет фонаы
        return self.level_color
    def draw(self, screen, player_rect,camera_offset_x):
    # Отрисовка уровня с учетом смещения камеры
        camera_offset_x = player_rect.x - screen.get_width() // 4  # Вы можете экспериментировать с коэффициентом деления

        # Очищаем список платформ перед перерисовкой
        self.platforms = []

        # Заполняем список платформ данными о блоках
        for i, row in enumerate(self.level_data):
            for j, tile in enumerate(row):
                if tile == "-":
                    platform_rect = pygame.Rect(j * 40 - camera_offset_x, i * 40, 40, 40)
                    self.platforms.append(platform_rect)  # Добавляем платформу в список
                    pygame.draw.rect(screen, (255, 255, 255), platform_rect)  # Рисуем стены
