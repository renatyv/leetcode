from functools import cache


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
    words_set = set(wordDict)

    @cache
    def recursive(start_index: int) -> bool:
        nonlocal words_set
        nonlocal s
        if start_index == len(s):
            return True
        for word in words_set:
            if s.startswith(word, start_index):
                if recursive(start_index + len(word)):
                    return True
        return False

    return recursive(0)


def test_examples():
    assert wordBreak("leetcode", ["leet", "code"])
    assert wordBreak(s="applepenapple", wordDict=["apple", "pen"])
    assert not wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])


def test_corner():
    assert wordBreak("a", ["a"])
    assert wordBreak("aa", ["a"])
    assert wordBreak("aaa", ["a"])
    assert wordBreak("aaaaaaab", ["a", "ab"])
    assert wordBreak("ab", ["ab"])
    assert wordBreak("aab", ["a", "aab"])
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
    assert not wordBreak("abc", ["a", "b"])
