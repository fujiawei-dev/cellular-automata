'''The Langton Ant'''

import sys

import numpy as np
import pygame
from pygame.locals import *


def evolution(M, x, y, f):
    if M[y, x] == 1:
        M[y, x] = 0
        if f == '↑':
            f = '←'
            x -= 1
        elif f == '←':
            f = '↓'
            y += 1
        elif f == '↓':
            f = '→'
            x += 1
        elif f == '→':
            f = '↑'
            y -= 1
    elif M[y, x] == 0:
        M[y, x] = 1
        if f == '↑':
            f = '→'
            x += 1
        elif f == '→':
            f = '↓'
            y += 1
        elif f == '↓':
            f = '←'
            x -= 1
        elif f == '←':
            f = '↑'
            y -= 1
    return M, x, y, f


def main(display_size=900, square_size=5, rand=8000):
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((display_size, display_size), 0, 32)
    pygame.display.set_caption('The Langton Ant')

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    DISPLAYSURF.fill(WHITE)

    length = display_size//square_size + 2
    M = np.zeros((length, length), dtype=np.int)

    x, y = length//2, length//2
    f = '↓'

    step = 0
    while step < 12000:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        w, h = M.shape
        for i in range(1, w):
            for j in range(1, h):
                if M[i, j] == 1:
                    pygame.draw.rect(DISPLAYSURF, BLACK,
                                     ((i-1)*square_size, (j-1)*square_size, square_size, square_size))
                else:
                    pygame.draw.rect(DISPLAYSURF, WHITE,
                                     ((i-1)*square_size, (j-1)*square_size, square_size, square_size))

        M, x, y, f = evolution(M, x, y, f)
        pygame.PixelArray(DISPLAYSURF)
        pygame.display.update()

        step += 1
        print(step)
        pygame.image.save(DISPLAYSURF, 'langton/{}.png'.format(step))


if __name__ == '__main__':
    main()
