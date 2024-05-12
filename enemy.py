import pygame
from hitter import Hitter

class Enemy(Hitter):
    def __init__(self, position: tuple[int, int], size: tuple[int, int], group: pygame.sprite.GroupSingle, color=(0, 255, 0, 255)):
        super().__init__(position, size, group, color)
        self.placed_direction = 1

    def update(self, ball: pygame.sprite.Sprite):
        super().update(ball)
        if ball.direction_x < 0 or ball.get_out_attr():
            return
        if ball.rect.centery > self.rect.centery:
            self.rect.y += self.SPEED
        elif ball.rect.centery < self.rect.centery:
            self.rect.y += (self.SPEED * -1)
