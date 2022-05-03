from collections import deque
from typing import Deque


def oranges_rotting(grid: list[list[int]]) -> int:
    """
    You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.
    Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
    Return the minimum number of minutes that must elapse until no cell has a fresh orange.
    If this is impossible, return -1.
    Idea: use BFS + dynamic programming. Create a matrix with number of minutes necessary to rot"""
    nrows = len(grid)
    ncols = len(grid[0])
    # init matrix
    # -1 -- unvisited
    minutes_to_rot = [[-1 for col in range(ncols)] for row in range(nrows)]
    # list of coordinates of rotten oranges
    rotten_border: Deque[tuple[int, int]] = deque()
    fresh_oranges: set[tuple[int, int]] = set()
    max_minutes = 0
    for row in range(nrows):
        for col in range(ncols):
            if grid[row][col] == 2:
                rotten_border.append((row, col))
                minutes_to_rot[row][col] = 0
            if grid[row][col] == 1:
                fresh_oranges.add((row, col))
    if not fresh_oranges:
        return 0
    # Breadth-First-Search
    # rotten_border -- list of rotten oranges, neighbors of which we should check
    while rotten_border:
        row, col = rotten_border.popleft()
        max_minutes = max(max_minutes, minutes_to_rot[row][col])
        neighbors_candidates = [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]
        neighbors = [(r, c) for (r, c) in neighbors_candidates if \
                     (r >= 0) and (c >= 0) and (r < nrows) and (c < ncols)]
        for neighbor_row, neighbor_col in neighbors:
            # check that it is unvisited
            if minutes_to_rot[neighbor_row][neighbor_col] >= 0:
                continue
            if (neighbor_row, neighbor_col) in fresh_oranges:
                minutes_to_rot[neighbor_row][neighbor_col] = minutes_to_rot[row][col] + 1
                rotten_border.append((neighbor_row, neighbor_col))
                fresh_oranges.remove((neighbor_row, neighbor_col))
    # if there still are fresh oranges, they will never rot
    if fresh_oranges:
        return -1
    return max_minutes


def test_corner_cases():
    assert oranges_rotting([[0]]) == 0
    assert oranges_rotting([[1]]) == -1
    assert oranges_rotting([[2]]) == 0
    assert oranges_rotting([[1, 2]]) == 1


def test_oranges_rotting():
    assert oranges_rotting([[1, 1, 1],
                            [1, 2, 1],
                            [1, 1, 1]]) == 2


def test_oranges_rotting():
    assert oranges_rotting([[2, 1, 0],
                            [1, 0, 1],
                            [0, 1, 2]]) == 1


def test_examples():
    assert oranges_rotting([[2, 1, 1],
                            [1, 1, 0],
                            [0, 1, 1]]) == 4
    assert oranges_rotting([[2, 1, 1],
                            [0, 1, 1],
                            [1, 0, 1]]) == -1
    assert oranges_rotting([[0, 2]]) == 0
