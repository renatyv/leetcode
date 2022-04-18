import collections


def floodFill(image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
    # pixes on the border of the flood
    # test if color is outstide image
    visited = set()
    nrows = len(image)
    ncols = len(image[0])
    border = collections.deque()
    border.append((sr, sc))
    starting_color = image[sr][sc]
    while border:
        row, col = border.pop()
        image[row][col] = newColor
        visited.add((row, col))
        candidate_neighbors = [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]
        for r, c in candidate_neighbors:
            if (r >= 0) and (c >= 0) and (r < nrows) and (c < ncols):
                if image[r][c] == starting_color and (r,c) not in visited:
                    border.append((r, c))
    return image


def test_floodFill_single():
    image = [[1]]
    sr = 0
    sc = 0
    newColor = 2
    assert floodFill(image, sr, sc, newColor) == [[2]]


def test_floodFill_example_1():
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    newColor = 2
    assert floodFill(image, sr, sc, newColor) == [[2,2,2],[2,2,0],[2,0,1]]


def test_floodFill_example_2():
    image = [[0,0,0],[0,0,0]]
    sr = 0
    sc = 0
    newColor = 2
    assert floodFill(image, sr, sc, newColor) == [[2,2,2],[2,2,2]]


def test_floodFill_example_3():
    image = [[0,0,0],[0,1,1]]
    sr = 1
    sc = 1
    newColor = 2
    assert floodFill(image, sr, sc, newColor) == [[0,0,0],[0,2,2]]
