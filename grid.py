import random

import numpy as np
import pygame


class Grid:
    def __init__(self, width, height, scale, offset):
        self.scale = scale

        self.columns = int(height / scale)
        self.rows = int(width / scale)

        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset

    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = random.randint(0, 1)

    def evolve(self):
        next_state = np.ndarray(shape=(self.size))
        for x in range(self.rows):
            for y in range(self.columns):
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours(x, y)
                if state == 0 and neighbours == 3:
                    next_state[x][y] = 1
                elif state == 1 and (neighbours < 2 or neighbours > 3):
                    next_state[x][y] = 0
                else:
                    next_state[x][y] = state
        self.grid_array = next_state

    def Conway(self, off_color, on_color, surface, pause):
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                # random_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                if self.grid_array[x][y] == 1:
                    pygame.draw.rect(
                        surface,
                        on_color,
                        [
                            x_pos,
                            y_pos,
                            self.scale - self.offset,
                            self.scale - self.offset,
                        ],
                    )
                else:
                    pygame.draw.rect(
                        surface,
                        off_color,
                        [
                            x_pos,
                            y_pos,
                            self.scale - self.offset,
                            self.scale - self.offset,
                        ],
                    )

        if pause == False:
            self.evolve()

    def HandleMouse(self, x, y):
        _x = x // self.scale
        _y = y // self.scale

        if self.grid_array[_x][_y] != None:
            self.grid_array[_x][_y] = 1

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x + n + self.rows) % self.rows
                y_edge = (y + m + self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total
