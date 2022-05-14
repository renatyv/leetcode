from functools import cache
from copy import deepcopy


def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    """Given an array of distinct integers candidates and a target integer target,
    return a list of all unique combinations of candidates where the chosen numbers sum to target.
    You may return the combinations in any order.

    The same number may be chosen from candidates an unlimited number of times.
    Two combinations are unique if the frequency of at least one of the chosen numbers is different.
    It is guaranteed that the number of unique combinations that sum up to target
    is less than 150 combinations for the given input.

    1 <= candidates.length <= 30
    1 <= candidates[i] <= 200
    All elements of candidates are distinct.
    1 <= target <= 500

    Idea: combinations = combinationSum(candidates[:-1], target)
        + combinationSum(candidates[:-1], target-candidates[-1])
        + ...
    """
    def recursive_combinations(number_of_used_candidates: int, target: int) -> list[list[int]]:
        if target <= 0 or number_of_used_candidates <= 0:
            return []
        if number_of_used_candidates == 1:
            num = candidates[0]
            if target % num == 0:
                return [[num] * (target // num)]
            else:
                return []
        num = candidates[number_of_used_candidates - 1]
        combinations = recursive_combinations(number_of_used_candidates - 1, target)
        count_num = 1
        while target - num * count_num >= 0:
            new_target = target - num * count_num
            if new_target == 0:
                combinations.append([num] * count_num)
            else:
                pre_combinations = recursive_combinations(number_of_used_candidates - 1,
                                                          new_target)
                for comb in pre_combinations:
                    combinations.append(comb + [num] * count_num)
            count_num += 1
        return combinations

    return recursive_combinations(len(candidates), target)


def test_examples():
    assert combinationSum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert combinationSum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert combinationSum([2], 1) == []


def corner_cases():
    assert combinationSum([1], 2) == []
    assert combinationSum([1], 1) == [[1]]
    assert combinationSum([1], 2) == [[1, 1]]
    assert combinationSum([1, 2, 3], 4) == []


def test_cases_2():
    assert combinationSum([3, 4], 2) == []
    assert combinationSum([1, 2], 3) == [[1, 1, 1], [1, 2]]
    assert combinationSum([1, 3], 2) == [[1, 1]]


def test_cases_3():
    assert combinationSum([1], 3) == [[1, 1, 1]]
    assert combinationSum([1, 2], 3) == [[1, 1, 1], [1, 2]]
    assert combinationSum([1, 2], 4) == [[1, 1, 1, 1], [1, 1, 2], [2, 2]]
    assert combinationSum([1, 2, 3], 3) == [[1, 1, 1], [1, 2], [3]]


def test_wa_0():
    assert combinationSum([6, 3, 5], 6) == [[6], [3, 3]]
    assert combinationSum([6, 3], 6) == [[6], [3, 3]]


def test_wa_1():
    assert len(combinationSum([6, 3, 5, 1], 9)) == 8
