def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    """There are n cars going to the same destination along a one-lane road.
    The destination is target miles away.
    You are given two integer array position and speed, both of length n,
    where position[i] is the position of the ith car
    and speed[i] is the speed of the ith car (in miles per hour).
    A car can never pass another car ahead of it,
    but it can catch up to it and drive bumper to bumper at the same speed.
    The faster car will slow down to match the slower car's speed.
    The distance between these two cars is ignored
    (i.e., they are assumed to have the same position).
    A car fleet is some non-empty set of cars driving at the same position and same speed.
    Note that a single car is also a car fleet.
    If a car catches up to a car fleet right at the destination point,
    it will still be considered as one car fleet.
    Return the number of car fleets that will arrive at the destination.
    1<= position.length == speed.length <= 10^5
    0 <= position[i] < target
    0 < target <= 10^6
    0 < speed[i] <= 10^6

    Idea: use monotonic stack
    1) Sort by position
    2) Use monotonic stack for arrival time"""
    positions_and_speed = [(i, j) for i, j in zip(position, speed)]
    positions_and_speed.sort(reverse=True)
    arrival_time_sorted_stack = []
    for pos, speed in positions_and_speed:
        arrival_time = (target - pos) / speed
        if not arrival_time_sorted_stack\
                or arrival_time > arrival_time_sorted_stack[-1]:
            arrival_time_sorted_stack.append(arrival_time)
    return len(arrival_time_sorted_stack)


def test_edge_cases():
    assert carFleet(10, [1], [1]) == 1
    assert carFleet(3, [0, 1], [1, 2]) == 2
    assert carFleet(2, [0, 1], [2, 1]) == 1
    assert carFleet(3, [0, 1], [2, 1]) == 1
    assert carFleet(1, [0, 1], [2, 1]) == 2


def test_examples():
    assert carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert carFleet(10, [3], [3]) == 1
    assert carFleet(100, [0, 2, 4], [4, 2, 1]) == 1
