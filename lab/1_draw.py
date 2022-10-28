import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

color = (0, 0, 0)
rect(screen, (255, 255, 255), (0, 0, 400, 400))
circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (255, 0, 0), (150, 150), 25)
circle(screen, (255, 0, 0), (250, 150), 25)
line(screen, color, (100, 100), (165, 130), 7)
line(screen, color, (300, 100), (220, 130), 7)
circle(screen, (0, 0, 255), (150, 150), 10)
circle(screen, (0, 0, 255), (250, 150), 10)
rect(screen, color, (100, 250, 200, 25))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
