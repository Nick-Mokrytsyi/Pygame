import pygame
import sys

from bullet import Bullet
from enemy import Enemy


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


def update(screen, background_color, gun, enemys,  bullets):
    """Update the display of game"""
    screen.fill(background_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.show()
    enemys.draw(screen)
    pygame.display.flip()


def update_bullets(bullets):
    """Update the coordinates of bullets and delete them from the list"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_enemys(enemy):
    enemy.update()

def create_army(screen, enemys):
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((700 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((800 - 100 - 2 * enemy_height) / enemy_height)
    for row_number in range(number_enemy_y - 2):
        for enemy_number in range(number_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + (enemy_number * enemy_width)
            enemy.y = enemy_height + (row_number * enemy_height)
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + (enemy.rect.height * row_number)
            enemys.add(enemy)


