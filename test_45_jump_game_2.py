def jump(nums: list[int]) -> int:
    """Idea: n_jumps_to_reach[i] = number of jumps necessary to reach step i
    if nums[i]=k, then we need at most n_jumps_to_reach[i]+1 steps to reach every step i...i+k"""
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        return 1
    n_jumps_to_reach = [10**5] * len(nums)
    n_jumps_to_reach[0] = 0
    for cur_step, jump_size in enumerate(nums):
        max_step = min(cur_step+jump_size, len(nums)-1)
        for next_step in range(cur_step+1, max_step + 1):
            n_jumps_to_reach[next_step] = min(n_jumps_to_reach[cur_step]+1,
                                              n_jumps_to_reach[next_step])
    return n_jumps_to_reach[-1]


def test_jump_example_1():
    assert jump([2,3,1,1,4]) == 2
    assert jump([2,3,0,1,4]) == 2


def test_jump_1():
    assert jump([1,1,1,1]) == 3
    assert jump([1, 1, 1, 3]) == 3
    assert jump([1, 2, 1, 1]) == 2
    assert jump([3, 1, 3, 1, 1, 1]) == 2

