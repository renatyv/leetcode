def moveZeroes(nums: list[int]) -> None:
    """Idea: user number of encountered zeros to compute index for the next non-zero element"""
    if len(nums) <= 1:
        return
    num_zeros = 0
    # move non-zero elements
    for i, num in enumerate(nums):
        if num == 0:
            num_zeros += 1
            continue
        nums[i-num_zeros] = num
    # fill what's left with zeroes
    for i in range(num_zeros):
        nums[-i-1] = 0
    return


def test_move_zeroes_examples():
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    assert nums == [1,3,12,0,0]
    nums = [0]
    moveZeroes(nums)
    assert nums == [0]


def test_move_zeroes_1():
    nums = [1]
    moveZeroes(nums)
    assert nums == [1]
    nums = [0,1,2,3]
    moveZeroes(nums)
    assert nums == [1,2,3,0]
    nums = [1, 2, 0, 3]
    moveZeroes(nums)
    assert nums == [1, 2, 3, 0]
