from math import ceil


def minEatingSpeed(piles: list[int], h: int) -> int:
    """ Idea: binary search for eating speed."""
    if h == len(piles):
        return max(piles)
    # time is larger than number of bnanas
    if sum(piles) <= h:
        return 1
    sorted_piles = sorted(piles)

    def get_eat_time(sorted_piles: list[int], bananas_per_h: int) -> int:
        """given the eating speed, returns number of hours required for eating the pile"""
        total_time = 0
        pile_num = len(sorted_piles) - 1
        while pile_num >= 0 and sorted_piles[pile_num] > bananas_per_h:
            total_time += ceil(sorted_piles[pile_num] / bananas_per_h)
            pile_num -= 1
        total_time += pile_num + 1
        return total_time

    # binary search
    min_speed = 1
    max_speed = max(piles)
    while min_speed + 1 < max_speed:
        pivot_speed = min_speed + (max_speed - min_speed) // 2
        pivot_time = get_eat_time(sorted_piles, pivot_speed)
        # speed is too small, not enough time
        if pivot_time > h:
            min_speed = pivot_speed
        else:
            max_speed = pivot_speed
    return max_speed


def test_edge_cases():
    assert minEatingSpeed([1, 2], 2) == 2
    assert minEatingSpeed([3], 2) == 2
    assert minEatingSpeed([3], 1) == 3
    assert minEatingSpeed([4], 2) == 2
    assert minEatingSpeed([3], 4) == 1
    assert minEatingSpeed([2, 3], 2) == 3
    assert minEatingSpeed([2, 3], 3) == 2
    assert minEatingSpeed([2, 3], 4) == 2


def test_examples():
    assert minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert minEatingSpeed([4, 11, 20, 23, 30], 5) == 30
    assert minEatingSpeed([4, 11, 20, 23, 30], 6) == 23
