import pygame, random
from pygame.locals import *


def on_grid_random():
    global PIXEL_SIZE
    x = random.randint(0, 590)
    y = random.randint(0, 590)
    return x // PIXEL_SIZE * PIXEL_SIZE, y // PIXEL_SIZE * PIXEL_SIZE


def collision(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
PIXEL_SIZE = 20
pygame.init()
tela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

snake = [(200, 200), (200 + PIXEL_SIZE, 200), (200 + PIXEL_SIZE * 2, 200)]
snake_skin = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
snake_skin.fill((0, 255, 0))

apple_pos = on_grid_random()
apple = pygame.Surface((PIXEL_SIZE, PIXEL_SIZE))
apple.fill((255, 0, 0))
direction = LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                direction = UP
            if event.key == K_DOWN:
                direction = DOWN
            if event.key == K_LEFT:
                direction = LEFT
            if event.key == K_RIGHT:
                direction = RIGHT

    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0, 0))

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1][0], snake[i - 1][1]

    if direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - PIXEL_SIZE)
    if direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + PIXEL_SIZE)
    if direction == RIGHT:
        snake[0] = (snake[0][0] + PIXEL_SIZE, snake[0][1])
    if direction == LEFT:
        snake[0] = (snake[0][0] - PIXEL_SIZE, snake[0][1])

    tela.fill((0, 0, 0))
    tela.blit(apple, apple_pos)
    for pos in snake:
        tela.blit(snake_skin, pos)

    pygame.display.update()
