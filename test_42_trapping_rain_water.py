def trap(height: list[int]) -> int:
    """Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.
    Idea: Dynamic programming.
    Compute two arrays:
    1) the largest height upto i, starting from left
    2) the largest height upto i, starting from right
    use them to compute volume of element i = min(largest_height_before, largest_height_after) - height[i]
    """
    if len(height) <= 2:
        return 0
    largest_height_upto = [0] * len(height)
    largest_height_upto[0] = height[0]
    largest_height_from = [0] * len(height)
    for i in range(1, len(height)):
        largest_height_upto[i] = max(largest_height_upto[i - 1], height[i])
    for i in range(1, len(height) + 1):
        largest_height_from[-i] = max(largest_height_from[-i + 1], height[-i])
    volume = 0
    for i in range(1, len(height) - 1):
        water_height_at_i = min(largest_height_upto[i - 1], largest_height_from[i + 1])
        volume += max(water_height_at_i - height[i], 0)
    return volume


def test_edge_cases():
    assert trap([1]) == 0
    assert trap([1, 2, 1]) == 0
    assert trap([2, 2]) == 0
    assert trap([2, 3]) == 0
    assert trap([3, 2]) == 0
    assert trap([1, 2, 3, 2, 2]) == 0
    assert trap([3, 2, 2]) == 0
    assert trap([2, 2, 3]) == 0
    assert trap([3, 2, 2, 2, 1]) == 0
    assert trap([1, 2, 2, 3]) == 0


def test_cases_1():
    assert trap([1, 0, 1]) == 1
    assert trap([1, 0, 2]) == 1
    assert trap([2, 0, 1]) == 1
    assert trap([2, 0, 2]) == 2
    assert trap([3, 0, 1, 0, 1]) == 2
    assert trap([3, 0, 3, 0, 1]) == 4
    assert trap([1, 0, 3, 0, 3]) == 4
    assert trap([1, 0, 3, 3, 3]) == 1
    assert trap([1, 0, 3, 3, 2]) == 1
    assert trap([1, 0, 3, 2, 3]) == 2


def test_examples():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
