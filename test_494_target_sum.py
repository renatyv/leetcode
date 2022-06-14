from functools import cache


def findTargetSumWays(nums: list[int], target: int) -> int:
    """You are given an integer array nums and an integer target.
    You want to build an expression out of nums by adding one of the symbols
     '+' and '-' before each integer in nums and then concatenate all the integers.

    1 <= nums.length <= 20
    0 <= nums[i] <= 1000
    0 <= sum(nums[i]) <= 1000
    -1000 <= target <= 1000
    Idea: use recursion over nums + cache
    """

    @cache
    def recursive_sol(nums_index: int, local_target: int) -> int:
        if nums_index == len(nums) - 1:
            if nums[nums_index] == 0 and local_target == 0:
                return 2
            return 1 if (nums[nums_index] == local_target or nums[nums_index] == -local_target) else 0
        return recursive_sol(nums_index + 1, local_target - nums[nums_index]) \
               + recursive_sol(nums_index + 1, local_target + nums[nums_index])

    return recursive_sol(0, target)


def test_edge_cases():
    assert findTargetSumWays([1], 1) == 1
    assert findTargetSumWays([1], 2) == 0
    assert findTargetSumWays([1, 2], 3) == 1
    assert findTargetSumWays([1, 1], 1) == 0
    assert findTargetSumWays([1, 1], 2) == 1
    assert findTargetSumWays([1, 2], 2) == 0
    assert findTargetSumWays([1, 2], 1) == 1
    assert findTargetSumWays([1, 2], -1) == 1
    assert findTargetSumWays([1, 2], 3) == 1
    assert findTargetSumWays([1, 1, 1], 3) == 1
    assert findTargetSumWays([1, 1], 0) == 2  # -1,1; 1,-1
    assert findTargetSumWays([1, 1, 1], 0) == 0
    assert findTargetSumWays([1, 1, 1], 1) == 3  # 1,-1,1; 1,1,-1; -1,1,1
    assert findTargetSumWays([1,0],1) == 2


def test_examples():
    assert findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
    assert findTargetSumWays([1], 1) == 1
