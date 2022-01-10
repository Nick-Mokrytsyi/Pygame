import pygame

import controls
from space_gun import Space_Rocket
from pygame.sprite import Group
from enemy import Enemy
from stats import Stats
from scores import Scores


def start():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("SPACE DEFENDER")
    background_color = (0, 0, 0)
    gun = Space_Rocket(screen)
    bullets = Group()
    enemys = Group()
    controls.create_army(screen, enemys)
    stats = Stats()
    score = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.flag:
            gun.update_gun()
            controls.update(screen, background_color, stats, score, gun, enemys, bullets)
            controls.update_bullets(screen, stats, score, enemys, bullets)
            controls.update_enemys(stats, screen, gun, enemys, bullets)


start()
