import numpy as np

import grid


def test_HandleMouse():
    scale = 1
    w, h = 10, 10

    g = grid.Grid(w, h, scale, 0)
    g.grid_array.fill(0)

    x, y = 5, 5
    g.HandleMouse(x, y)

    assert g.grid_array[x][y] == 1


def test_NumColsRows():
    scale = 2
    w, h = 20, 10

    g = grid.Grid(w, h, scale, 0)

    assert g.columns == 5
    assert g.rows == 10


def test_evolve_empty():
    scale = 1
    w, h = 10, 10

    g = grid.Grid(w, h, scale, 0)
    g.grid_array.fill(0)

    next = np.ndarray(shape=(g.size))
    g.evolve(next)

    # No evolution from empty grid
    assert np.array_equal(next, g.grid_array)


def test_underpopulation_one_cell():
    scale = 1
    w, h = 10, 10

    g = grid.Grid(w, h, scale, 0)
    g.grid_array.fill(0)

    g.grid_array[5][5] = 1

    next = np.ndarray(shape=(g.size))
    g.evolve(next)

    # No neighbours for single cell
    assert g.get_neighbours(5, 5) == 0

    # Underpopulation: Single cell dies
    assert g.grid_array[5][5] == 0


def test_overpopulation_one_cell():
    scale = 1
    w, h = 10, 10

    g = grid.Grid(w, h, scale, 0)
    g.grid_array.fill(0)

    g.grid_array[5][5] = 1

    # Neighbours
    nn = [(4, 5), (6, 5), (5, 4), (5, 6)]
    for n in nn:
        x, y = n
        g.grid_array[x][y] = 1

    assert g.get_neighbours(5, 5) == 4

    next = np.ndarray(shape=(g.size))
    g.evolve(next)

    # Overpopulation: Single cell dies
    assert g.grid_array[5][5] == 0


def test_reproduction_one_cell():
    scale = 1
    w, h = 10, 10

    g = grid.Grid(w, h, scale, 0)
    g.grid_array.fill(0)
    g.grid_array[5][5] = 0

    # Neighbours
    nn = [(4, 5), (6, 5), (5, 4)]
    for n in nn:
        x, y = n
        g.grid_array[x][y] = 1

    assert g.get_neighbours(5, 5) == 3

    next = np.ndarray(shape=(g.size))
    g.evolve(next)

    # Reproduction: Dead cell becomes live cell
    assert g.grid_array[5][5] == 1
