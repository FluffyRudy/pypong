import pygame
from pygame.math import Vector2
from random import choice

class Ball(pygame.sprite.Sprite):
    BALL_SIZE = (20, 20)
    CENTER = (BALL_SIZE[0] // 2, BALL_SIZE[1] // 2)
    RADIUS = (BALL_SIZE[0] + BALL_SIZE[1]) // 4
    SPEED = 8

    def __init__(self, position: tuple[int, int]):
        super().__init__()
        self.image = pygame.Surface(self.BALL_SIZE)
        self.rect = self.image.get_rect(topleft=position)
        self.color = "white"
        self.speedX = self.SPEED * choice([-1, 1])
        self.speedY = self.SPEED * choice([-1, 1])
        self.display_surface_rect = pygame.display.get_surface().get_rect(topleft=(0, 0))

    def update(self):
        pygame.draw.circle(self.image, self.color, self.CENTER, self.RADIUS)
        self.rect.x += (self.speedX)
        self.rect.y += (self.speedY)

        if self.rect.bottom > self.display_surface_rect.bottom  or self.rect.top < 0:
            self.speedY *= -1

    