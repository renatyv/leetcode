def maxAreaOfIsland(grid: list[list[int]]) -> int:
    """You are given an m x n binary matrix grid.
    An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical).
    You may assume all four edges of the grid are surrounded by water.
    The area of an island is the number of cells with a value 1 in the island.
    Return the maximum area of an island in grid. If there is no island, return 0.

    Solution Idea: Run deep-first-search (DFS) to compute the land area.
    Then continue discovering water using another DFS.
    """
    grid_height = len(grid)
    grid_width = len(grid[0])
    if grid_width == 1 and grid_height == 1:
        return grid[0][0]

    def get_island_area(grid: list[list[int]],
                        visited_grid_cells: list[list[bool]],
                        start_row: int,
                        start_col: int,
                        unvisited_water: set[tuple[int, int]]) -> int:
        """Goes over the whole land, computing the area.
        Side effect: modifies unvisited water
        Side effect: modifies visited grid cells
        :returns area of the land"""
        grid_height = len(grid)
        grid_width = len(grid[0])
        if grid[start_row][start_col] == 0:
            raise Exception("start position must be ground")
        if visited_grid_cells[start_row][start_col]:
            raise Exception("start position must not be visited")
        ground_border: set[tuple[int,int]] = {(start_row, start_col)}
        island_area = 0
        while ground_border:
            row, col = ground_border.pop()
            island_area += 1
            visited_grid_cells[row][col] = True
            # add all ground neighbors
            for neighbor_row, neighbor_col in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
                if neighbor_row < 0 or neighbor_row >= grid_height \
                        or neighbor_col < 0 or neighbor_col >= grid_width\
                        or visited_grid_cells[neighbor_row][neighbor_col]:
                    continue
                if grid[neighbor_row][neighbor_col] == 1:
                    ground_border.add((neighbor_row, neighbor_col))
                else:
                    unvisited_water.add((neighbor_row, neighbor_col))
        return island_area
    visited_grid_cells = [[False for column in range(grid_width)] for row in range(grid_height)]
    unvisited_water: set[tuple[int, int]] = set()
    max_area = 0
    if grid[0][0] == 1:
        cur_area = get_island_area(grid, visited_grid_cells, 0, 0, unvisited_water)
        max_area = max(max_area, cur_area)
    else:
        unvisited_water.add((0, 0))
    while unvisited_water:
        row, col = unvisited_water.pop()
        visited_grid_cells[row][col] = True
        for neighbor_row, neighbor_col in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if neighbor_row < 0 or neighbor_row >= grid_height \
                    or neighbor_col < 0 or neighbor_col >= grid_width \
                    or visited_grid_cells[neighbor_row][neighbor_col]:
                continue
            if grid[neighbor_row][neighbor_col] == 1:
                cur_area = get_island_area(grid, visited_grid_cells, neighbor_row, neighbor_col, unvisited_water)
                max_area = max(cur_area, max_area)
            else:
                unvisited_water.add((neighbor_row, neighbor_col))
    return max_area


def test_corner_cases():
    assert maxAreaOfIsland([[0]]) == 0
    assert maxAreaOfIsland([[1]]) == 1
    assert maxAreaOfIsland([[0, 0, 0, 0], [0, 0, 0, 0]]) == 0
    assert maxAreaOfIsland([[1, 1, 1], [1, 1, 1]]) == 6


def test_example_1():
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    assert maxAreaOfIsland(grid) == 6


def test_example_2():
    grid = [[0,0,0,0,0,0,0,0]]
    assert maxAreaOfIsland(grid) == 0


def test_max_area_of_island_1d():
    gird = [[0,0,1,1,0,0]]
    assert maxAreaOfIsland(gird) == 2
    gird = [[1, 1, 0, 1, 0, 0]]
    assert maxAreaOfIsland(gird) == 2
    gird = [[1, 1, 0, 1, 1, 1]]
    assert maxAreaOfIsland(gird) == 3
    gird = [[0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1]]
    assert maxAreaOfIsland(gird) == 3


def test_max_area_of_island_2d():
    gird = [[0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 1, 1, 0],
            [0, 0, 0, 0]]
    assert maxAreaOfIsland(gird) == 4
    gird = [[1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 0, 1, 1],
            [1, 0, 1, 0, 1],
            [1, 1, 1, 1, 1]]
    assert maxAreaOfIsland(gird) == 5+3+4+3+5