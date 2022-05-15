def uniquePaths(nrows: int, ncols: int) -> int:
    """There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]).
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
    The robot can only move either down or right at any point in time.
    Given the two integers m and n,
    return the number of possible unique paths that the robot can take to reach the bottom-right corner.

    Idea: 2D dynamic programming."""
    prev_row = [1] * ncols
    # compute nex row
    for row_n in range(1, nrows):
        next_row = [1] * ncols
        for col_n in range(1, ncols):
            next_row[col_n] = prev_row[col_n] + next_row[col_n - 1]
        prev_row = next_row
    return prev_row[-1]


def test_cases():
    assert uniquePaths(1, 1) == 1
    assert uniquePaths(2, 1) == 1
    assert uniquePaths(100, 1) == 1
    assert uniquePaths(1, 100) == 1


def test_examples():
    assert uniquePaths(3, 2) == 3
    assert uniquePaths(3, 7) == 28
