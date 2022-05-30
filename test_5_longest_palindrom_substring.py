def longestPalindrome(s: str) -> str:
    """Given a string s, return the longest palindromic substring in s.

    Idea: expand around center"""
    def even_palindrome_len(center_index: int, s: str):
        """for palindrome 'bb' center index is 1, half_len = 1"""
        # actual computation
        half_len = 1
        while center_index - half_len + 1 >= 0 and \
                center_index + half_len < len(s) and \
                s[center_index - half_len + 1] == s[center_index + half_len]:
            half_len += 1
        return 2 * (half_len - 1)

    def odd_palindrome_len(center_index: int, s: str):
        """for palindrome 'bab' center index is 1, half_len = 1"""
        half_len = 0
        while center_index - half_len >= 0 and \
                center_index + half_len < len(s) and \
                s[center_index - half_len] == s[center_index + half_len]:
            half_len += 1
        return 2 * (half_len - 1) + 1

    if len(s) == 1:
        return s[0]
    max_palindrome = s[0]
    max_pal_len = 0
    # look for longest odd palindrome
    center_index = max_pal_len // 2 - 1
    while True:
        center_index += 1
        if max_pal_len % 2 == 0:
            next_half_len = max_pal_len // 2
        else:
            next_half_len = (max_pal_len // 2) + 1
        if center_index - next_half_len < 0:
            continue
        if center_index + next_half_len >= len(s):
            break
        if s[center_index - next_half_len] != s[center_index + next_half_len]:
            continue
        o_p_len = odd_palindrome_len(center_index, s)
        if o_p_len > max_pal_len:
            max_pal_len = o_p_len
            max_palindrome = s[center_index - (o_p_len // 2):center_index + o_p_len // 2 + 1]
    # look for longest even palindrome
    center_index = max_pal_len // 2 - 1
    while True:
        center_index += 1
        next_half_len = max_pal_len // 2 + 1
        if center_index - next_half_len + 1 < 0:
            continue
        if center_index + next_half_len >= len(s):
            break
        if s[center_index - next_half_len + 1] != s[center_index + next_half_len]:
            continue
        e_p_len = even_palindrome_len(center_index, s)
        if e_p_len > max_pal_len:
            max_pal_len = e_p_len
            max_palindrome = s[center_index - (e_p_len // 2) + 1:center_index + e_p_len // 2 + 1]
    return max_palindrome


def test_edge_cases():
    assert longestPalindrome('a') == 'a'
    assert longestPalindrome('ab') == 'a'
    assert longestPalindrome('aa') == 'aa'
    assert longestPalindrome('aaa') == 'aaa'
    assert longestPalindrome('baa') == 'aa'
    assert longestPalindrome('aab') == 'aa'


def test_examples():
    assert longestPalindrome("babad") == "bab"
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("abadd") == "aba"


def test_cases():
    assert longestPalindrome('baab') == 'baab'
    assert longestPalindrome("abadd") == "aba"
    assert longestPalindrome('abcbb') == 'bcb'
    assert longestPalindrome('bbabc') == 'bab'
    assert longestPalindrome('aaaaaaa') == 'aaaaaaa'
    assert longestPalindrome('aaaaaaaa') == 'aaaaaaaa'
    assert longestPalindrome('baaaaaaaac') == 'aaaaaaaa'
    assert longestPalindrome('baaaaaaaa') == 'aaaaaaaa'
    assert longestPalindrome('aaaaaaaab') == 'aaaaaaaa'
    assert longestPalindrome('aaaaaaaaab') == 'aaaaaaaaa'
    assert longestPalindrome('baaaaaaaaa') == 'aaaaaaaaa'
    assert longestPalindrome('baaaaaaaaac') == 'aaaaaaaaa'
    assert longestPalindrome('baaaaaaaaab') == 'baaaaaaaaab'
    assert longestPalindrome('cbaab') == 'baab'
    assert longestPalindrome('baabc') == 'baab'
    assert longestPalindrome('ababa') == 'ababa'
    assert longestPalindrome('ababac') == 'ababa'
    assert longestPalindrome('cababa') == 'ababa'
    assert longestPalindrome('cababad') == 'ababa'
    assert longestPalindrome('cababadab') == 'ababa'
    assert longestPalindrome('cabababababababab') == 'abababababababa'
