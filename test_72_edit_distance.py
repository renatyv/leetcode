def minDistance(word1: str, word2: str) -> int:
    """Given two strings word1 and word2,
    return the minimum number of operations required to convert word1 to word2.
    You have the following three operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character:
    Idea: use modify Longest Common Subsequence algorithm. Save
    len(w1) == 0 => lev = len(w2)
    len(w2) == 0 => lev = len(w1)
    w1[-1] == w2[-1] => lev = lev(w1, w2)
    lev = min(
            lev(w1[:-1], w2) + 1, --- deletion from w1
            lev(w1, w2[:-1]) + 1, --- insertion into w1
            lev(w1[:-1], w2[:-1]) + 1) --- substitution
    dist =
    number of replacements = min(len(w1), len(w2)) - LCS(w1,w2) -
    number of insertions(deletions) = abs(len(w1)-len(w2))"""
    # Can be optimized: we only need two elements from previous row and one from previous column
    subproblems = [[0] * (len(word1) + 1) for w in range(len(word2) + 1)]
    # number of columns = len(word1)
    # number of rows = len(word2)
    for row in range(len(word2) + 1):
        for col in range(len(word1) + 1):
            # init zeroth column
            if row == 0:
                subproblems[row][col] = col
                continue
            # init zeroth row
            if col == 0:
                subproblems[row][col] = row
                continue
            # last char is the same, so we don't need to do anything
            if word1[col - 1] == word2[row - 1]:
                subproblems[row][col] = subproblems[row - 1][col - 1]
                continue
            subproblems[row][col] = min(
                subproblems[row - 1][col] + 1,  # deletion
                subproblems[row][col - 1] + 1,  # insertion
                subproblems[row - 1][col - 1] + 1  # substitution
            )
    return subproblems[-1][-1]


def test_edge_cases():
    assert minDistance('a', 'a') == 0
    assert minDistance('a', 'b') == 1
    assert minDistance('b', 'a') == 1
    assert minDistance('', '') == 0
    assert minDistance('a', '') == 1
    assert minDistance('', 'a') == 1
    assert minDistance('abc', 'adc') == 1
    assert minDistance('abc', 'adc') == 1


def test_examples():
    assert minDistance('horse', 'ros') == 3
    assert minDistance('intention', 'execution') == 5
