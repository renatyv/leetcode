from collections import Counter


def minWindow(s: str, t: str) -> str:
    """Given two strings s and t of lengths m and n respectively,
    return the minimum window substring of s such that every character in t
    (including duplicates) is included in the window.
    If there is no such substring, return the empty string ""."""
    # how many characters is necessary
    if not t or not s:
        return ""

    t_counter = Counter(t)
    required = len(t_counter)

    # left and right pointer
    left, right = 0, 0

    # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    # e.g. if t is "AABC" then the window must have two A's, one B and one C. Thus formed would be = 3 when all these conditions are met.
    formed = 0

    # Dictionary which keeps a count of all the unique characters in the current window.
    window_counter = {}

    # ans tuple of the form (window length, left, right)
    MAX_LEN = 10 ** 6
    current_window = (MAX_LEN, None, None)

    while right < len(s):

        # Add one character from the right to the window
        char = s[right]
        window_counter[char] = window_counter.get(char, 0) + 1

        # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
        if char in t_counter and window_counter[char] == t_counter[char]:
            formed += 1

        # Try and contract the window till the point where it ceases to be 'desirable'.
        while left <= right and formed == required:
            char = s[left]

            # Save the smallest window until now.
            if right - left + 1 < current_window[0]:
                current_window = (right - left + 1, left, right)

            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counter[char] -= 1
            if char in t_counter and window_counter[char] < t_counter[char]:
                formed -= 1

            # Move the left pointer ahead, this would help to look for a new window.
            left += 1

            # Keep expanding the window once we are done contracting.
        right += 1
    return '' if current_window[0] == MAX_LEN else s[current_window[1]: current_window[2] + 1]


def test_edge_cases():
    assert minWindow('abcdef', 'dg') == ''
    assert minWindow('a', 'b') == ''
    assert minWindow('a', 'a') == 'a'
    assert minWindow('aa', 'a') == 'a'
    assert minWindow('ab', 'b') == 'b'
    assert minWindow('ba', 'b') == 'b'
    assert minWindow('abc', 'b') == 'b'


def test_cases_1():
    assert minWindow('cabad', 'aba') == 'aba'
    assert minWindow('cabra..abag', 'aba') == 'aba'
    assert minWindow('cabad', 'aa') == 'aba'
    assert minWindow('cabad', 'cd') == 'cabad'


def test_examples():
    assert minWindow(s="ADOBECODEBANC", t="ABC") == "BANC"
    assert minWindow(s="a", t="a") == 'a'
    assert minWindow(s="a", t="aa") == ''
