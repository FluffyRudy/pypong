import pygame
from pygame.math import Vector2
from random import choice

class Ball(pygame.sprite.Sprite):
    BALL_SIZE = (20, 20)
    CENTER = (BALL_SIZE[0] // 2, BALL_SIZE[1] // 2)
    RADIUS = (BALL_SIZE[0] + BALL_SIZE[1]) // 4
    SPEED = 8
    FACTOR = 0.1 #either to increase or decrease speed by 10%

    #adding offset
    def __init__(self, position: tuple[int, int], offset_x: int):
        super().__init__()
        self.image = pygame.Surface(self.BALL_SIZE)
        self.rect = self.image.get_rect(topleft=position)
        self.color = "white"
        self.direction_x = choice([-1, 1])
        self.speedX = self.SPEED
        self.speedY = self.SPEED * choice([-1, 1, 0])
        self.display_surface_rect = pygame.display.get_surface().get_rect(topleft=(0, 0))
        self.lower_bound = offset_x
        self.upper_bound = self.display_surface_rect.right - offset_x
        self.isout = True #initially set ball at rest

    def update(self) -> None:
        pygame.draw.circle(self.image, self.color, self.CENTER, self.RADIUS)
        if self.isout:
            return True

        if self.rect.left < self.lower_bound or self.rect.right > self.upper_bound:
            self.set_out_attr(True)
            self.reset()

        self.rect.x += (self.speedX * self.direction_x)
        self.rect.y += (self.speedY)

        if self.rect.bottom > self.display_surface_rect.bottom  or self.rect.top < 0:
            self.speedY *= -1

    def collision_reaction(self, sprite: pygame.sprite.Sprite):
        center_diff = sprite.rect.centery - self.rect.centery #hitter.centery - ball.centery
        self.speedY += (center_diff * self.FACTOR)
        self.direction_x *= -1
    
    def set_out_attr(self, is_out: bool):
        self.isout = is_out
    
    def get_out_attr(self):
        return self.isout
    
    def reset(self):
        self.speedY = 0
        self.direction_x = choice([-1, 1])
        self.rect.center = self.display_surface_rect.center