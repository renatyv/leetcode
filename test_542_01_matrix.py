from collections import deque
from typing import Deque


def updateMatrix(mat: list[list[int]]) -> list[list[int]]:
    """Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
    The distance between two adjacent cells is 1.

    Idea: BFS + dynamic programming.
    Visit all elements with distance 0, then all with distance 1, ...
    Use FIFO for that"""
    nrows = len(mat)
    ncols = len(mat[0])
    MAX_DISTANCE = 10**5
    distance_to_zero: list[list[int]] = [[MAX_DISTANCE for col in range(ncols)] for row in range(nrows)]
    coordinates = tuple[int, int]
    next_nodes: Deque[coordinates] = deque()
    # add all zeros
    for row_n, row in enumerate(mat):
        for col_n, mat_rc in enumerate(row):
            if mat_rc == 0:
                distance_to_zero[row_n][col_n] = 0
                next_nodes.append((row_n, col_n))
    # bfs. Visit all elements with distance 0, then all with distance 1, ...
    while next_nodes:
        row_n, col_n = next_nodes.popleft()
        cur_node_distance: int = distance_to_zero[row_n][col_n]
        neighbor_candidates = [(row_n+1, col_n), (row_n-1, col_n), (row_n, col_n+1), (row_n, col_n-1)]
        neighbors = [(r, c) for r, c in neighbor_candidates if (r >= 0) and (c >= 0) and (r < nrows) and (c < ncols)]
        for neighbor_r, neighbor_c in neighbors:
            # skip visited on previous step (probably less distance)
            if distance_to_zero[neighbor_r][neighbor_c] != MAX_DISTANCE:
                continue
            distance_to_zero[neighbor_r][neighbor_c] = cur_node_distance + 1
            next_nodes.append((neighbor_r, neighbor_c))
    return distance_to_zero


def mats_are_equal(mat1: list[list[int]], mat2: list[list[int]]) -> bool:
    if len(mat1) != len(mat2):
        return False
    if len(mat1[0]) != len(mat2[0]):
        return False
    return all(row_mat1 == row_mat2 for row_mat1, row_mat2 in zip(mat1, mat2))


def test_equal_mats():
    assert mats_are_equal([[0]],
                          [[0]])
    assert not mats_are_equal([[0, 1]],
                              [[0, 2]])
    assert mats_are_equal([[0], [1]],
                          [[0], [1]])


def test_updateMatrix_corner_1():
    assert mats_are_equal(updateMatrix([[0, 1, 1]]),
                          [[0, 1, 2]])
    assert mats_are_equal(updateMatrix([[1, 1, 1],
                                        [1, 0, 1],
                                        [1, 1, 1]]),
                          [[2, 1, 2],
                           [1, 0, 1],
                           [2, 1, 2]])
    assert mats_are_equal(updateMatrix([[0, 1, 0],
                                        [1, 0, 1],
                                        [1, 1, 0]]),
                          [[0, 1, 0],
                           [1, 0, 1],
                           [2, 1, 0]])
    assert mats_are_equal(updateMatrix([[0, 1, 0],
                                        [1, 1, 1]]),
                          [[0, 1, 0],
                           [1, 2, 1]])


def test_updateMatrix_corner_2():
    assert mats_are_equal(updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
                          [[0, 0, 0], [0, 1, 0], [0, 0, 0]])


def test_updateMatrix_example():
    assert mats_are_equal(updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]),
                          [[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    assert mats_are_equal(updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]),
                          [[0,0,0],[0,1,0],[1,2,1]])
