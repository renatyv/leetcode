def subsets(nums: list[int]) -> list[list[int]]:
    """Given an integer array nums of unique elements, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.
    1 <= nums.length <= 10
    Idea: use recursion
    """
    if len(nums) == 1:
        return [[], [nums[0]]]
    prev_subsets = subsets(nums[:-1])
    return prev_subsets \
           + [prev_set + [nums[-1]] for prev_set in prev_subsets]


def test_examples():
    assert subsets([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert subsets([0]) == [[], [0]]


def test_corner_cases():
    assert subsets([1]) == [[], [1]]
