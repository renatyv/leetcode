def intervalIntersection(firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
    """
    You are given two lists of closed intervals, firstList and secondList, where
    firstList[i] = [starti, endi] and secondList[j] = [startj, endj].
    Each list of intervals is pairwise disjoint and in sorted order.

    Return the intersection of these two interval lists.

    A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

    The intersection of two closed intervals is a set of real numbers
    that are either empty or represented as a closed interval.
    For example, the intersection of [1, 3] and [2, 4] is [2, 3].
    Idea:
    1. put all interval starts and ends into one sorted array
    2. If first interval closes at the opening of the second interval,
    in the sorted array the opening should be before closing
    3. Maintain two flags:
        interval_1_opened, interval_2_opened
    4. if both flags are opened - we are in the intersection.
    """
    if len(firstList) == 0 or len(secondList) == 0:
        return []
    # list of (position, magic).
    #  magic == 0 if it is opening end for the first interval
    #  magic == 1 if it is opening end for the second interval
    #  magic == 3 if it is closing end for the first interval
    #  magic == 2 if it is closing end for the second interval
    list_of_ends: list[tuple[int, int]] = []
    for row in firstList:
        list_of_ends.append((row[0], 0))
        list_of_ends.append((row[1], 3))
    for row in secondList:
        list_of_ends.append((row[0], 1))
        list_of_ends.append((row[1], 2))
    list_of_ends.sort(key=lambda x: x[0] + (x[1] / 10))
    interval_intersections = []
    first_opened = False
    second_opened = False
    intersection_start = -1
    for interval_border, list_num in list_of_ends:
        # we encountered an end of intersection
        if first_opened and second_opened:
            intersection_end = interval_border
            interval_intersections.append([intersection_start, intersection_end])
        # if it is first interval
        if list_num == 0 or list_num == 3:
            first_opened = not first_opened
        else:
            second_opened = not second_opened
        #     start of the intersection
        if first_opened and second_opened:
            intersection_start = interval_border
    return interval_intersections


def test_examples():
    assert intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]],
                                [[1, 5], [8, 12], [15, 24], [25, 26]]) == [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24],
                                                                           [25, 25]]
    assert intervalIntersection([[1, 3], [5, 9]], []) == []


def test_empty_cases():
    assert intervalIntersection([], [[1, 3], [5, 9]]) == []
    assert intervalIntersection([[1, 3], [5, 9]], []) == []
    assert intervalIntersection([], []) == []
    assert intervalIntersection([[1, 2]], [[3, 4]]) == []
    assert intervalIntersection([[3, 4]], [[1, 2]]) == []


def test_edge_cases():
    assert intervalIntersection([[1, 2]], [[1, 2]]) == [[1, 2]]
    assert intervalIntersection([[1, 4]], [[2, 3]]) == [[2, 3]]
    assert intervalIntersection([[2, 3]], [[1, 4]]) == [[2, 3]]
    assert intervalIntersection([[2, 2]], [[1, 4]]) == [[2, 2]]
    assert intervalIntersection([[1, 2]], [[2, 3]]) == [[2, 2]]
    assert intervalIntersection([[2, 3]], [[1, 2]]) == [[2, 2]]
    assert intervalIntersection([[1, 3]], [[2, 3]]) == [[2, 3]]
    assert intervalIntersection([[1, 3]], [[1, 2]]) == [[1, 2]]
    assert intervalIntersection([[1, 4]], [[2, 5]]) == [[2, 4]]
