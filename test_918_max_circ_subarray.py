def maxSubarraySumCircular(nums: list[int]) -> int:
    """Given a circular integer array nums of length n,
    return the maximum possible sum of a non-empty subarray of nums.

    A circular array means the end of the array connects to the beginning of the array.
    Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i]
    is nums[(i - 1 + n) % n].

    A subarray may only include each element of the fixed buffer nums at most once.
    Formally, for a subarray nums[i], nums[i + 1], ..., nums[j],
    there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

    Idea 1: do kadane's algotihm
    Idea 2: Find minimal subarray. To do that invert signs and run cadane's.
    """
    def kadane(nums: list[int]) -> int:
        """Compute max subarray for all subarrays ending with [i] using info from [i-1]"""
        global_max_sum = nums[0]
        local_max_sum = nums[0]
        for num in nums[1:]:
            # max sum taking the next element = taking previous one, or starting new sum from the current one
            local_max_sum = max(num, local_max_sum + num)
            global_max_sum = max(global_max_sum, local_max_sum)
        return global_max_sum
    max_linear_cont_subarray = kadane(nums)
    max_negative_cont_subarray = kadane([-num for num in nums])
    # if all elements are negative
    if sum(nums) == -max_negative_cont_subarray:
        return max_linear_cont_subarray
    max_wrap_subarray = sum(nums)+max_negative_cont_subarray
    return max(max_linear_cont_subarray, max_wrap_subarray)


def test_edge_cases():
    assert maxSubarraySumCircular([1]) == 1
    assert maxSubarraySumCircular([-1]) == -1
    assert maxSubarraySumCircular([-1, 1]) == 1


def circular_cases():
    assert maxSubarraySumCircular([-1, 1, 2]) == 3
    assert maxSubarraySumCircular([1, -1, 2]) == 3
    assert maxSubarraySumCircular([2, 1, -1]) == 3
    assert maxSubarraySumCircular([-3, -2, -1]) == -1


def test_exmaples():
    assert maxSubarraySumCircular([1, -2, 3, -2]) == 3
    assert maxSubarraySumCircular([5,-3,5]) == 10
    assert maxSubarraySumCircular([-3,-2,-3]) == -2
