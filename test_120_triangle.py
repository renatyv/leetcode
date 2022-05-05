def minimumTotal(triangle: list[list[int]]) -> int:
    """Given a triangle array, return the minimum path sum from top to bottom.
    For each step, you may move to an adjacent number of the row below.
    More formally, if you are on index i on the current row,
    you may move to either index i or index i + 1 on the next row.

    Idea: dynamic programming
    Use solution for previous row: minimal sum to get to element at index [i]
    """
    prev_row_min_sum = triangle[0]
    # starting from second row
    for row_n, row in enumerate(triangle[1:]):
        cur_row_min_sum = [-1] * len(row)
        cur_row_min_sum[0] = row[0] + prev_row_min_sum[0]
        for col_n in range(1, len(row) - 1):
            cur_row_min_sum[col_n] = min(prev_row_min_sum[col_n], prev_row_min_sum[col_n - 1]) \
                                     + row[col_n]
        cur_row_min_sum[-1] = row[-1] + prev_row_min_sum[-1]
        prev_row_min_sum = cur_row_min_sum
    return min(prev_row_min_sum)


def test_example():
    assert minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]) == 11
    assert minimumTotal([[-10]]) == -10


def test_corner():
    assert minimumTotal([[1], [2, 1], [3, 2, 1]]) == 3
    assert minimumTotal([[1], [1, 2], [1, 2, 3]]) == 3
    assert minimumTotal([[1], [2, 1], [2, 1, 3]]) == 3
