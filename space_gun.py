import pygame


class Space_Rocket():

    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/Space rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.move_right = False
        self.move_left = False

    def show(self):
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """The update position of space_gun"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.center += 3.5

        if self.move_left and self.rect.left > 0:
            self.center -= 3.5

        self.rect.centerx = self.center