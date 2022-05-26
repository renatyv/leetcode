def lengthOfLongestSubstring(s: str) -> int:
    """
    Idea 1: compute longest substring for substring s[0:k+1] using results for substring s[0:k]
    Idea 2: use set to keep characters and sliding window (2 pointers).
    """
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    # maps symbols to it's last occurance in the string
    left = 0
    right = 0
    len_of_longest_substring = 0
    current_substring_chars = set()
    for right in range(0, len(s)):
        if s[right] in current_substring_chars:
            # remove all symbols upto first occurrence of s[right]
            while s[right] in current_substring_chars:
                current_substring_chars.remove(s[left])
                left += 1
        current_substring_chars.add(s[right])
        len_of_longest_substring = max(len_of_longest_substring, right - left + 1)
    return len_of_longest_substring


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
