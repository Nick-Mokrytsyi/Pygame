import pygame

import controls
from space_gun import Space_Rocket
from pygame.sprite import Group


def start():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("SPACE DEFENDER")
    background_color = (0, 0, 0)
    gun = Space_Rocket(screen)
    bullets = Group()

    while True:
        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update(screen, background_color, gun, bullets)
        controls.update_bullets(bullets)


start()
