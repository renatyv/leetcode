def numberOfArithmeticSlices(nums: list[int]) -> int:
    """An integer array is called arithmetic if it consists of at least three elements
    and if the difference between any two consecutive elements is the same.
    For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
    Given an integer array nums, return the number of arithmetic subarrays of nums.

    A subarray is a contiguous subsequence of the array.
    Idea: dynamic programming.
    1. Compute number of slices for array nums[:-1]
    2. Compute longest slice, ending at nums[-2]
    3. Use that to compute number of slices and longest slice ending at nums[-1]"""
    if len(nums) < 3:
        return 0
    slices_number = 0
    length_of_slice_ending_prev = 2
    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
            length_of_slice_ending_at_i = length_of_slice_ending_prev + 1
            slices_number = slices_number + max(0, length_of_slice_ending_at_i - 2)
        else:
            length_of_slice_ending_at_i = 2
        length_of_slice_ending_prev = length_of_slice_ending_at_i
    return slices_number


def corner_cases():
    assert numberOfArithmeticSlices([1, 2]) == 0
    assert numberOfArithmeticSlices([1, 3]) == 0
    assert numberOfArithmeticSlices([1, 1, 1]) == 0
    assert numberOfArithmeticSlices([1, 2, 4]) == 0
    assert numberOfArithmeticSlices([4, 2, 1]) == 0
    assert numberOfArithmeticSlices([1, 2, 4, 5]) == 0
    assert numberOfArithmeticSlices([5, 4, 2, 1]) == 0
    assert numberOfArithmeticSlices([1, 3, 1, 4]) == 0


def test_one():
    assert numberOfArithmeticSlices([1, 2, 3]) == 1
    assert numberOfArithmeticSlices([3, 2, 1]) == 1
    assert numberOfArithmeticSlices([3, 2, 1, -1]) == 1
    assert numberOfArithmeticSlices([-1, 1, 2, 3]) == 1
    assert numberOfArithmeticSlices([-1, 1, 2, 3, 5]) == 1
    assert numberOfArithmeticSlices([-1, 3, 2, 1, 5]) == 1


def test_two():
    assert numberOfArithmeticSlices([3, 2, 1, 2, 3]) == 2
    assert numberOfArithmeticSlices([1, 2, 3, 3, 2, 1]) == 2


def test_6():
    assert numberOfArithmeticSlices([1, 2, 3, 4, 5]) == 6


def test_examples():
    assert numberOfArithmeticSlices([1, 2, 3, 4]) == 3
    assert numberOfArithmeticSlices([1]) == 0
