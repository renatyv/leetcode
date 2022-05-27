from collections import deque
from typing import Callable, Optional, NoReturn


def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    """Idea: BFS. Start from borders and go upwards.
    1) Visit starting from pacific going upwards
    2) Visit starting from atlantic going upwards"""
    row = int
    column = int
    visited_array = int
    do_on_mark_function = Callable[[row, column, visited_array], NoReturn]

    def BFS(initial_nodes: list[tuple[int, int]],
            visited_mark: int,
            visited_array: list[list[int]],
            do_before_marking_visited: Optional[do_on_mark_function] = None):
        nrows = len(visited_array)
        ncols = len(visited_array[0])
        for (r, c) in initial_nodes:
            if do_before_marking_visited:
                do_before_marking_visited(r, c, visited_array[r][c])
            visited_array[r][c] = visited_mark
        dfs_border = deque(initial_nodes)
        while dfs_border:
            row, col = dfs_border.pop()
            neighbor_candidates = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            neighbors = [(r, c) for (r, c) in neighbor_candidates if 0 <= r < nrows and 0 <= c < ncols]
            for neighbor_r, neighbor_c in neighbors:
                if visited_array[neighbor_r][neighbor_c] != visited_mark and \
                        heights[neighbor_r][neighbor_c] >= heights[row][col]:
                    # if raining from both, add to the answer
                    if do_before_marking_visited:
                        do_before_marking_visited(neighbor_r, neighbor_c, visited_array[neighbor_r][neighbor_c])
                    visited_array[neighbor_r][neighbor_c] = visited_mark
                    dfs_border.appendleft((neighbor_r, neighbor_c))

    nrows = len(heights)
    ncols = len(heights[0])
    if nrows == 1:
        return [[0, x] for x in range(ncols)]
    if ncols == 1:
        return [[x, 0] for x in range(nrows)]
    # visited = 0 if not visited,
    # -1 if available from pacific,
    # 1 if available from atlantic
    visited_array = [[0] * ncols for row in range(nrows)]
    pacific_border = [(0, c) for c in range(ncols)] + [(r, 0) for r in range(1, nrows)]
    BFS(initial_nodes=pacific_border, visited_mark=-1, visited_array=visited_array)

    raining_to_both = []

    def on_both_oceans(r: int, c: int, visited_mark: int) -> NoReturn:
        nonlocal raining_to_both
        if visited_mark == -1:
            raining_to_both.append([r, c])

    last_row = [(nrows - 1, c) for c in range(ncols)]
    last_column_except_corner = [(r, ncols - 1) for r in range(0, nrows - 1)]
    atlantic_border = last_column_except_corner + last_row
    BFS(initial_nodes=atlantic_border, visited_mark=1, visited_array=visited_array,
        do_before_marking_visited=on_both_oceans)
    return raining_to_both


def compare_results(list1: list[list[int, int]], list2: list[list[int, int]]) -> bool:
    return {tuple(x) for x in list1} == {tuple(x) for x in list2}


def test_examples():
    result = pacificAtlantic([[1, 2, 2, 3, 5],
                              [3, 2, 3, 4, 4],
                              [2, 4, 5, 3, 1],
                              [6, 7, 1, 4, 5],
                              [5, 1, 1, 2, 4]])
    actual = [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert compare_results(result, actual)
    result = pacificAtlantic([[2, 1],
                              [1, 2]])
    actual = [[0, 0], [0, 1], [1, 0], [1, 1]]
    assert compare_results(actual, result)
