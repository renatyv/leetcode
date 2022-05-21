def maxSubArray(nums: list[int]) -> int:
    """
    Given an integer array nums, find the contiguous subarray (containing at least one number)
    which has the largest sum and return its sum.
    A subarray is a contiguous part of an array.
    Solution idea: Kadane's algorithm.
    Compute max subarray for all subarrays ending with [i] using info from [i-1]"""
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    max_sum_subarray_ending_at_i = 0
    global_max_sum = -10 ** 4 - 1
    for num in nums:
        # you either add element to previous array or start a new one
        max_sum_subarray_ending_at_i = max(num,
                                           max_sum_subarray_ending_at_i + num)
        global_max_sum = max(global_max_sum, max_sum_subarray_ending_at_i)
    return global_max_sum


def test_max_subarray_examples():
    assert maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert maxSubArray([1]) == 1
    assert maxSubArray([5, 4, -1, 7, 8]) == 23
