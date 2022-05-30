def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    """There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
    You have a car with an unlimited gas tank
    and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
    You begin the journey with an empty tank at one of the gas stations.

    Given two integer arrays gas and cost,
    return the starting gas station's index if you can travel around the circuit
    once in the clockwise direction, otherwise return -1.
    If there exists a solution, it is guaranteed to be unique

    n == gas.length == cost.length
    1 <= n <= 105
    0 <= gas[i], cost[i] <= 104
    Two properties:
    1. Start from zero
    2. If maximum we can go starting from i is to j > i,
    then for all i<k<j:
    if we start from k we can not go further than j.
    Thus, next value we should check is j+1
    """
    if len(gas) == 1:
        if gas[0] >= cost[0]:
            return 0
        else:
            return -1
    start = 0
    while True:
        # skip if we can not start from here
        while gas[start] < cost[start]:
            start += 1
            if start == len(gas):
                return -1
        gas_left = gas[start] - cost[start]
        end = (start+1) % len(gas)
        # find how far can we go.
        while gas_left >= 0:
            if end == start:
                return start
            gas_left += gas[end]
            gas_left -= cost[end]
            end = (end + 1) % len(gas)
        # we now for shure, that starting position should not be in 0...start
        if end <= start:
            return -1
        # we can skip everything up until end
        start = end
    return -1


def test_edge_cases():
    assert canCompleteCircuit([1], [1]) == 0
    assert canCompleteCircuit([0], [1]) == -1
    assert canCompleteCircuit([0], [2]) == -1
    assert canCompleteCircuit([2], [2]) == 0
    assert canCompleteCircuit([1, 2, 3, 4],
                              [2, 3, 4, 5]) == -1
    assert canCompleteCircuit([2, 1, 1, 1],
                              [1, 2, 1, 1]) == 0
    assert canCompleteCircuit([1, 2, 1, 1],
                              [2, 1, 1, 1]) == 1


def test_examples():
    assert canCompleteCircuit([1, 2, 3, 4, 5],
                              [3, 4, 5, 1, 2]) == 3
    assert canCompleteCircuit([5, 1, 2, 3, 4],
                              [2, 3, 4, 5, 1]) == 4
    assert canCompleteCircuit([4, 5, 1, 2, 3],
                              [1, 2, 3, 4, 5]) == 0
    assert canCompleteCircuit([3, 4, 5, 1, 2],
                              [5, 1, 2, 3, 4]) == 1
    assert canCompleteCircuit([2, 3, 4, 5, 1],
                              [4, 5, 1, 2, 3]) == 2
    assert canCompleteCircuit([2, 3, 4],
                              [3, 4, 3]) == -1
    assert canCompleteCircuit([3, 4, 2],
                              [4, 3, 3]) == -1
    assert canCompleteCircuit([4, 2, 3],
                              [3, 3, 4]) == -1
