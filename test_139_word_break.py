def wordBreak(s: str, wordDict: list[str]) -> bool:
    """Given a string s and a dictionary of strings wordDict,
    return true if s can be segmented into a space-separated sequence of one or more dictionary words.
    Note that the same word in the dictionary may be reused multiple times in the segmentation.
    1 <= s.length <= 300
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 20
    Ideas: hashing + memoization
    1. Use set to hash words
    2. Do not check the same substring s[i:] twice.
    To do that, keep track of all substring starting indexes we checked for
    3. Iterate over all possible prefix lengths for s[i:] to check that they are in the word_set"""
    if len(s) == 0:
        return True
    # start symbol number, current word number
    word_set = set(wordDict)
    word_lengths: set[int] = {len(word) for word in wordDict}
    asc_sorted_w_lengths = list(sorted(word_lengths))
    starting_index_scheduled = [False] * (len(s)+1)
    starting_index_scheduled[0] = True
    stack = [0]
    while stack:
        start_symbol = stack.pop()
        if start_symbol == len(s):
            return True
        for prefix_len in asc_sorted_w_lengths:
            end = start_symbol+prefix_len
            if end <= len(s)\
                    and not starting_index_scheduled[end]\
                    and s[start_symbol:end] in word_set:
                stack.append(end)
                starting_index_scheduled[end] = True
    return False


def test_examples():
    assert wordBreak("leetcode", ["leet", "code"])
    assert wordBreak(s="applepenapple", wordDict=["apple", "pen"])
    assert not wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])


def test_corner():
    assert wordBreak("a", ["a"])
    assert wordBreak("aa", ["a"])
    assert wordBreak("aaa", ["a"])
    assert wordBreak("aaaaaaab", ["a","ab"])
    assert wordBreak("ab", ["ab"])
    assert wordBreak("aab",["a","aab"])
    assert wordBreak("abab", ["ab"])
    assert wordBreak("ab", ["a", "b"])
    assert wordBreak("ab", ["b", "a"])
    assert wordBreak("abc", ["a", "b", "c"])
    assert wordBreak("abc", ["a", "b", "c"])
    assert wordBreak("aabc", ["a", "b", "c"])
    assert wordBreak("aabc", ["a", "b", "c"])
    assert not wordBreak("a", ["b"])
    assert not wordBreak("a", ["b", "c"])
    assert not wordBreak("abcd", ["efg", "bcd"])
    assert not wordBreak("abc", ["a","b"])
