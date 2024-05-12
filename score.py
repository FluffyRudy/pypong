import pygame
from ball import Ball

class Score: 
    def __init__(self, initial_score: int, disply_surface: pygame.Surface, based_sprite: Ball, font_color: pygame.Color):
        self.font = pygame.font.SysFont(None, 50, True, True)
        self.disply_surface: pygame.Surface = disply_surface
        self.display_surface_rect: pygame.Rect = self.disply_surface.get_rect(topleft=(0, 0))
        self.sprite_obj = based_sprite
        self.text = 0
        self.count = initial_score #score count
        self.color = font_color

    def update(self):
        if self.sprite_obj.out_boundry_right():
            self.increase_score()
        elif self.sprite_obj.out_boundry_left():
            self.decrease_score()

    def increase_score(self):
        self.count += 1
    
    def decrease_score(self):
        self.count -= 1

    def draw(self):
        font_surface = self.font.render(f"{self.count}", True, self.color)
        position_x = (self.display_surface_rect.centerx - font_surface.get_width() // 2)
        self.disply_surface.blit(font_surface, (position_x, font_surface.get_height()))