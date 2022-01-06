import pygame


class Enemy(pygame.sprite.Sprite):
    """The Class of one enemy"""

    def __init__(self, screen):
        super(Enemy, self).__init__()
        self.screen = screen
        self.image = pygame.image.load("images/arrival enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """Show the enemy on the display"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """"Move the enemy"""
        self.y = self.y + 0.1
        self.rect.y = self.y
