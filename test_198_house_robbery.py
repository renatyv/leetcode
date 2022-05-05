def rob(nums: list[int]) -> int:
    """
    You are a professional robber planning to rob houses along a street.
    Each house has a certain amount of money stashed,
    the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
    and it will automatically contact the police if two adjacent houses were broken into on the same night.
    Given an integer array nums representing the amount of money of each house,
    return the maximum amount of money you can rob tonight without alerting the police.

    Idea:  compute and save max cumulative reward if we rob house #n
    and use that to compute #(n+1)
    """
    if len(nums)<3:
        return max(nums)
    rob_n_max_reward: list[int] = [0, 0] # dummie data
    for ith_reward in nums:
        # don't rob current house or rob current and skip previous
        rob_n_max_reward.append(max(rob_n_max_reward[-1], rob_n_max_reward[-2]+ith_reward))
    return rob_n_max_reward[-1]


def test_rob():
    assert rob([1,2,3,1]) == 4
    assert rob([2,7,9,3,1]) == 12
    assert rob([2,1,1,2]) == 4

