def search(nums: list[int], target: int) -> int:
    """
    Given an array of integers nums which is sorted in ascending order, and an integer target,
    write a function to search target in nums.
    If target exists, then return its index. Otherwise, return -1.

    Idea: binary search
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1


def test_example():
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1,0,3,5,9,12], 2) == -1
