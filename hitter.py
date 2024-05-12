import pygame
import math
from ball import Ball

class Hitter(pygame.sprite.Sprite):
    BORDER_RADIUS = 3
    SPEED = 15
    def __init__(self, position: tuple[int, int], size: tuple[int, int], group: pygame.sprite.GroupSingle, color=(0, 255, 0, 255)):
        super().__init__(group)
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect(topleft=position)
        self.color = pygame.Color(color)
        self.border = Hitter.BORDER_RADIUS 
        self.direction_y = 0
        self.display_surface_rect = pygame.display.get_surface().get_rect(topleft=(0, 0))
        self.lower_bound = 0
        self.upper_bound = self.display_surface_rect.height - self.rect.height

    def update(self, ball: Ball):
        pygame.draw.rect(self.image, self.color, (0, 0, *self.rect.size), 0, self.BORDER_RADIUS)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction_y = -1
        elif keys[pygame.K_DOWN]:
            self.direction_y = 1
        else:
            self.direction_y = 0

        self.rect.y += (self.SPEED * self.direction_y)
        
        if self.rect.y > self.upper_bound:
            self.rect.y = self.upper_bound
        elif self.rect.y < 0:
            self.rect.y = self.lower_bound
