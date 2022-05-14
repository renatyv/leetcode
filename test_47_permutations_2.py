from collections import Counter


def permuteUnique(nums: list[int]) -> list[list[int]]:
    """Given a collection of numbers, nums, that might contain duplicates,
    return all possible unique permutations in any order.
    1 <= nums.length <= 8
    -10 <= nums[i] <= 10
    Idea: DFS + backtracking. """
    if len(nums) == 1:
        return [nums]

    def generate_permutations(current_prefix: list[int],
                              nums_counter: dict[int, int],
                              required_length: int):
        if len(current_prefix) == required_length:
            yield current_prefix.copy()
            return
        for num in nums_counter:
            if nums_counter[num] > 0:
                nums_counter[num] -= 1
                current_prefix.append(num)
                for perm in generate_permutations(current_prefix,
                                                  nums_counter,
                                                  required_length):
                    yield perm
                nums_counter[num] += 1
                current_prefix.pop()

    nums_count = Counter(nums)
    return list(generate_permutations([], nums_count, len(nums)))


def compare_permutations(permutations1, permutations2):
    def nums_to_str(nums):
        return ''.join(chr(ord('a') + 10 + num) for num in nums)

    set1 = {nums_to_str(perm) for perm in permutations1}
    set2 = {nums_to_str(perm) for perm in permutations2}
    return set1 == set2


def test_examples():
    assert compare_permutations(permuteUnique([1, 1, 2]), [[2, 1, 1], [1, 2, 1], [1, 1, 2]])
    assert compare_permutations(permuteUnique([1, 2, 3]),
                                [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]])


def test_corner_cases():
    assert permuteUnique([1]) == [[1]]
    assert permuteUnique([1, 1]) == [[1, 1]]
    assert permuteUnique([1, 1, 1, 1]) == [[1, 1, 1, 1]]


def test_cases_2():
    assert permuteUnique([1, 1]) == [[1, 1]]
    assert compare_permutations(permuteUnique([1, 2]), [[2, 1], [1, 2]])


def test_cases_3():
    assert permuteUnique([1, 1, 1]) == [[1, 1, 1]]
    assert compare_permutations(permuteUnique([2, 1, 1]), [[2, 1, 1], [1, 2, 1], [1, 1, 2]])
    assert compare_permutations(permuteUnique([3, 1, 2]),
                                [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]])


def test_cases_4():
    assert compare_permutations(permuteUnique([1, 1, 2, 2]),
                                [[2, 2, 1, 1], [1, 2, 2, 1], [1, 1, 2, 2], [1, 2, 1, 2], [2, 1, 2, 1], [2, 1, 1, 2]])
