import sys


def threeSumClosest(nums: list[int], target: int) -> int:
    """Given an integer array nums of length n and an integer target,
    find three integers in nums such that the sum is closest to target.
    Return the sum of the three integers.

    You may assume that each input would have exactly one solution.
    Idea:
    1. sort the array
    2. use three indexes i1 < i2 < i3
    3. When pair (i1, i2) is fixed, use binary search to find i3
    """

    sorted_nums = list(sorted(nums))
    n = len(sorted_nums)

    def binary_search(start_index, target):
        """Search for the element closest to target in a sorted list starting from start_index"""
        nonlocal sorted_nums
        left = start_index
        right = len(sorted_nums) - 1
        if left == right:
            return left
        while left + 1 < right:
            pivot = left + (right - left) // 2
            if sorted_nums[pivot] == target:
                return pivot
            if target < sorted_nums[pivot]:
                right = pivot
            else:
                left = pivot
        # find which one of left and right is closer to target
        if abs(sorted_nums[left] - target) < abs(sorted_nums[right] - target):
            return left
        else:
            return right

    closest_sum = sum(sorted_nums[:3])
    if target <= closest_sum:
        return closest_sum
    closest_sum = sum(sorted_nums[-3:])
    if target >= closest_sum:
        return closest_sum
    for i1 in range(n - 2):
        for i2 in range(i1 + 1, n - 1):
            i3_target = target - sorted_nums[i1] - sorted_nums[i2]
            i3 = binary_search(i2 + 1, i3_target)
            current_sum = sorted_nums[i1] + sorted_nums[i2] + sorted_nums[i3]
            if current_sum == target:
                return target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
    return closest_sum


def test_corner_cases():
    assert threeSumClosest([1, 1, 1], 4) == 3
    assert threeSumClosest([1, 1, 1], 0) == 3
    assert threeSumClosest([1, 2, 1, 1], 3) == 3
    assert threeSumClosest([1, 2, 1, 1], 5) == 4
    assert threeSumClosest([1, 2, 1, 1], 4) == 4
    assert threeSumClosest([1, 2, 1, 1], 3) == 3
    assert threeSumClosest([1, 2, 1, 1], 2) == 3
    assert threeSumClosest([1, 2, 1, 1], 1) == 3


def test_examples():
    assert threeSumClosest([-1, 2, 1, -4], 1) == 2
    assert threeSumClosest([0, 0, 0], 1) == 0


def test_wa1():
    assert threeSumClosest([1, 6, 9, 14, 16, 70], 81) == 80
