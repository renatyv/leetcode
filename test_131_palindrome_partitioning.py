from functools import cache


@cache
def partition(s: str) -> list[list[str]]:
    """Given a string s,
    partition s such that every substring of the partition is a palindrome.
    Return all possible palindrome partitioning of s.
    A palindrome string is a string that reads the same backward as forward.
    Idea: if suffix s[k:] is palindrom, then re-use partition for prefix s[:k]"""

    def is_palindrome(s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    if len(s) == 0:
        return [[]]
    partitions = []
    for suffix_len in range(1, len(s) + 1):
        suffix = s[-suffix_len:]
        prefix = s[:-suffix_len]
        if is_palindrome(suffix):
            partitions += [prefix_partition + [suffix] for prefix_partition in partition(prefix)]
    return partitions


def test_corner_cases():
    assert partition('a') == [['a']]
    assert partition('ab') == [['a', 'b']]
    assert partition('aa') == [['a', 'a'], ['aa']]
    assert partition('aba') == [['a', 'b', 'a'], ['aba']]
    assert partition('caba') == [['c', 'a', 'b', 'a'], ['c', 'aba']]
    assert partition('baab') == [['b', 'a', 'a', 'b'], ['b', 'aa', 'b'], ['baab']]
    assert partition('cabac') == [['c', 'a', 'b', 'a', 'c'], ['c', 'aba', 'c'], ['cabac']]


def test_examples():
    assert partition('aab') == [["a", "a", "b"], ["aa", "b"]]
    assert partition("a") == [["a"]]
