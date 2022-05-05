def all_possible_insertions(elem, into_list):
    resulting_list = []
    len_word = len(into_list[0])
    for insert_position in range(len_word + 1):
        inserted = [perm[0:insert_position] + [elem] + perm[insert_position:] for perm in into_list]
        resulting_list += inserted
    return resulting_list


def permute(nums: list[int]) -> list[list[int]]:
    """Given an array nums of distinct integers, return all the possible permutations.
    You can return the answer in any order.

    Idea: use recursion."""
    if len(nums) == 1:
        return [nums]
    if len(nums) == 2:
        return [nums, nums[::-1]]
    prev_perms = permute(nums[1:])
    return all_possible_insertions(nums[0], prev_perms)


def equal_permuatations(list1, list2):
    return len(list1) == len(list2) \
           and all(x2 in list1 for x2 in list2) \
           and all(x1 in list2 for x1 in list1)


def test_examples():
    # assert [[1]] == permute([1])
    # assert equal_permuatations(permute([0, 1]),
                               # [[0, 1], [1, 0]])
    # assert equal_permuatations(permute([1,2,3]),
    #                            [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    assert equal_permuatations(permute([1,2,3,4]),
                               [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2],
                                [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1],
                                [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1],
                                [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]])
