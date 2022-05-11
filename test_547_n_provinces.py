def findCircleNum(isConnected: list[list[int]]) -> int:
    """
    There are n cities. Some of them are connected, while some are not.
    If city a is connected directly with city b, and city b is connected directly with city c,
    then city a is connected indirectly with city c.
    A province is a group of directly or indirectly connected cities and no other cities outside of the group.
    You are given an n x n matrix isConnected where
    isConnected[i][j] = 1 if the ith city and the jth city are directly connected,
    isConnected[i][j] = 0 otherwise.

    Return the total number of provinces.

    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]

    Idea: DFS for unvisited nodes"""
    n_cities: int = len(isConnected)
    unvisited: set[int] = set(range(n_cities))
    n_provinces = 0
    while unvisited:
        new_city: int = unvisited.pop()
        # run DFS
        dfs_unvisited_border = {new_city}
        while dfs_unvisited_border:
            current_city = dfs_unvisited_border.pop()
            unvisited.discard(current_city)
            neighbors = (neighbor_city for neighbor_city in unvisited if
                         isConnected[current_city][neighbor_city])
            for neighbor_city in neighbors:
                if neighbor_city in unvisited:
                    dfs_unvisited_border.add(neighbor_city)
        n_provinces += 1
    return n_provinces


def test_examples():
    assert findCircleNum([[1,1,0],
                          [1,1,0],
                          [0,0,1]]) == 2
    assert findCircleNum([[1,0,0],
                          [0,1,0],
                          [0,0,1]]) == 3


def test_1d():
    assert findCircleNum([[1]]) == 1


def test_2d():
    assert findCircleNum([[1,0],
                          [0,1]]) == 2
    assert findCircleNum(([[1,1],
                           [1,1]])) == 1


def test_3d():
    assert findCircleNum([[1,0,0],
                          [0,1,0],
                          [0,0,1]]) == 3
    assert findCircleNum([[1, 1, 0],
                          [1, 1, 0],
                          [0, 0, 1]]) == 2
    assert findCircleNum([[1, 0, 0],
                          [0, 1, 1],
                          [0, 1, 1]]) == 2
    assert findCircleNum([[1, 0, 1],
                          [0, 1, 0],
                          [1, 0, 1]]) == 2
    assert findCircleNum([[1, 1, 1],
                          [1, 1, 1],
                          [1, 1, 1]]) == 1


def test_4d():
    assert findCircleNum([[1, 0, 0, 1],
                          [0, 1, 0, 0],
                          [0, 0, 1, 0],
                          [1, 0, 0, 1]]) == 3
