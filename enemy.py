import pygame
from hitter import Hitter

class Enemy(Hitter):
    def __init__(self, position: tuple[int, int], size: tuple[int, int], group: pygame.sprite.GroupSingle, color=(0, 255, 0, 255)):
        super().__init__(position, size, group, color)

    def update(self, ball: pygame.sprite.Sprite):
        super().update(ball)
        if ball.direction_x < 0 or ball.get_rest():
            return
        center_diff: int = abs(self.rect.centery - ball.rect.centery)
        adjusted_speed: int  = min(center_diff, self.SPEED)

        if ball.rect.centery > self.rect.centery:
            self.rect.y += adjusted_speed
        elif ball.rect.centery < self.rect.centery:
            self.rect.y -= adjusted_speed
