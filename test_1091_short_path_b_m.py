from collections import deque
def shortestPathBinaryMatrix(grid: list[list[int]]) -> int:
    """Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
    If there is no clear path, return -1.
    A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
    to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected
    (i.e., they are different and they share an edge or a corner).
    The length of a clear path is the number of visited cells of this path.
    Idea: BFS """
    nrows: int = len(grid)
    ncols: int = len(grid[0])
    if grid[0][0] == 1:
        return -1
    if grid[0][0] == 0 and nrows == ncols == 1:
        return 1
    MAX_PATH_LEN = 10**6
    min_path_len_to: list[list[int]] = [[MAX_PATH_LEN] * ncols for row in range(nrows)]
    min_path_len_to[0][0] = 1
    border = deque()
    border.append((0, 0))
    while border:
        row, col = border.popleft()
        neighbors_candidates = [(row-1, col), (row-1, col+1), (row-1, col-1),
                                (row+1, col), (row+1, col+1), (row+1, col-1),
                                (row, col+1), (row, col-1)]
        neighbors = [(r,c) for (r,c) in neighbors_candidates
                     if 0 <= r < nrows
                     and 0 <= c < ncols
                     and grid[r][c] == 0]
        for neighbor_r, neghbor_c in neighbors:
            if min_path_len_to[neighbor_r][neghbor_c] == MAX_PATH_LEN:
                min_path_len_to[neighbor_r][neghbor_c] = min_path_len_to[row][col] + 1
                if (neighbor_r, neghbor_c) == (nrows - 1, ncols - 1):
                    return min_path_len_to[neighbor_r][neghbor_c]
                border.append((neighbor_r, neghbor_c))
    return -1


def test_corner():
    assert shortestPathBinaryMatrix([[0]]) == 1
    assert shortestPathBinaryMatrix([[1]]) == -1
    assert shortestPathBinaryMatrix([[0,0,0],
                                     [0,1,1],
                                     [0,1,0]]) == -1


def test_examples():
    assert shortestPathBinaryMatrix([[0,1],[1,0]]) == 2
    assert shortestPathBinaryMatrix([[0,0,0],
                                     [1,1,0],
                                     [1,1,0]]) == 4
    assert shortestPathBinaryMatrix([[1,0,0],
                                     [1,1,0],
                                     [1,1,0]]) == -1
    assert shortestPathBinaryMatrix([[0, 0, 0],
                                     [0, 0, 0],
                                     [0, 0, 0]]) == 3
