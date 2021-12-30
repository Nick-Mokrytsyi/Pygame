import pygame
import sys

from bullet import Bullet


def events(screen, gun, bullets):
    """Event handling"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Right bottom
            if event.key == pygame.K_RIGHT:
                gun.move_right = True
            # Left bottom
            elif event.key == pygame.K_LEFT:
                gun.move_left = True
            # Space bottom = gun Fire
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # Right bottom
            if event.key == pygame.K_RIGHT:
                gun.move_right = False
            # Left bottom
            elif event.key == pygame.K_LEFT:
                gun.move_left = False



def update(screen, background_color, gun, bullets):
    """Update the display of game"""
    screen.fill(background_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.show()
    pygame.display.flip()

def update_bullets(bullets):
    """Update the coordinates of bullets and delete them from the list"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)