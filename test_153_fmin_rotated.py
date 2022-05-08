def findMin(nums: list[int]) -> int:
    """Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
    For example, the array nums = [0,1,2,4,5,6,7] might become:
    [4,5,6,7,0,1,2] if it was rotated 4 times.
    [0,1,2,4,5,6,7] if it was rotated 7 times.
    Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
    [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
    Given the sorted rotated array nums of unique elements, return the minimum element of this array.

    You must write an algorithm that runs in O(log n) time.
    Idea: find rotation number using binary search
    Cases:
    m = min(nums)
    M = max(nums)
    l - leftmost element
    r - rightmost element
    p - element in the middle
    All possible cases:
    [m....M]            l < r
    [l...p...Mm...r]    l > r, p > r
    [l...Mm...p...r]    l > r, p < r"""
    if len(nums) == 1:
        return nums[0]
    if nums[0] < nums[-1]:
        return nums[0]
    left_index = 0
    right_index = len(nums)-1
    pivot = 0
    while left_index +1 < right_index:
        pivot = left_index + (right_index - left_index)//2
        if nums[pivot] > nums[left_index]:
            left_index = pivot
        else:
            right_index = pivot
    return nums[right_index]


def test_examples():
    assert findMin([3,4,5,1,2]) == 1
    assert findMin([4,5,6,7,0,1,2]) == 0
    assert findMin([11,13,15,17]) == 11


def test_corner_cases():
    assert findMin([1]) == 1
    assert findMin([1, 2]) == 1
    assert findMin([2, 1]) == 1


def test_cases_3():
    assert findMin([1, 2, 3]) == 1
    assert findMin([3, 1, 2]) == 1
    assert findMin([2, 3, 1]) == 1


def test_cases_4():
    assert findMin([1, 2, 3, 4]) == 1
    assert findMin([4, 1, 2, 3]) == 1
    assert findMin([3, 4, 1, 2]) == 1
    assert findMin([2, 3, 4, 1]) == 1
