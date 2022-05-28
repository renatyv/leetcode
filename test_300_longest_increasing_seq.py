def lengthOfLIS(nums: list[int]) -> int:
    """Given an integer array nums, return the length of the longest strictly increasing subsequence.
    A subsequence is a sequence that can be derived from an array by deleting some
    or no elements without changing the order of the remaining elements.
    For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
    Idea: dynamic programming: save longest list ending at i.
    1) Go back the array with index LIS_for_smaller_nums over all elements smaller than nums[i]
    and update the local maximum:
    len_of_LIS_ending_at[i] = max(len_of_LIS_ending_at[LIS_for_smaller_nums]+1, len_of_LIS_ending_at[i])
    3) find the maximum of len_of_LIS_ending_at"""
    if len(nums) == 1:
        return 1
    # start dynamic programming
    len_of_LIS_ending_at = [1] * len(nums)
    max_LIS = 1
    for right in range(1, len(nums)):
        left = right
        if nums[right - 1] == nums[right]:
            len_of_LIS_ending_at[right] = len_of_LIS_ending_at[right - 1]
        else:
            # for all elements smaller than nums[right], try adding nums[right]. Find maximum
            while left >= 1:
                left -= 1
                if nums[left] >= nums[right]:
                    continue
                if left == -1:
                    len_of_LIS_ending_at[right] = 1
                len_of_LIS_ending_at[right] = max(len_of_LIS_ending_at[left] + 1,
                                                  len_of_LIS_ending_at[right])
        max_LIS = max(max_LIS, len_of_LIS_ending_at[right])
    return max_LIS


def test_corner_cases():
    assert lengthOfLIS([1]) == 1
    assert lengthOfLIS([1, 2]) == 2
    assert lengthOfLIS([2, 1]) == 1
    assert lengthOfLIS([1, 2, -1]) == 2
    assert lengthOfLIS([-1, 1, 2]) == 3
    assert lengthOfLIS([1, 2, 3, -3, -2, -1]) == 3
    assert lengthOfLIS([2, 3, -3, -2, 0]) == 3


def test_examples():
    assert lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
    assert lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1


def test_corner_large():
    assert lengthOfLIS(list(range(2500))) == 2500
    assert lengthOfLIS(list(range(2500, 0, -1))) == 1
    assert lengthOfLIS([2] * 2500) == 1
