import pygame
from ball import Ball

class Score: 
    def __init__(self, initial_score: int, disply_surface: pygame.Surface, based_sprite: Ball, font_color: pygame.Color):
        self.font = pygame.font.SysFont(None, 50, True, True)
        self.disply_surface: pygame.Surface = disply_surface
        self.display_surface_rect: pygame.Rect = self.disply_surface.get_rect(topleft=(0, 0))
        self.sprite_obj = based_sprite
        self.text = 0
        self.player_count = initial_score
        self.ai_count = initial_score
        self.color = font_color

    def update(self):
        if self.sprite_obj.out_boundry_right():
            self.increase_player_score()
        elif self.sprite_obj.out_boundry_left():
            self.increase_ai_score()

    def increase_player_score(self):
        self.player_count += 1
    
    def increase_ai_score(self):
        self.ai_count += 1

    def draw(self):
        score_surface = self.font.render(f"{self.player_count} - {self.ai_count}", True, self.color)
        position_x_player = (self.display_surface_rect.centerx - score_surface.get_width() // 2)
        self.disply_surface.blit(score_surface, (position_x_player, score_surface.get_height()))