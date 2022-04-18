def twoSum(numbers: list[int], target: int) -> list[int]:
    """Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
    find two numbers such that they add up to a specific target number.
    Idea: Use binary search."""
    def binary_search(nums: list[int], from_index: int, to_index, target: int) -> (bool, int):
        """returns index such that nums[index] == target
        If such index is not found, nums[index]<target and nums[index+1] > target"""
        if nums[from_index] == target:
            return True, from_index
        if nums[to_index] == target:
            return True, to_index
        if from_index == to_index:
            return False, from_index
        left = from_index
        right = to_index
        while left+1 < right:
            center = left + (right - left)//2
            if nums[center] == target:
                return True, center
            if nums[center] > target:
                right = center
            else:
                left = center
        return False, left
    for first_index, num in enumerate(numbers):
        found, second_index = binary_search(numbers, first_index+1, len(numbers)-1, target-num)
        if found:
            return [first_index+1, second_index+1]
    raise KeyError()


def test_two_sum_2():
    assert twoSum([3,24,50,79,88,150,345], 200) == [3,6]


def test_two_sum_examples():
    assert twoSum([2,7,11,15], 9) == [1, 2]
    assert twoSum([2,3,4], 6) == [1, 3]
    assert twoSum([-1,0], -1) == [1, 2]


def test_two_sum_1():
    assert twoSum([-1, 0, 1], 0) == [1, 3]


