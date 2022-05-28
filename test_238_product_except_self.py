def productExceptSelf(nums: list[int]) -> list[int]:
    """Given an integer array nums, return an array answer such that answer[i] is equal to
    the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation."""
    if len(nums) == 1:
        return nums
    if len(nums) == 2:
        return [nums[1], nums[0]]
    product_of_prefix = [0] * len(nums)
    product_of_suffix = [0] * len(nums)
    product_of_prefix[0] = nums[0]
    product_of_suffix[-1] = nums[-1]
    for i in range(1, len(nums) - 1):
        product_of_prefix[i] = product_of_prefix[i - 1] * nums[i]
        product_of_suffix[-i - 1] = product_of_suffix[-i] * nums[-i - 1]
    return [product_of_suffix[1]] \
           + [product_of_prefix[i - 1] * product_of_suffix[i + 1] for i in range(1, len(nums) - 1)] + \
           [product_of_prefix[-2]]


def test_corner_cases():
    assert productExceptSelf([1, 2]) == [2, 1]
    assert productExceptSelf([1, 2, 3]) == [6, 3, 2]
    assert productExceptSelf([1] * (10 ** 5)) == [1] * (10 ** 5)


def test_examples():
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
