def characterReplacement(s: str, k: int) -> int:
    """You are given a string s and an integer k.
    You can choose any character of the string and change it to any other uppercase English character.
    You can perform this operation at most k times.
    Return the length of the longest substring containing the same letter you can get
    after performing the above operations.
    Idea: 1) compute longest sequence for index i and use that for i+1
    2) keep dict with count of each character
    3) move left pointer to the right until we are at the longest required substring again"""
    if len(s) <= k:
        return len(s)
    longest_seq = 0
    left = 0
    char_counter: dict[str, int] = dict()
    for right in range(len(s)):
        char_counter[s[right]] = char_counter.get(s[right], 0) + 1
        while (right - left + 1) - max(char_counter.values()) > k:
            char_counter[s[left]] -= 1
            left += 1
        cur_seq_len = right - left + 1
        longest_seq = max(cur_seq_len, longest_seq)
    return longest_seq


def test_edge_cases():
    assert characterReplacement('A', 0) == 1
    assert characterReplacement('A', 1) == 1
    assert characterReplacement('A', 2) == 1
    assert characterReplacement('AB', 0) == 1
    assert characterReplacement('AB', 1) == 2
    assert characterReplacement('AB', 3) == 2
    assert characterReplacement('ABC', 2) == 3
    assert characterReplacement('ABB', 1) == 3
    assert characterReplacement('BBA', 1) == 3
    assert characterReplacement('BAB', 1) == 3
    assert characterReplacement('ABB', 2) == 3
    assert characterReplacement('ABBA', 2) == 4
    assert characterReplacement('ABBA', 1) == 3
    assert characterReplacement('ABBA', 0) == 2
    assert characterReplacement('ABAB', 0) == 1
    assert characterReplacement('ABAB', 1) == 3
    assert characterReplacement('ABAB', 2) == 4
    assert characterReplacement('ABCAB', 2) == 4
    assert characterReplacement('ABACB', 2) == 4
    assert characterReplacement('FBACBB', 2) == 5


def test_examples():
    assert characterReplacement('ABAB', 2) == 4
    assert characterReplacement('AABABBA', k=1) == 4
