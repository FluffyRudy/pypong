import pygame
from pygame.math import Vector2
from random import choice

class Ball(pygame.sprite.Sprite):
    BALL_SIZE = (20, 20)
    CENTER = (BALL_SIZE[0] // 2, BALL_SIZE[1] // 2)
    RADIUS = (BALL_SIZE[0] + BALL_SIZE[1]) // 4
    SPEED = 8
    FACTOR = 0.1

    def __init__(self, position: tuple[int, int], offset_x: int):
        super().__init__()
        self.image = pygame.Surface(self.BALL_SIZE)
        self.rect = self.image.get_rect(topleft=position)
        self.color = "white"
        self.direction_x = choice([-1, 1])
        self.speedX = self.SPEED
        self.speedY = self.SPEED * choice([-1, 1, 0])
        self.display_surface = pygame.display.get_surface()
        self.display_surface_rect = self.display_surface.get_rect(topleft=(0, 0))
        self.lower_bound = offset_x
        self.upper_bound = self.display_surface_rect.right - offset_x
        self.rest = True #initially set ball at rest

    def update(self) -> None:
        pygame.draw.circle(self.image, self.color, self.CENTER, self.RADIUS)
        if self.rest:
            return None

        if self.out_boundry_left() or self.out_boundry_right():
            self.set_rest(True)
            self.reset()

        self.rect.x += (self.speedX * self.direction_x)
        self.rect.y += (self.speedY)
        
        if self.rect.bottom > self.display_surface_rect.bottom:
            self.speedY *= -1
            self.rect.bottom = self.display_surface_rect.bottom
        elif self.rect.top < self.display_surface_rect.top:
            self.speedY *= -1
            self.rect.top = self.display_surface_rect.top

    def collision_reaction(self, sprite: pygame.sprite.Sprite):
        center_diff =  self.rect.centery - sprite.rect.centery
        self.speedY += (center_diff * self.FACTOR)
        self.direction_x *= -1
    
    def set_rest(self, is_out: bool):
        self.rest = is_out
    
    def get_rest(self):
        return self.rest
    
    def reset(self):
        self.speedY = 0
        self.direction_x = choice([-1, 1])
        self.rect.center = self.display_surface_rect.center
    
    def out_boundry_left(self):
        return self.rect.left < self.lower_bound
    
    def out_boundry_right(self):
        return self.rect.right > self.upper_bound