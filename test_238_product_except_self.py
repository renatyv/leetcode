def productExceptSelf(nums: list[int]) -> list[int]:
    """Given an integer array nums, return an array answer such that answer[i] is equal to
    the product of all the elements of nums except nums[i].
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
    You must write an algorithm that runs in O(n) time and without using the division operation."""
    result = [1] * len(nums)
    prefix_product = 1
    suffix_product = 1

    for index in range(len(nums)):
        result[index] *= prefix_product
        result[-1 - index] *= suffix_product
        prefix_product *= nums[index]
        suffix_product *= nums[-1 - index]

    return result


def test_corner_cases():
    assert productExceptSelf([1, 2]) == [2, 1]
    assert productExceptSelf([1, 2, 3]) == [6, 3, 2]
    assert productExceptSelf([1] * (10 ** 5)) == [1] * (10 ** 5)


def test_examples():
    assert productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
