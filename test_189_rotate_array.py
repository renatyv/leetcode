import math


def rotate(nums: list[int], k: int) -> None:
    """
    Given an array, rotate the array to the right by k steps, where k is non-negative.

    Do not return anything, modify nums in-place instead.
    Use less memory
    https://www.geeksforgeeks.org/array-rotation/
    Idea: Move each element by math.gcd(k, n) several times (just before the cycle ends)
    """
    n = len(nums)
    # k could be larger than nums length, or negative.
    shift = -k % n
    for cycle_start_index in range(math.gcd(k, n)):
        cycle_first_val = nums[cycle_start_index]
        save_to_index = cycle_start_index
        next_index = (save_to_index + shift) % n
        # rotate the full cycle
        while next_index != cycle_start_index:
            nums[save_to_index] = nums[next_index]
            save_to_index = next_index
            next_index = (save_to_index + shift) % n
        nums[save_to_index] = cycle_first_val
    return


# nums = [0,1,2,3,4,5,6], k=2
# rotated = [5,6,0,1,2,3,4]
# rotated[0] = nums[5]
# rotated[2] = nums[0]
# rotated[4] = nums[2]
# rotated[6] = nums[4]
# rotated[1] = nums[6]
# rotated[3] = nums[1]
# rotated[5] = nums[3]
def test_rotate_example_1():
    test_array = [0,1,2,3,4,5,6]
    rotate(test_array, 2)
    assert test_array == [5,6,0,1,2,3,4]



# nums = [0,1,2,3], k=2
# rotated = [2,3,1,2]
# rotated[0] = nums[3]
# rotated[3] = nums[0]
# rotated[4] = nums[2]
# rotated[6] = nums[4]
def test_rotate_example_2():
    test_array = [-1,-100,3,99]
    rotate(test_array,2)
    assert test_array == [3,99,-1,-100]


def test_rotate_example_large_k():
    test_array = [1,2]
    rotate(test_array,3)
    assert test_array == [2,1]


def test_rotate_example_negative_k():
    test_array = [1, 2]
    rotate(test_array, -3)
    assert test_array == [2, 1]
