class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


def can_attend_meetings(intervals: list[Interval]) -> bool:
    """https://www.lintcode.com/problem/920/"""
    # sort by interval start
    sorted_intervals = sorted(intervals, key=lambda x: x.start)
    for prev, cur in zip(sorted_intervals[:-1], sorted_intervals[1:]):
        if prev.start < cur.start < prev.end:
            return False
    # Write your code here
    return True


def test_edge_cases():
    assert can_attend_meetings([Interval(1, 2), Interval(3, 4)])
    assert can_attend_meetings([Interval(3, 4), Interval(1, 2)])
    assert can_attend_meetings([Interval(3, 4), Interval(1, 2), Interval(5, 6)])
    assert not can_attend_meetings([Interval(2, 5), Interval(3, 4), Interval(6, 8)])
    assert not can_attend_meetings([Interval(2, 5), Interval(3, 4)])
    assert not can_attend_meetings([Interval(2, 5), Interval(4, 8)])
    assert not can_attend_meetings([Interval(2, 5), Interval(1, 3)])


def test_examples():
    assert not can_attend_meetings([Interval(0, 30), Interval(5, 10), Interval(15, 20)])
    assert can_attend_meetings([Interval(5, 8), Interval(9, 15)])
