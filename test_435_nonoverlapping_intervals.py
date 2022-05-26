def eraseOverlapIntervals(intervals: list[list[int]]) -> int:
    """Given an array of intervals where intervals[i] = [starti, endi],
    return the minimum number of intervals you need
    to remove to make the rest of the intervals non-overlapping.
    1. Sort by left-hand side of the intervals
    2. if intervals are overlapping, leave the one with the lowest right-hand side"""
    sorted_intervals = sorted(intervals, key=lambda interval: interval[0])

    overlapping_count = 0
    prev_left, prev_right = sorted_intervals[0]
    i = 1
    while i < len(sorted_intervals):
        left, right = sorted_intervals[i]
        # skip non-overlapping
        if left >= prev_right:
            prev_right = right
        else:
            # overlapping
            overlapping_count += 1
            # take the shortest
            prev_right = min(prev_right, right)
        i += 1
    return overlapping_count


def test_corner_cases():
    assert eraseOverlapIntervals([[1, 8], [2, 3], [4, 5], [6, 7]]) == 1


def test_examples():
    assert eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
