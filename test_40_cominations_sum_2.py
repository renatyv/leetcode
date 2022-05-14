from collections import Counter


def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    """Given a collection of candidate numbers (candidates) and a target number (target),
    find all unique combinations in candidates where the candidate numbers sum to target.
    Each number in candidates may only be used once in the combination.

    Note: The solution set must not contain duplicate combinations.
    Ideas:
    1. Count number of distinct numbers in candidates
    2. use solution for problem using one less candidate number"""
    candidates_counter = Counter(candidates)
    candidates_keys = list(candidates_counter.keys())

    def recursive_solution(number_of_counter_keys: int, target: int):
        nonlocal candidates_counter
        if target == 0:
            return [[]]
        if number_of_counter_keys == 1:
            key = candidates_keys[0]
            if target % key == 0 and candidates_counter[key] >= (target // key):
                return [[key] * (target // key)]
            else:
                return []
        combinations_without_last_key = recursive_solution(number_of_counter_keys - 1, target)
        combinations_with_last_key = []
        key = candidates_keys[number_of_counter_keys - 1]
        key_count = candidates_counter[key]
        for num_keys in range(1, min(target // key, key_count) + 1):
            new_target = target - key * num_keys
            pre_combinations = recursive_solution(number_of_counter_keys - 1, new_target)
            for comb in pre_combinations:
                combinations_with_last_key.append(comb + ([key] * num_keys))
        return combinations_without_last_key + combinations_with_last_key

    return recursive_solution(len(candidates_keys), target)


def test_corner_cases():
    assert combinationSum2([1], 3) == []
    assert combinationSum2([1, 2], 3) == [[1, 2]]
    assert combinationSum2([1, 2, 3], 3) == [[1, 2], [3]]
    assert combinationSum2([1, 1], 2) == [[1, 1]]
    assert combinationSum2([1, 1], 1) == [[1]]
    assert combinationSum2([1, 1, 1], 2) == [[1, 1]]


def test_1():
    assert combinationSum2([1, 1, 2, 2], 4) == [[1, 1, 2], [2, 2]]


def test_examples():
    assert combinationSum2([10, 1, 2, 7, 6, 1, 5], 8) == [[1, 7], [1, 1, 6], [2, 6], [1, 2, 5]]
    assert combinationSum2([2, 5, 2, 1, 2], 5) == [[5], [2, 2, 1]]
