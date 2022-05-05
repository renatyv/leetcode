def letterCasePermutation(s: str) -> list[str]:
    """
    Given a string s, you can transform every letter individually
    to be lowercase or uppercase to create another string.
    Return a list of all possible strings we could create. Return the output in any order.
    Idea: use recursion."""
    def recursive_permutations(lowcase: str):
        if len(lowcase) == 1:
            if lowcase[0].isalpha():
                return [lowcase, lowcase.upper()]
            else:
                return [lowcase]
        if lowcase[0].isalpha():
            return [lowcase[0]+perm for perm in recursive_permutations(lowcase[1:])] +\
                   [lowcase[0].upper()+perm for perm in recursive_permutations(lowcase[1:])]
        else:
            return [lowcase[0]+perm for perm in recursive_permutations(lowcase[1:])]
    return recursive_permutations(s.lower())


def equal_permuatations(list1, list2):
    return len(list1) == len(list2) \
           and all(x2 in list1 for x2 in list2) \
           and all(x1 in list2 for x1 in list1)


def test_example():
    assert equal_permuatations(letterCasePermutation('a1b2'),
                               ["a1b2", "a1B2", "A1b2", "A1B2"])
    assert equal_permuatations(letterCasePermutation('3z4'),
                               ["3z4","3Z4"])

def test_corner():
    assert equal_permuatations(letterCasePermutation('3'),
                               ['3'])
    assert equal_permuatations(letterCasePermutation('a'),
                               ['a','A'])
    assert equal_permuatations(letterCasePermutation('ab'),
                               ['ab', 'Ab','aB','AB'])
    assert equal_permuatations(letterCasePermutation('1234567890,.'),
                               ['1234567890,.'])
    assert len(letterCasePermutation('abcdefghijkl')) == 2**12
