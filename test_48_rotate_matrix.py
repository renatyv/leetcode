def rotate(matrix: list[list[int]]) -> None:
    """You are given an n x n 2D matrix representing an image,
    rotate the image by 90 degrees (clockwise).
    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
    DO NOT allocate another 2D matrix and do the rotation."""
    for r in range(len(matrix) // 2):
        for c in range(r, len(matrix) - r - 1):
            tmp = matrix[r][c]
            matrix[r][c] = matrix[-c - 1][r]
            matrix[-c - 1][r] = matrix[-r - 1][-c - 1]
            matrix[-r - 1][-c - 1] = matrix[c][-r - 1]
            matrix[c][-r - 1] = tmp


def test_edge_cases():
    matrix = [[0]]
    rotate(matrix)
    assert matrix == [[0]]
    matrix = [[0, 1],
              [2, 3]]
    rotate(matrix)
    assert matrix == [[2, 0],
                      [3, 1]]


def test_examples():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    rotate(matrix)
    assert matrix == [[7, 4, 1],
                      [8, 5, 2],
                      [9, 6, 3]]
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix)
    assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
