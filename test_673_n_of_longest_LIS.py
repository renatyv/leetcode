def findNumberOfLIS(nums: list[int]) -> int:
    """Given an integer array nums, return the number of longest increasing subsequences.
    Notice that the sequence has to be strictly increasing.
    Idea: DP"""
    n = len(nums)
    len_of_LIS = [1] * n
    count = [1] * n
    for right in range(1, n):
        for left in range(right):
            if nums[right] > nums[left]:
                if len_of_LIS[right] < len_of_LIS[left] + 1:
                    len_of_LIS[right] = len_of_LIS[left] + 1
                    count[right] = count[left]
                elif len_of_LIS[right] == len_of_LIS[left] + 1:
                    count[right] += count[left]
    max_length = max(len_of_LIS)

    return sum(count[i] for i in range(n) if len_of_LIS[i] == max_length)


def test_wa_2():
    assert findNumberOfLIS([2, 2, 3,4]) == 2
    assert findNumberOfLIS([2,2,2,2,2,4,8,3,6,14,4,10,15,7,4,89]) == 35


def test_wa_1():
    assert findNumberOfLIS([1,3,2]) == 2
    assert findNumberOfLIS([1, 3, 2]) == 2
    assert findNumberOfLIS([1, 2, -2, -1, -4, -3]) == 3


def test_examples():
    assert findNumberOfLIS([1,3,5,4,7]) == 2
    assert findNumberOfLIS([2,2,2,2,2]) == 5


def test_corner_1():
    assert findNumberOfLIS([1]) == 1
    assert findNumberOfLIS([5,4,3,2,1]) == 5
    assert findNumberOfLIS([5, 4, 4]) == 3


def test_cases_1():
    assert findNumberOfLIS([1,2,-2,-1]) == 2
    assert findNumberOfLIS([1, 2, -2, -1]) == 2


def test_corner_large():
    assert findNumberOfLIS(list(range(2500))) == 1
    assert findNumberOfLIS(list(range(2500,0,-1))) == 2500
