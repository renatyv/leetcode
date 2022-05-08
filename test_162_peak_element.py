def findPeakElement(nums: list[int]) -> int:
    """A peak element is an element that is strictly greater than its neighbors.
    Given an integer array nums, find a peak element, and return its index.
    If the array contains multiple peaks, return the index to any of the peaks.
    You may imagine that nums[-1] = nums[n] = -∞.
    You must write an algorithm that runs in O(log n) time.

    Idea: run modified binary search.
    If next to pivot element is greater, sequence is rising, peak is to the right.
    Otherwise, peak is somewhere to the left"""
    def is_peak(nums: list[int], index: int) -> bool:
        if index == 0:
            return nums[0] > nums[1]
        if index == len(nums)-1:
            return nums[-2] < nums[-1]
        return nums[index-1] < nums[index] > nums[index+1]
    if len(nums) == 1:
        return 0
    left = 0
    if is_peak(nums, left):
        return left
    right = len(nums)-1
    if is_peak(nums, right):
        return right
    while left+1 < right:
        pivot = left + (right-left)//2
        if is_peak(nums, pivot):
            return pivot
        if nums[pivot+1] > nums[pivot]:
            left = pivot
        else:
            right = pivot
    return right


def test_examples():
    assert findPeakElement([1,2,3,1]) == 2
    res = findPeakElement([1,2,1,3,5,6,4])
    assert res == 5 or res == 1


def test_corner():
    assert findPeakElement([1]) == 0
    assert findPeakElement([5,4,3,2]) == 0
    assert findPeakElement([1,2,3,4]) == 3


def test_2():
    assert findPeakElement([1,2]) == 1
    assert findPeakElement([2,1]) == 0


def test_3():
    assert findPeakElement([3,2,1]) == 0
    assert findPeakElement([1, 3, 2]) == 1
    assert findPeakElement([1, 2, 3]) == 2
    res = findPeakElement([1, 0, 1])
    assert res == 0 or res == 2


def test_4():
    assert findPeakElement([1,2,1,0]) == 1
    assert findPeakElement([1,2,3,1]) == 2


def test_5():
    assert findPeakElement([1,2,1,0,-1]) == 1
    assert findPeakElement([-1,0,2,1,-1]) == 2
    assert findPeakElement([0,1,2,1,0]) == 2
    assert findPeakElement([0, 1, 2, 3, 2]) == 3
    assert findPeakElement([0, 3, 2, 1, 0]) == 1


def test_5():
    assert findPeakElement([1, 2, 1, 0, -1]) == 1
    assert findPeakElement([-1, 0, 2, 1, -1]) == 2
    assert findPeakElement([0, 1, 2, 1, 0]) == 2
    assert findPeakElement([0, 1, 2, 3, 2]) == 3
    assert findPeakElement([0, 3, 2, 1, 0]) == 1
    assert findPeakElement([0, 1, 2, 1, 0]) == 2
    res = findPeakElement([0, 1, 0, 1, 0])
    assert  res == 1 or res == 3


def test_6():
    assert findPeakElement([0,1,2,1,0,-1]) == 2
    assert findPeakElement([-1, 0, -1, -2, -1, -3]) == 1
    assert findPeakElement([-2, -1, 0, -1, -2, -3]) == 2
    assert findPeakElement([-3, -2, -1, 0, -1, -2]) == 3
    assert findPeakElement([-4, -3, -2, -1, 0, -1]) == 4
