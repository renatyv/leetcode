import collections
import numpy as np

def numIslands(grid: list[list[str]]) -> int:
    """Idea: Greedy depth-first-search. If we found ground, discover it fully first. Then continue to discover water.
    For that keep track of discovered water separately."""
    def get_neighbors(row, col, nrows, ncols):
        candidate_neighbors = [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]
        return [(r, c) for (r, c) in candidate_neighbors if (r >= 0) and (c >= 0) and (r < nrows) and (c < ncols)]

    def DFS_ground_mark(row, col, island_number_grid, island_number, new_water_border):
        ground_border = {(row, col)}
        while ground_border:
            row, col = ground_border.pop()
            # mark visited
            island_number_grid[row][col] = island_number
            for (r, c) in get_neighbors(row, col, nrows, ncols):
                # if not visited yet
                if island_number_grid[r][c] == -1:
                    if grid[r][c] == '0':
                        new_water_border.add((r, c))
                    else:
                        ground_border.add((r, c))
        return

    nrows = len(grid)
    ncols = len(grid[0])
    island_count = 0
    # -1 not visited (neighbors are not added), 0 water, 1 first island, 2 second island, etc..
    island_number_grid = [[-1 for col in range(ncols)] for row in range(nrows)]
    # contains tuples of unvisited (row, column).
    water_border: set[tuple[int, int]] = set()
    # came to 0,0 from blue water, no islands yet
    sr = 0
    sc = 0
    if grid[sr][sc] == '0':
        water_border.add((sr, sc))
        island_number_grid[sr][sc] = 0
    else:  # first island discovered
        island_count = 1
        island_number_grid[sr][sc] = 1
        DFS_ground_mark(sr, sc, island_number_grid, island_number=1, new_water_border=water_border)
    while water_border:
        row, col = water_border.pop()
        island_number_grid[row][col] = 0
        neighbors = get_neighbors(row, col, nrows, ncols)
        for (r, c) in neighbors:
            if island_number_grid[r][c] == -1:
                if grid[r][c] == '0':
                    water_border.add((r, c))
                else:
                    # new island found,
                    island_count += 1
                    # now let's discover it completely
                    DFS_ground_mark(r, c, island_number_grid, island_count, water_border)
    return island_count


def test_cheatah():
    grid = [
        ["1", "1", "1", "1", "1"],
        ["1", "0", "1", "0", "1"],
        ["1", "1", "0", "1", "1"],
        ["1", "0", "1", "0", "1"],
        ["1", "1", "1", "1", "1"]
    ]
    assert numIslands(grid) == 1


def test_cheatah_2():
    grid = [
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "0", "1", "0", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1"]
    ]
    assert numIslands(grid) == 2


def test_numIslands_empty_grid():
    assert numIslands([['0']]) == 0
    grid = [
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert numIslands(grid) == 0


def test_single_island():
    # assert numIslands([['1']]) == 1
    grid = [
        ["0", "0", "0"],
        ["0", "1", "0"],
        ["0", "0", "0"]
    ]
    assert numIslands(grid) == 1
    grid = [
        ["0", "0", "0", "0", "0"],
        ["0", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert numIslands(grid) == 1
    grid = [
        ["1", "0", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "1", "0", "0", "0"],
        ["0", "1", "1", "1", "1"]
    ]
    assert numIslands(grid) == 1
    grid = [
        ["1", "1", "1", "1", "1"],
        ["1", "1", "0", "1", "1"],
        ["1", "1", "0", "1", "1"],
        ["1", "1", "1", "1", "1"]
    ]
    assert numIslands(grid) == 1
    grid = [
        ["0", "0", "0", "0", "0"],
        ["0", "1", "1", "1", "0"],
        ["0", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert numIslands(grid) == 1


def test_two_islands():
    assert numIslands([['1', '0', '1']]) == 2
    grid = [
        ["0", "0", "0", "0", "0"],
        ["0", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert numIslands(grid) == 2
    grid = [
        ["1", "0", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
        ["0", "1", "1", "1", "1"]
    ]
    assert numIslands(grid) == 2
    grid = [
        ["1", "1", "0", "1", "1"],
        ["1", "1", "0", "1", "1"],
        ["1", "1", "0", "1", "1"],
        ["1", "1", "0", "1", "1"]
    ]
    assert numIslands(grid) == 2
    grid = [
        ["1", "0", "0", "0", "0"],
        ["1", "0", "1", "1", "0"],
        ["0", "0", "1", "1", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert numIslands(grid) == 2
    grid = [
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "0", "1", "0", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1"]
    ]
    assert numIslands(grid) == 2
    grid = [
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "1"],
        ["1", "1", "1", "0", "1"],
        ["1", "0", "0", "0", "0"],
        ["1", "1", "1", "0", "1"]
    ]
    assert numIslands(grid) == 2


def test_three_islands():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert numIslands(grid) == 3
    grid = [
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "0", "0"],
        ["1", "0", "1", "0", "1"],
        ["1", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "1"]
    ]
    assert numIslands(grid) == 3


def test_qorkie():
    grid = [["1", "0", "0", "1", "1", "1", "0", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["1", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "0", "1", "0"],
            ["0", "0", "0", "1", "1", "1", "1", "0", "1", "0", "1", "1", "0", "0", "0", "0", "1", "0", "1", "0"],
            ["0", "0", "0", "1", "1", "0", "0", "1", "0", "0", "0", "1", "1", "1", "0", "0", "1", "0", "0", "1"],
            ["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
            ["1", "0", "0", "0", "0", "1", "0", "1", "0", "1", "1", "0", "0", "0", "0", "0", "0", "1", "0", "1"],
            ["0", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1"],
            ["0", "0", "0", "1", "0", "1", "0", "0", "1", "1", "0", "1", "0", "1", "1", "0", "1", "1", "1", "0"],
            ["0", "0", "0", "0", "1", "0", "0", "1", "1", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "1"],
            ["0", "0", "1", "0", "0", "1", "0", "0", "0", "0", "0", "1", "0", "0", "1", "0", "0", "0", "1", "0"],
            ["1", "0", "0", "1", "0", "0", "0", "0", "0", "0", "0", "1", "0", "0", "1", "0", "1", "0", "1", "0"],
            ["0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "1", "0", "1", "1", "1", "0", "1", "1", "0", "0"],
            ["1", "1", "0", "1", "0", "0", "0", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "1"],
            ["0", "1", "0", "0", "1", "1", "1", "0", "0", "0", "1", "1", "1", "1", "1", "0", "1", "0", "0", "0"],
            ["0", "0", "1", "1", "1", "0", "0", "0", "1", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0"],
            ["1", "0", "0", "1", "0", "1", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "1", "1"],
            ["1", "0", "1", "0", "0", "0", "0", "0", "0", "1", "0", "0", "0", "1", "0", "1", "0", "0", "0", "0"],
            ["0", "1", "1", "0", "0", "0", "1", "1", "1", "0", "1", "0", "1", "0", "1", "1", "1", "1", "0", "0"],
            ["0", "1", "0", "0", "0", "0", "1", "1", "0", "0", "1", "0", "1", "0", "0", "1", "0", "0", "1", "1"],
            ["0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "0", "1", "0", "0", "0", "1", "1", "0", "0", "0"]]
    assert numIslands(grid) == 58
