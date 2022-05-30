def searchRange(nums: list[int], target: int) -> list[int]:
    """Given an array of integers nums sorted in non-decreasing order,
    find the starting and ending position of a given target value.
    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.
    Idea: binary search"""
    if len(nums) == 0:
        return [-1, -1]
    def find_first_target_index(nums: list[int], target: int) -> int:
        """Idea: binary search."""
        if nums[0] == target:
            return 0
        start_index, end_index = 0, len(nums) - 1
        while start_index + 1 < end_index:
            pivot = start_index + (end_index - start_index) // 2
            if nums[pivot] < target:
                start_index = pivot
            else:
                end_index = pivot
        if nums[end_index] != target:
            return -1
        return end_index
    def find_last_target_index(nums: list[int], target: int) -> int:
        """Idea: binary search."""
        if nums[-1] == target:
            return len(nums)-1
        start_index, end_index = 0, len(nums) - 1
        while start_index+1 < end_index:
            pivot = start_index + (end_index - start_index) // 2
            if nums[pivot] <= target:
                start_index = pivot
            else:
                end_index = pivot
        if nums[start_index] != target:
            return -1
        return start_index
    return [find_first_target_index(nums, target), find_last_target_index(nums, target)]


def test_examples():
    assert searchRange([5,7,7,8,8,10],8) == [3,4]
    assert searchRange([5,7,7,8,8,10],6) == [-1,-1]
    assert searchRange([],0) == [-1,-1]


def test_edge_cases():
    assert searchRange([0,0], 0) == [0, 1]
    assert searchRange([1], 0) == [-1, -1]
    assert searchRange([0,1,2,0],0) == [0,3]
