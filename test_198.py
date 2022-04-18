def rob(nums: list[int]) -> int:
    """
    Idea:  compute and save max cumulative reward if we rob house #n
    and use that to compute next one
    """
    if len(nums)<3:
        return max(nums)
    rob_n_max_reward: list[int] = [0, 0] # dummie data
    for ith_reward in nums:
        # we eithter rob hob previous house and not current, skip
        rob_n_max_reward.append(max(rob_n_max_reward[-1], rob_n_max_reward[-2]+ith_reward))
    return rob_n_max_reward[-1]


def test_rob():
    assert rob([1,2,3,1]) == 4
    assert rob([2,7,9,3,1]) == 12
    assert rob([2,1,1,2]) == 4

