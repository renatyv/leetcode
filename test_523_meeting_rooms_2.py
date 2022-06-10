class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f'({self.start},{self.end})'


def min_meeting_rooms(intervals: list[Interval]) -> int:
    """https://www.lintcode.com/problem/919/"""
    if len(intervals) <= 1:
        return len(intervals)
    # sort by start time
    actions = []
    for interval in intervals:
        actions.append((interval.start, True))
        actions.append((interval.end, False))
    sorted_actions = sorted(actions)
    min_required_rooms = 1
    num_opened_rooms = 0
    for action in sorted_actions:
        _, open_action = action
        if open_action:
            num_opened_rooms += 1
        else:
            num_opened_rooms -= 1
        min_required_rooms = max(num_opened_rooms, min_required_rooms)
    return min_required_rooms


def test_edge_cases():
    assert min_meeting_rooms([Interval(0, 1)]) == 1
    assert min_meeting_rooms([Interval(0, 1), Interval(2, 3)]) == 1
    assert min_meeting_rooms([Interval(1, 2), Interval(2, 3)]) == 1
    assert min_meeting_rooms([Interval(1, 5),
                              Interval(2, 3),
                              Interval(2, 6)]) == 3
    assert min_meeting_rooms([Interval(1, 4),
                              Interval(2, 3),  # 0
                              Interval(3, 5)]) == 2
    assert min_meeting_rooms([Interval(1, 4),
                              Interval(2, 3),  # 0
                              Interval(3, 5),  # 0
                              Interval(4, 6),  # 0
                              Interval(7, 8)]) == 2


def test_examples():
    assert min_meeting_rooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]) == 2
    assert min_meeting_rooms([Interval(2, 7)]) == 1
