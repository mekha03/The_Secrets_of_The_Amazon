import pygame, sys
from settings import *
from level import Level
from game_data import level_0

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_0, screen)

background = pygame.image.load('../graphics/Background image/a59b735200362f91e6735b2abcb787b2.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))
    level.run()

    pygame.display.update()
    clock.tick(60)