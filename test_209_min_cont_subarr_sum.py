def minSubArrayLen(target: int, nums: list[int]) -> int:
    """Given an array of positive integers nums and a positive integer target,
    return the minimal length of a contiguous subarray
    [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target.
    If there is no such subarray, return 0 instead.
    Idea: Sliding window, two pointers"""
    n = len(nums)
    left, right = 0, 0
    total = 0
    min_len = n + 1
    while right < n:
        total += nums[right]
        if total >= target:
            while left <= right and total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1
        right += 1
    return min_len if min_len != n + 1 else 0


def test_corner():
    assert minSubArrayLen(3, [0,1,0]) == 0
    assert minSubArrayLen(3, [0]) == 0
    assert minSubArrayLen(3, [3]) == 1
    assert minSubArrayLen(3, [1]) == 0


def test_2():
    assert minSubArrayLen(3, [2, 3]) == 1
    assert minSubArrayLen(3, [3, 2]) == 1


def test_3():
    assert minSubArrayLen(3, [1, 2, 3]) == 1
    assert minSubArrayLen(3, [3, 2, 1]) == 1
    assert minSubArrayLen(3, [1, 2, 0]) == 2
    assert minSubArrayLen(3, [1, 2, 1]) == 2
    assert minSubArrayLen(5, [1, 2, 1]) == 0
    assert minSubArrayLen(4, [1, 2, 1]) == 3


def test_examples():
    assert minSubArrayLen(7, [2,3,1,2,4,3]) == 2
    assert minSubArrayLen(4, [1,4,4]) == 1
    assert minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0
