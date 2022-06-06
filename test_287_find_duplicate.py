def findDuplicate(nums: list[int]) -> int:
    """Idea:
    1) use array as a map
    2) duplicates lead to cycles
    3) fast & slow pointers to find cycle
    """
    # search for intersection point, cycle
    slow_pointer = nums[0]
    fast_pointer = nums[0]
    while True:
        slow_pointer = nums[slow_pointer]
        fast_pointer = nums[nums[fast_pointer]]
        if slow_pointer == fast_pointer:
            break
    # Find the "entrance" to the cycle.
    slow_pointer = nums[0]
    while slow_pointer != fast_pointer:
        slow_pointer = nums[slow_pointer]
        fast_pointer = nums[fast_pointer]
    return fast_pointer


def test_examples():
    assert findDuplicate([1, 1]) == 1
    assert findDuplicate([2, 2, 2]) == 2
    assert findDuplicate([3, 1, 3, 4, 2]) == 3
