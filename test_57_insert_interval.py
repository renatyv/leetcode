def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    if len(intervals) == 0:
        return [newInterval]
    new_start, new_end = newInterval
    resulting_intervals = []
    i = 0
    # skip intervals which end before the new interval starts
    while i < len(intervals) and intervals[i][1] < new_start:
        resulting_intervals.append(intervals[i])
        i += 1
    if i == len(intervals):
        resulting_intervals.append(newInterval)
        return resulting_intervals
    # now merge new interval
    left, right = intervals[i]
    merged_start = min(new_start, left)
    merged_end = new_end
    # find last interval starting inbetween new_start, new_end
    while i < len(intervals) and intervals[i][0] <= new_end:
        right = intervals[i][1]
        merged_end = max(new_end, right)
        i += 1
    resulting_intervals.append([merged_start, merged_end])
    # add what is left
    while i < len(intervals):
        resulting_intervals.append(intervals[i])
        i += 1
    return resulting_intervals


def test_corner_cases():
    assert insert([], [0, 1]) == [[0, 1]]
    assert insert([], [2, 4]) == [[2, 4]]
    assert insert([[3, 6]], [0, 2]) == [[0, 2], [3, 6]]
    assert insert([[3, 6]], [0, 3]) == [[0, 6]]
    assert insert([[3, 6]], [0, 6]) == [[0, 6]]
    assert insert([[3, 6]], [3, 6]) == [[3, 6]]
    assert insert([[3, 6]], [4, 5]) == [[3, 6]]
    assert insert([[3, 6]], [0, 8]) == [[0, 8]]
    assert insert([[3, 6]], [2, 8]) == [[2, 8]]
    assert insert([[3, 6]], [6, 8]) == [[3, 8]]


def test_two_intervals():
    assert insert([[3, 4], [6, 6]], [0, 2]) == [[0, 2], [3, 4], [6, 6]]
    assert insert([[3, 4], [6, 6]], [0, 3]) == [[0, 4], [6, 6]]
    assert insert([[3, 4], [6, 6]], [0, 6]) == [[0, 6]]
    assert insert([[3, 4], [6, 6]], [3, 6]) == [[3, 6]]
    assert insert([[3, 4], [6, 6]], [4, 5]) == [[3, 5], [6, 6]]
    assert insert([[3, 4], [6, 6]], [0, 8]) == [[0, 8]]
    assert insert([[3, 4], [6, 6]], [3, 8]) == [[3, 8]]
    assert insert([[3, 4], [6, 6]], [6, 8]) == [[3, 4], [6, 8]]


def test_examples():
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
