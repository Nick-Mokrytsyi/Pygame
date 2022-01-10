import pygame.font
from space_gun import Space_Rocket
from pygame.sprite import Sprite, Group


class Scores():
    def __init__(self, screen, stats):
        self.guns_life_rect = None
        self.guns_life_image = None
        self.guns = None
        self.high_score_rect = None
        self.high_score_image = None
        self.score_rect = None
        self.score_image = None
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (139, 195, 74)
        self.back_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_life()

    def image_score(self):
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color, self.back_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, self.back_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 40
        self.high_score_rect.top = 20

    def image_life(self):
        self.guns_life_image = self.font.render(str(self.stats.guns_left), True, self.text_color, self.back_color)
        self.guns_life_rect = self.guns_life_image.get_rect()
        self.guns_life_rect.centerx = self.screen_rect.centerx
        self.guns_life_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.guns_life_image, self.guns_life_rect)
