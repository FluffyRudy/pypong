import pygame
from hitter import Hitter

class Enemy(Hitter):
    def __init__(self, position: tuple[int, int], size: tuple[int, int], group: pygame.sprite.GroupSingle, color=(0, 255, 0, 255)):
        super().__init__(position, size, group, color)
    
    def follow_ball(self):
        pass

    def update(self, ball: pygame.sprite.Sprite):
        super().update(ball)
