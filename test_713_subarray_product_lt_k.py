def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    """Given an array of integers nums and an integer k,
    return the number of contiguous subarrays
    where the product of all the elements in the subarray is strictly less than k.

    Idea: dynamic programming.
    Compute subproblem for index up to i, then compute for i+1
    multiply by new value and then divide previous max product by leftmost index until it is less than k"""
    if k <= 1:
        return 0
    left_index = 0
    n_subarrays = 0
    # product for the max subbarray ending at i
    max_subarray_product = 1
    for right_index, num in enumerate(nums):
        max_subarray_product = max_subarray_product * num
        while max_subarray_product >= k:
            max_subarray_product = max_subarray_product // nums[left_index]
            left_index += 1
        n_subarrays += (right_index-left_index) + 1
    return n_subarrays


def test_1():
    assert numSubarrayProductLessThanK([1], 1) == 0
    assert numSubarrayProductLessThanK([1], 2) == 1


def test_2():
    assert numSubarrayProductLessThanK([2, 1], 1) == 0
    assert numSubarrayProductLessThanK([1, 2], 2) == 1 # [1]
    assert numSubarrayProductLessThanK([2, 1], 2) == 1  # [1]
    assert numSubarrayProductLessThanK([2, 1], 3) == 3  # [1], [2], [2,1]
    assert numSubarrayProductLessThanK([1, 2], 3) == 3  # [1], [2], [1,2]


def test_3():
    assert numSubarrayProductLessThanK([1, 2, 3], 2) == 1 # [1]
    assert numSubarrayProductLessThanK([2, 1, 3], 2) == 1 # [1]
    assert numSubarrayProductLessThanK([2, 3, 1], 2) == 1 # [1]
    assert numSubarrayProductLessThanK([1, 3, 2], 3) == 2  # [1], [2]
    assert numSubarrayProductLessThanK([2, 3, 1], 3) == 2  # [2], [1]
    assert numSubarrayProductLessThanK([2, 1, 3], 3) == 3  # [2], [1], [2,1]
    assert numSubarrayProductLessThanK([1, 2, 3], 3) == 3  # [1], [2], [2,1]
    assert numSubarrayProductLessThanK([3, 2, 1], 3) == 3  # [2], [1], [2,1]
    assert numSubarrayProductLessThanK([1, 2, 3], 4) == 4  # [1], [2], [3], [1,2]
    assert numSubarrayProductLessThanK([3, 2, 1], 4) == 4  # [3], [2], [1], [2,1]
    assert numSubarrayProductLessThanK([2, 1, 3], 4) == 5  # [2], [1], [3], [2,1], [1,3]
    assert numSubarrayProductLessThanK([2, 1, 3], 10) == 6  # [2], [1], [3], [2,1], [1,3], [2,1,3]


def test_example():
    assert numSubarrayProductLessThanK([10,5,2,6], 100) == 8
    assert numSubarrayProductLessThanK([1,2,3], 0) == 0


def test_wa():
    assert numSubarrayProductLessThanK([6,2,10,9,3], 13) == 6
    assert numSubarrayProductLessThanK([6,2,10,10,9,3], 18) == 7
    assert numSubarrayProductLessThanK([10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3], 19) == 18
