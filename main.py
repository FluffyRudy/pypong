import pygame
import sys
from player import Player
from enemy import Enemy
from ball import Ball
from score import Score

class Game:
    HITTER_SIZE = (10, 200)
    HITTER_OFFSET = 20
    WHITE = pygame.Color(255, 255, 255, 255)
    def __init__(self):
        self.bg_color = pygame.Color(50, 50, 50, 150)
        self.width = 1000
        self.height = 900
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen_rect = self.screen.get_rect(topleft=(0, 0))

        self.player = pygame.sprite.GroupSingle()
        self.player_hitter = Player( (self.HITTER_OFFSET, 0), self.HITTER_SIZE, self.player )

        self.enemy = pygame.sprite.GroupSingle()
        self.enemy_hitter = Enemy((self.screen_rect.width-self.HITTER_SIZE[0]-self.HITTER_OFFSET, 0), self.HITTER_SIZE, self.enemy, (0, 255, 0, 255))

        self.ball = pygame.sprite.GroupSingle(Ball(self.screen_rect.center, offset_x=self.HITTER_OFFSET))
        
        self.score_count = 0
        self.score = Score(self.score_count, self.screen, self.ball.sprite, self.WHITE)

        self.clock = pygame.time.Clock()


    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                ball_sprite = self.ball.sprite
                if ball_sprite.get_rest(): #if ball is at rest start movement
                    ball_sprite.set_rest(False)

    def run(self):
        while True:
            self.handle_event()
            self.screen.fill(self.bg_color)
            
            self.player.update(self.ball.sprite)
            self.enemy.update(self.ball.sprite)
            self.score.update()
            self.ball.update()

            self.score.draw()
            self.player.draw(self.screen)
            self.enemy.draw(self.screen) 
            self.ball.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(60)

def main():
    pygame.init()
    pygame.font.init()
    game = Game()
    game.run()

if __name__ == "__main__":
    main()