def findAnagrams(s: str, p: str) -> list[int]:
    """Given two strings s and p, return an array of all the start indices of p's anagrams in s.
    You may return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    Idea: count number of each symbol in anacgram using dict.
    """
    if len(p) > len(s):
        return []
    if len(s) == 1:
        return [0] if s == p else []
    # initialize
    # differnce[char] == 0 means equal number of symbols 'char' in current substring of s and p
    # differnce[char] > 0 means number of symbols 'char' in p is greater than in current substring of s
    # differnce[char] == -n means number symbol 'char' is present in substring of s n times, but not present in p
    s_substring_end = -1
    s_substring_start = -len(p)
    difference: dict[str, int] = {}
    for char in p:
        difference[char] = difference.get(char, 0) + 1
    n_different_symbols = len(p)
    starting_indecies = []
    while s_substring_end+1 < len(s):
        # add next symbol to substring
        # differnce[char] > 0 means number of symbols 'char' in p was greater than in current substring of s
        s_substring_end += 1
        add_char = s[s_substring_end]
        if difference.get(add_char, 0) > 0:
            n_different_symbols -= 1
        else:
            n_different_symbols += 1
        difference[add_char] = difference.get(add_char, 0) - 1
        # remove leftmost symbol from substring
        # differnce[char] == -n means number symbol 'char' is present in substring of s n times, but not present in p
        if s_substring_start >= 0: # necessary for initialization
            remove_char = s[s_substring_start]
            if difference.get(remove_char, 0) < 0:
                n_different_symbols -= 1
            else:
                n_different_symbols += 1
            difference[remove_char] = difference.get(remove_char, 0) + 1
        s_substring_start += 1
        # check if it is anagram
        if n_different_symbols == 0:
            starting_indecies.append(s_substring_start)
    return starting_indecies


def test_examples():
    assert findAnagrams('abab', 'ab') == [0,1,2]
    assert findAnagrams('cbaebabacd', 'abc') == [0,6]


def test_corner():
    assert findAnagrams('a', 'a') == [0]
    assert findAnagrams('a', 'b') == []
    assert findAnagrams('b', 'a') == []
    assert findAnagrams('a', 'ab') == []


def test_2():
    assert findAnagrams('ab', 'ab') == [0]
    assert findAnagrams('ab', 'ba') == [0]
    assert findAnagrams('ab', 'b') == [1]
    assert findAnagrams('ab', 'a') == [0]
    assert findAnagrams('aa', 'a') == [0,1]

def test_3():
    assert findAnagrams('abc', 'b') == [1]
    assert findAnagrams('aba', 'a') == [0,2]


def test_random():
    assert findAnagrams('ababa', 'ab') == [0,1,2,3]
    assert findAnagrams('abacba', 'ab') == [0,1,4]
