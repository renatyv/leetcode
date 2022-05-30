def checkInclusion(reference_string: str, test_string: str) -> bool:
    """Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
    In other words, return true if one of s1's permutations is the substring of s2.

    Idea: use dict (hashtable) to store difference of symbols count.
    Run over test_string sequentially to update this difference"""
    if len(test_string) < len(reference_string):
        return False
    # strings_difference_dict['a'] = 2 means reference string has two more symbols 'a' than test substring
    strings_difference_dict: dict[str, int] = dict()
    for char in reference_string:
        strings_difference_dict[char] = strings_difference_dict.get(char, 0) + 1
    num_of_different_symbols = len(reference_string)
    # Check next substring (next = advance pointer by one symbol)
    for substring_starting_index in range(-len(reference_string), len(test_string) - len(reference_string)):
        # remove first symbol from the beginning
        remove_symbol = None if substring_starting_index < 0 else test_string[substring_starting_index]
        if remove_symbol:
            strings_difference_dict[remove_symbol] += 1
            if strings_difference_dict[remove_symbol] <= 0:
                num_of_different_symbols -= 1
            else:
                num_of_different_symbols += 1
        # add symbol to the end
        add_symbol = test_string[substring_starting_index + len(reference_string)]
        strings_difference_dict[add_symbol] = strings_difference_dict.get(add_symbol, 0) - 1
        if strings_difference_dict[add_symbol] >= 0:
            num_of_different_symbols -= 1
        else:
            num_of_different_symbols += 1
        if num_of_different_symbols == 0:
            return True
    return False


def test_edge_cases():
    assert checkInclusion("a", "a")
    assert checkInclusion("a", "abc")
    assert checkInclusion("a", "bac")
    assert checkInclusion("a", "bca")
    assert not checkInclusion("a", "b")
    assert not checkInclusion("asv", "")
    assert not checkInclusion("ab", "b")


def check_thesame():
    assert checkInclusion("asv", "vsa")
    assert checkInclusion("arb", "bar")


def test_examples():
    assert checkInclusion("ab", "eidbaooo")
    assert not checkInclusion("ab", "eidboaoo")
