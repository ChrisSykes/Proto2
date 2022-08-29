import pygame
from pygame.locals import *
pygame.init()

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

ship_surface = pygame.image.load('./graphics/ship.png').convert_alpha()




clock = pygame.time.Clock() 
FPS = 120 

isRunning = True

while isRunning:

    delta_time = clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    pygame.Surface.blit(ship_surface, (WINDOW_WIDTH - 100, WINDOW_HEIGHT / 2))

    display_surface.fill('Black')

    pygame.display.update()
      
