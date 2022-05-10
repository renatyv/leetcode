def numSubarrayProductLessThanK(nums: list[int], k: int) -> int:
    """Given an array of integers nums and an integer k,
    return the number of contiguous subarrays
    where the product of all the elements in the subarray is strictly less than k.

    Idea: dynamic programming.
    Compute subproblem for index up to i, then compute for i+1
    n_subarrays[i]: number of cont. subarr. with product < k
    max_subarray_len[i]: maximal len of subarray ending at i, such that its product < k"""
    n_subarrays: list[int] = [0] * len(nums)
    # -1 means no subarrays
    max_subarray_len: list[int] = [0] * len(nums)
    # product for the max subbarray ending at i
    max_subarray_product: list[int] = [1] * len(nums)
    if nums[0] < k:
        n_subarrays[0] = 1
        max_subarray_len[0] = 1
        max_subarray_product[0] = nums[0]
    for i, num in enumerate(nums[1:], start=1):
        if nums[i] >= k:
            max_subarray_len[i] = 0
            n_subarrays[i] = n_subarrays[i - 1]
            continue
        # update max len of subarray, using solution from previous step
        # starting index for previous longest cont. subarray
        max_subarray_len[i] = max_subarray_len[i-1] + 1
        max_subarray_product[i] = max_subarray_product[i-1] * nums[i]
        while max_subarray_len[i] > 1 and max_subarray_product[i] >= k:
            starting_index = i - max_subarray_len[i]+1
            max_subarray_product[i] = max_subarray_product[i] // nums[starting_index]
            max_subarray_len[i] -= 1
        n_subarrays[i] = n_subarrays[i-1] + max_subarray_len[i]
    return n_subarrays[-1]


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
