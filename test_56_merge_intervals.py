def merge(intervals: list[list[int]]) -> list[list[int]]:
    """Given an array of intervals where intervals[i] = [starti, endi],
    merge all overlapping intervals, and return an array of the non-overlapping intervals
    that cover all the intervals in the input.
    Idea:
    1) sort by left-hand side
    2) keep track of the previous interval.
    If i-th interval is overlapping with previous, expand the latter"""
    if len(intervals) <= 1:
        return intervals
    # sort by left side
    sorted_intervals = list(sorted(intervals, key=lambda interval: interval[0]))
    merged_intervals = []
    # dummy previous interval [-2,-1]
    prev_left, prev_right = [-2, -1]
    i = 0
    while i < len(sorted_intervals):
        i_left, i_right = sorted_intervals[i]
        if i_left > prev_right:  # no overlap with current interval, put current in the resulting array
            merged_intervals.append([prev_left, prev_right])
            prev_left, prev_right = i_left, i_right
        else:
            # overlap detected, expand previous interval
            prev_right = max(prev_right, i_right)
        i += 1
    merged_intervals.append([prev_left, prev_right])
    return merged_intervals[1:]


def test_merge_corner():
    assert merge([[1, 2]]) == ([[1, 2]])
    assert merge([[2, 6], [1, 3]]) == [[1, 6]]
    assert merge([[1, 3], [4, 6]]) == [[1, 3], [4, 6]]
    assert merge([[1, 4], [4, 6]]) == [[1, 6]]
    assert merge([[1, 4], [2, 3]]) == [[1, 4]]


def test_chain():
    assert merge([[1, 4], [2, 6], [3, 4], [5, 7]]) == [[1, 7]]


def test_examples():
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
