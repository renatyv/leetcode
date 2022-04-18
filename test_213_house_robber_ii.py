def rob(nums: list[int]) -> int:
    """houses are in circle
    Idea: Both first and last houses can not be robbed the same night.
    Try not taking into account first house, then try not taking into account last house. Find the maximum between them."""
    def rob_in_line(nums: list[int]) -> int:
        """houses are in line. Idea: cumulitive reward for house n if we rob it  = cumulitive reward for house (n-2) + reward for house n.
            If we don't rob it, cumulitive reward is the same as for house n-1
            :returns max profit"""
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        cum_reward: list[int] = [0, 0]
        for i, reward_n in enumerate(nums):
            cum_reward.append(max(cum_reward[-1], cum_reward[-2]+reward_n))
        return cum_reward[-1]
    if not nums:
        return 0
    if len(nums) <= 2:
        return max(nums)
    cum_rewards_without_first = rob_in_line(nums[1:])
    cum_rewards_without_last = rob_in_line(nums[:-1])
    return max(cum_rewards_without_first, cum_rewards_without_last)


def test_rob_example_1():
    assert rob([2,3,2]) == 3


def test_rob_example_2():
    assert rob([1,2,3,1]) == 4


def test_rob_example_3():
    assert rob([1,2,3]) == 3


def test_not_rob_last():
    assert rob([]) == 0


def test_various():
    assert rob([1, 2, 3, 4]) == 6
    assert rob([1, 2, 3, 3]) == 5
    assert rob([4, 2, 3, 4, 4]) == 8
    assert rob([1, 2, 3, 4, 1]) == 6
    assert rob([5, 1, 1, 1, 5]) == 6
