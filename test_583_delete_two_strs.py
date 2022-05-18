def minDistance(word1: str, word2: str) -> int:
    """Given two strings word1 and word2, return the minimum number of steps
     required to make word1 and word2 the same.
     In one step, you can delete exactly one character in either string.
     Idea: use Longest Common Subsequence
     aswer = len(word1)-len(lcs) + len(word2)-lcs"""

    def LCS(w1: str, w2: str) -> str:
        """longest common subsequence
        Dynamic programming.
        1) lcs(w1+X,w2+X) = lcs(w1,w2) + X
        2) lcs(w1+X,w2+Y) = max(lcs(w1+X,w2), lcs(w1, w2+Y)
        lcs[0][:] = ''
        lcs[:][0] = ''
        lcs[row][col] = LCS(w1[:row-1],w2[:row-1])
        note, that we only need previous row and previous column
        """
        prev_row = [''] * (len(w1) + 1)
        for row in range(1, len(w2) + 1):
            cur_row = [''] * (len(w1) + 1)
            prev_col = ''
            for col in range(1, len(w1) + 1):
                if w1[col - 1] == w2[row - 1]:
                    cur_row[col] = prev_row[col - 1] + w1[col - 1]
                else:
                    if len(prev_row[col]) > len(prev_col):
                        cur_row[col] = prev_row[col]
                    else:
                        cur_row[col] = prev_col
                prev_col = cur_row[col]
            prev_row = cur_row
        return prev_row[-1]

    lcs = LCS(word1, word2)
    return len(word1) + len(word2) - 2 * len(lcs)


def test_examples():
    assert minDistance(word1="sea", word2="eat") == 2
    assert minDistance(word1="leetcode", word2="etco") == 4


def test_corner_cases():
    assert minDistance('a', 'a') == 0
    assert minDistance('ab', 'ab') == 0
    assert minDistance('a', 'b') == 2
    assert minDistance('ab', 'a') == 1
    assert minDistance('a', 'ab') == 1
