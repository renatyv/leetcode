def maxProduct(nums: list[int]) -> int:
    """Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
    and return the product.
    The test cases are generated so that the answer will fit in a 32-bit integer.
    A subarray is a contiguous subsequence of the array.
    Idea: dynamic programming
    Use two arrays:
    1) max_product[i] --- contiguous subarray ending at i having max product
    2) min_product[i] --- contiguous subarray ending at i having min negative product
    use i-1 to compute i
    Save only previous values max_product[i-1] and max_product[i-1] instead of the whole arrays"""
    if len(nums) == 1:
        return nums[0]
    prev_min = nums[0]
    prev_max = nums[0]
    abs_max = nums[0]
    for i in range(1, len(nums)):
        cur_max = max(nums[i], prev_max * nums[i], prev_min * nums[i])
        cur_min = min(nums[i], prev_max * nums[i], prev_min * nums[i])
        abs_max = max(cur_max, abs_max)
        prev_min, prev_max = cur_min, cur_max
    return abs_max


def test_corner_cases():
    assert maxProduct([1]) == 1
    assert maxProduct([-1]) == -1
    assert maxProduct([1, 2]) == 2
    assert maxProduct([-1, 1]) == 1
    assert maxProduct([-2, 3, -4]) == 24
    assert maxProduct([-2, 2, 0, 2, 2, 0, -1, -2]) == 4
    assert maxProduct([-2, 2, 0, 2, 2, 0, -1, -2]) == 4
    assert maxProduct([-2, 2, 0, 2, 2, 0, -1, -2, 0, -2, -3]) == 6


def test_examples():
    assert maxProduct([2, 3, -2, 4]) == 6
    assert maxProduct([-2, 0, -1]) == 0
