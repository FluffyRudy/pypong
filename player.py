import pygame
from hitter import Hitter
from ball import Ball

class Player(Hitter):
    def __init__(self, position: tuple[int, int], size: tuple[int, int], group: pygame.sprite.GroupSingle, color=(0, 255, 0, 255)):
        super().__init__(position, size, group, color)

    def update(self, ball: Ball):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction_y = -1
        elif keys[pygame.K_DOWN]:
            self.direction_y = 1
        else:
            self.direction_y = 0

        self.rect.y += (self.SPEED * self.direction_y)
        
        super().update(ball)