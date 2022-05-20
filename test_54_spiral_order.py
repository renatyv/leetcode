def spiralOrder(matrix: list[list[int]]) -> list[int]:
    """Given an m x n matrix, return all elements of the matrix in spiral order.
    -100 <= matrix[i][j] <= 100
    Idea: mark visited cells with 101"""
    spiral_order = []
    nrows = len(matrix)
    ncols = len(matrix[0])
    row = 0
    col = -1
    VISITED = 101
    while col + 1 != ncols and matrix[row][col + 1] != VISITED:
        while col + 1 < ncols and matrix[row][col + 1] != VISITED:
            col += 1
            spiral_order.append(matrix[row][col])
            matrix[row][col] = VISITED
        while row + 1 < nrows and matrix[row + 1][col] != VISITED:
            row += 1
            spiral_order.append(matrix[row][col])
            matrix[row][col] = VISITED
        while col - 1 >= 0 and matrix[row][col - 1] != VISITED:
            col -= 1
            spiral_order.append(matrix[row][col])
            matrix[row][col] = VISITED
        while row - 1 >= 0 and matrix[row - 1][col] != VISITED:
            row -= 1
            spiral_order.append(matrix[row][col])
            matrix[row][col] = VISITED
    return spiral_order


def test_corner():
    assert spiralOrder([[1]]) == [1]
    assert spiralOrder([[1, 2, 3]]) == [1, 2, 3]
    assert spiralOrder([[1], [2], [3]]) == [1, 2, 3]
    assert spiralOrder([[1, 2],
                        [4, 3]]) == [1, 2, 3, 4]
    assert spiralOrder([[1, 2],
                        [6, 3],
                        [5, 4]]) == [1, 2, 3, 4, 5, 6]
    assert spiralOrder([[1, 2, 3],
                        [6, 5, 4]]) == [1, 2, 3, 4, 5, 6]


def test_wa1():
    assert spiralOrder([[1, 2, 3, 4],
                        [5, 6, 7, 8],
                        [9, 10, 11, 12],
                        [13, 14, 15, 16]]) == [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]


def test_examples():
    assert spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
