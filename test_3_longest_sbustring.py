import pytest


def lengthOfLongestSubstring(s: str) -> int:
    """
    Idea 1: compute longest substring for substring s[0:k+1] using results for substring s[0:k]
    Idea 2: use hash table to save las occurance of every symbol.
    Then use that information to think on next character.
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    # maps symbols to it's last occurance in the string
    last_symbol_position = dict()
    absolute_longest_substring = 0
    # length of a longest substring wuthout repetitions ending at symbol k-1
    cur_longest_substring_length = 0
    # in string s[last_repeting_index+1 : next_index] there are no repeating values
    last_repeating_index = -1
    for next_index in range(len(s)):
        next_symbol = s[next_index]
        # new symbol, not encountered before
        if next_symbol not in last_symbol_position:
            cur_longest_substring_length += 1
        else:
            # we've seen this symbol before, but was it after last_repeating_index?
            if last_repeating_index <= last_symbol_position[next_symbol]:
                last_repeating_index = last_symbol_position[next_symbol]
                cur_longest_substring_length = next_index - last_repeating_index
            else:
                cur_longest_substring_length += 1
        absolute_longest_substring = max(absolute_longest_substring, cur_longest_substring_length)
        last_symbol_position[next_symbol] = next_index
    return absolute_longest_substring


def test_length_of_longest_substring():
    assert lengthOfLongestSubstring('') == 0
    assert lengthOfLongestSubstring('b') == 1
    assert lengthOfLongestSubstring('bb') == 1
    assert lengthOfLongestSubstring('bbb') == 1
    assert lengthOfLongestSubstring('ab') == 2
    assert lengthOfLongestSubstring('abb') == 2
    assert lengthOfLongestSubstring('aab') == 2
    assert lengthOfLongestSubstring('1111abc2222') == 5
    assert lengthOfLongestSubstring('111abc222abcd333') == 6
    assert lengthOfLongestSubstring('abcabcbb') == 3
    assert lengthOfLongestSubstring('pwwkew') == 3
