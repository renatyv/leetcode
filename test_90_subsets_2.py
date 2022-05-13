def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    """Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
    The solution set must not contain duplicate subsets. Return the solution in any order.
    1 <= nums.length <= 10
    Idea: count number of symbols"""
    if len(nums) == 1:
        return [[], [nums[0]]]
    nums_count: dict[int, int] = dict()
    all_subsets = [[]]
    for num in nums:
        nums_count[num] = nums_count.get(num, 0) + 1
    for num in nums_count:
        add_subsets = []
        for repeat_times in range(1, nums_count[num] + 1):
            add_suffix = [num] * repeat_times
            add_subsets += [s + add_suffix for s in all_subsets]
        all_subsets += add_subsets
    return all_subsets


def test_examples():
    assert subsetsWithDup([1, 2]) == [[], [1], [2], [1, 2]]
    assert subsetsWithDup([1, 2, 2]) == [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]]
    assert subsetsWithDup([1, 2, 2, 2]) == [[], [1], [2], [1, 2], [2, 2], [1, 2, 2], [2, 2, 2], [1, 2, 2, 2]]
    assert subsetsWithDup([0]) == [[], [0]]


def test_corner():
    assert subsetsWithDup([1, 1]) == [[], [1], [1, 1]]
    assert subsetsWithDup([1, 1, 1]) == [[], [1], [1, 1], [1, 1, 1]]
    assert subsetsWithDup([1, 1, 2]) == [[], [1], [1, 1], [2], [1, 2], [1, 1, 2]]
