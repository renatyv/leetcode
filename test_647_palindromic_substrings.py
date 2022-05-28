def countSubstrings(s: str) -> int:
    """Given a string s, return the number of palindromic substrings in it.
    A string is a palindrome when it reads the same backward as forward.
    A substring is a contiguous sequence of characters within the string.
    Idea: expand palindromes around all possible centers"""

    def expand_around_center(s: str, left: int, right: int) -> int:
        """:returns number of substrings with center at left <= right"""
        n_palindromic_ss = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            n_palindromic_ss += 1
            left -= 1
            right += 1
        return n_palindromic_ss

    if len(s) == 1:
        return 1
    n_palindromic_ss = 0
    for i in range(1, len(s)):
        n_palindromic_ss += expand_around_center(s=s, left=i - 1, right=i - 1)
        n_palindromic_ss += expand_around_center(s=s, left=i - 1, right=i)
    # last symbol s[-1] was not taken into account as a palindrome
    n_palindromic_ss += 1
    return n_palindromic_ss


def test_corner_cases():
    assert countSubstrings('s') == 1
    assert countSubstrings('ss') == 3
    assert countSubstrings('aba') == 4
    assert countSubstrings('cabac') == 5 + 1 + 1
    assert countSubstrings('cd') == 2
    assert countSubstrings('cde') == 3
    assert countSubstrings('cdef') == 4
    assert countSubstrings('abba') == 4 + 2


def test_examples():
    assert countSubstrings('abc') == 3
    assert countSubstrings('aaa') == 6
