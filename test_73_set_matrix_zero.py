def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    nrows = len(matrix)
    ncols = len(matrix[0])
    zero_rows = set()
    zero_cols = set()
    for row in range(nrows):
        for col in range(ncols):
            if matrix[row][col] == 0:
                zero_rows.add(row)
                zero_cols.add(col)
    for row in range(nrows):
        for col in range(ncols):
            if row in zero_rows or col in zero_cols:
                matrix[row][col] = 0
    return


def test_corner_cases():
    matrix = [[0]]
    setZeroes(matrix)
    assert matrix == [[0]]
    matrix = [[1]]
    setZeroes(matrix)
    assert matrix == [[1]]
    matrix = [[0, 1]]
    setZeroes(matrix)
    assert matrix == [[0, 0]]
    matrix = [[0], [1]]
    setZeroes(matrix)
    assert matrix == [[0], [0]]
    matrix = [[0, 1],
              [1, 1]]
    setZeroes(matrix)
    assert matrix == [[0, 0],
                      [0, 1]]


def test_examples():
    matrix = [[0, 1, 2, 0],
              [3, 4, 5, 2],
              [1, 3, 1, 5]]
    setZeroes(matrix)
    assert matrix == [[0, 0, 0, 0],
                      [0, 4, 5, 0],
                      [0, 3, 1, 0]]
    matrix = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]
    setZeroes(matrix)
    assert matrix == [[1, 0, 1],
                      [0, 0, 0],
                      [1, 0, 1]]


def test_wa1():
    matrix = [[8, 3, 6, 9, 7, 8, 0, 6],
              [0, 3, 7, 0, 0, 4, 3, 8],
              [5, 3, 6, 7, 1, 6, 2, 6],
              [8, 7, 2, 5, 0, 6, 4, 0],
              [0, 2, 9, 9, 3, 9, 7, 3]]
    setZeroes(matrix)
    assert matrix == [[0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,3,6,0,0,6,0,0],
                      [0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0]]

