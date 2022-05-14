def permuteUnique(nums: list[int]) -> list[list[int]]:
    """Given a collection of numbers, nums, that might contain duplicates,
    return all possible unique permutations in any order.
    1 <= nums.length <= 8
    -10 <= nums[i] <= 10"""
    def permuteSorted(s: str) -> set[str]:
        if len(s) == 1:
            return {s}
        prev_permutations = permuteSorted(s[:-1])
        add_element = s[-1]
        resulting_permutations = set()
        for permutation in prev_permutations:
            for insert_position in range(len(permutation)):
                # skip repeating elements
                if add_element != permutation[insert_position]:
                    resulting_permutations.add(permutation[:insert_position]+add_element+permutation[insert_position:])
            resulting_permutations.add(permutation+add_element)
        return resulting_permutations

    s = ''.join(chr(ord('a') + 10 + num) for num in nums)
    permutations: set[str] = permuteSorted(s)
    resulting_perms = []
    for s in permutations:
        resulting_perms.append([ord(char)-ord('a')-10 for char in s])
    return resulting_perms


def compare_permutations(permutations1, permutations2):
    def nums_to_str(nums):
        return ''.join(chr(ord('a') + 10 + num) for num in nums)
    set1 = {nums_to_str(perm) for perm in permutations1}
    set2 = {nums_to_str(perm) for perm in permutations2}
    return set1 == set2


def test_examples():
    assert compare_permutations(permuteUnique([1,1,2]), [[2,1,1],[1,2,1],[1,1,2]])
    assert compare_permutations(permuteUnique([1,2,3]), [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]])


def test_corner_cases():
    assert permuteUnique([1]) == [[1]]
    assert permuteUnique([1,1]) == [[1,1]]
    assert permuteUnique([1, 1, 1, 1]) == [[1, 1, 1, 1]]


def test_cases_2():
    assert permuteUnique([1, 1]) == [[1, 1]]
    assert compare_permutations(permuteUnique([1, 2]), [[2, 1],[1, 2]])


def test_cases_3():
    assert permuteUnique([1,1,1]) == [[1,1,1]]
    assert compare_permutations(permuteUnique([2, 1, 1]), [[2,1,1],[1,2,1],[1,1,2]])
    assert compare_permutations(permuteUnique([3, 1, 2]), [[3, 2, 1], [2, 3, 1], [2, 1, 3], [3, 1, 2], [1, 3, 2], [1, 2, 3]])


def test_cases_4():
    assert compare_permutations(permuteUnique([1,1,2,2]), [[2,2,1,1],[1,2,2,1],[1,1,2,2],[1,2,1,2],[2,1,2,1],[2,1,1,2]])
