def missingNumber(nums: list[int]) -> int:
    """Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.
    Idea: 1) sum(nums) + x == sum(range)
    x = sum(range) - sum(nums) = sum(range-nums)
    2) To protect from overflow, compute sum(nums)-sum(range) element-by element"""
    current_sum = 0
    for i in range(len(nums)):
        current_sum += i - nums[i]
    # add largest elemnt
    current_sum += len(nums)
    return current_sum


def test_examples():
    assert missingNumber([0, 1]) == 2
    assert missingNumber([0, 1, 3]) == 2
    assert missingNumber([0, 2, 3]) == 1
    assert missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
