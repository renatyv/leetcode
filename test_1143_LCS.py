def longestCommonSubsequence(text1: str, text2: str) -> int:
    """Given two strings text1 and text2, return the length of their longest common subsequence.
    If there is no common subsequence, return 0.
    A subsequence of a string is a new string generated from the original string with some characters
    (can be none) deleted without changing the relative order of the remaining characters.
    Idea: 2d dynamic programming
    1) LCS(s1+X,s2+X) = LCS(s1,s2)+X
    2) LCS(s1+Y,s2+Y) = max(LCS(s1, s2+Y), LCS(s1+X,s2))"""
    lcs_array: list[list[str]] = [[''] * (len(text1)+1) for row in range(len(text2)+1)]
    for t2 in range(1, len(text2)+1): # iterate over rows
        for t1 in range(1, len(text1)+1): # iterate over columns
            if text1[t1-1] == text2[t2-1]:
                lcs_array[t2][t1] = lcs_array[t2-1][t1-1] + text1[t1-1]
            else:
                if len(lcs_array[t2-1][t1]) > len(lcs_array[t2][t1-1]):
                    lcs_array[t2][t1] = lcs_array[t2-1][t1]
                else:
                    lcs_array[t2][t1] = lcs_array[t2][t1-1]
    return len(lcs_array[len(text2)][len(text1)])


def test_corner_cases():
    assert longestCommonSubsequence('a','a') == len('a')
    assert longestCommonSubsequence('ab', 'ab') == len('ab')
    assert longestCommonSubsequence('acb', 'ab') == len('ab')


def test_examples():
    assert longestCommonSubsequence(text1 = "abcde", text2 = "ace" ) == len('ace')
    assert longestCommonSubsequence(text1 = "abc", text2 = "abc") == len('abc')
    assert longestCommonSubsequence(text1 = "abc", text2 = "def") == len('')
