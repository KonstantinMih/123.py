import pygame
from pygame.draw import *
from random import randint
pygame.font.init()

FPS = 60
screen = pygame.display.set_mode((1200, 900))

score = 0
balls = []

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def new_balls():
    '''генерирует новые шарики '''
    if len(balls) < 4:
        x = randint(100, 700)
        y = randint(100, 500)
        r = randint(50, 70)
        color = COLORS[randint(0, 5)]
        speed_x = randint(-15, 15)
        speed_y = randint(-15, 15)
        balls.append([color, (x, y), r, speed_x, speed_y])

def draw_balls(screen, balls):
    '''Отрисовывет шар
    screen - экран
    balls - список сгенерированных шаров'''
    for b in balls:
        circle(screen, b[0], b[1], b[2])

def move_balls():
    '''двигает шары'''
    for b in balls:
        if b[1][1] - b[2] <= 0 or b[1][1] + b[2] >= 900:
            b[4] = -b[4]
        if b[1][0] - b[2] <= 0 or b[1][0] + b[2] >= 1200:
            b[3] = -b[3]
        x = b[1][0] + b[3]
        y = b[1][1] + b[4]
        b[1] = (x, y)

def click(event):
    ''' засекает, попали ли кликом в шарик, и удаляет шар, в который попали кликом, начисляя очки '''
    for b in balls:
        if ((event.pos[0] - b[1][0])**2 + (event.pos[1] - b[1][1])**2) <= b[2]**2:
            balls.remove(b)
    return 4 - len(balls)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if click(event) != 0:
                score = score + click(event)
                print(score)
    new_balls()
    draw_balls(screen, balls)
    move_balls()
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()