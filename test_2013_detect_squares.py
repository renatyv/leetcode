import collections


class DetectSquares:

    def __init__(self):
        # returns an empty set if key is not present
        # y is in self.x_points if [x,y] is added
        self._x_to_y = collections.defaultdict(set)
        # x is in self.y_points if [x,y] is added
        self._y_to_x = collections.defaultdict(set)
        # returns 0 if key is not present
        self._points_counter = collections.defaultdict(int)
        pass

    def add(self, point: list[int]) -> None:
        """Adds new points from the stream into a data structure.
        Duplicate points are allowed and should be treated as different points."""
        x, y = point
        self._x_to_y[x].add(y)
        self._y_to_x[y].add(x)
        self._points_counter[(x, y)] += 1

    def count(self, point: list[int]) -> int:
        """Given a query point,
        counts the number of ways to choose three points from the data structure such that
        the three points and the query point form an axis-aligned square with positive area."""
        x, y = point
        num_squares = 0
        for y_1 in self._x_to_y[x]:
            # square side
            a = y - y_1
            if a == 0:
                continue
            # check left square
            if (x - a) in self._y_to_x[y_1] \
                    and (x - a) in self._y_to_x[y]:
                num_squares += self._points_counter[(x, y_1)] \
                               * self._points_counter[(x - a, y_1)] \
                               * self._points_counter[(x - a, y)]
            # check right square
            if (x + a) in self._y_to_x[y_1] \
                    and (x + a) in self._y_to_x[y]:
                num_squares += self._points_counter[(x, y_1)] \
                               * self._points_counter[(x + a, y_1)] \
                               * self._points_counter[(x + a, y)]
        return num_squares


def test_edge_cases():
    detectSquares = DetectSquares()
    detectSquares.add([2, 2])
    detectSquares.add([2, 2])
    detectSquares.add([1, 2])
    detectSquares.add([1, 2])
    assert detectSquares.count([2, 2]) == 0
    detectSquares = DetectSquares()
    detectSquares.add([1, 1])
    detectSquares.add([1, 2])
    detectSquares.add([1, 3])
    detectSquares.add([2, 1])
    detectSquares.add([2, 3])
    detectSquares.add([3, 1])
    detectSquares.add([3, 2])
    detectSquares.add([3, 3])
    assert detectSquares.count([2, 2]) == 4
    assert detectSquares.count([1, 2]) == 0
    assert detectSquares.count([1, 1]) == 1
    assert detectSquares.count([3, 3]) == 1
    assert detectSquares.count([1, 3]) == 1
    assert detectSquares.count([3, 1]) == 1
    detectSquares.add([1, 2])
    assert detectSquares.count([2, 2]) == 6
    assert detectSquares.count([2, 2]) == 6


def test_examples():
    # ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
    # [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
    # [null, null, null, null, 1, 0, null, 2]
    detectSquares = DetectSquares()
    detectSquares.add([3, 10])
    detectSquares.add([11, 2])
    detectSquares.add([3, 2])
    assert detectSquares.count([11, 10]) == 1
    assert detectSquares.count([14, 8]) == 0
    detectSquares.add([11, 2])
    assert detectSquares.count([11, 10]) == 2
