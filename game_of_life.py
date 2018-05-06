import sys
from time import sleep

import numpy as np
import pygame
from pygame.locals import *


def generate(length, rand):
    before = np.zeros((length, length), dtype=np.int)
    for i in range(rand):
        before[np.random.randint(1, length-1),
               np.random.randint(1, length-1)] = 1
    return before


def evolution(before):
    after = np.zeros(before.shape, np.int)
    w, h = before.shape
    for i in range(1, w-1):
        for j in range(1, h-1):
            ij = before[i-1: i+2, j-1: j+2].sum() - before[i, j]
            if ij == 3:
                after[i, j] = 1
            elif ij == 2:
                after[i, j] = before[i, j]
            else:
                after[i, j] = 0
    return after


display_size = 900
life_size = 5

pygame.init()
DISPLAYSURF = pygame.display.set_mode((display_size, display_size), 0, 32)
pygame.display.set_caption('Game of Life')

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF.fill(WHITE)

before = generate(length=display_size//life_size + 2, rand=10000)

n = 1
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    w, h = before.shape
    for i in range(1, w):
        for j in range(1, h):
            if before[i, j] == 1:
                pygame.draw.rect(DISPLAYSURF, BLACK,
                                 ((i-1)*life_size, (j-1)*life_size, life_size, life_size))
            else:
                pygame.draw.rect(DISPLAYSURF, WHITE,
                                 ((i-1)*life_size, (j-1)*life_size, life_size, life_size))

    before = evolution(before)
    pygame.PixelArray(DISPLAYSURF)
    pygame.display.update()
    sleep(0.1)

    pygame.image.save(DISPLAYSURF, 'png/{}.png'.format(n))
    n += 1