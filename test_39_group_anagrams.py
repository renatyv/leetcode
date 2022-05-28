from collections import Counter


class HashableStringCounter(Counter):
    def __hash__(self):
        return ''.join(char * self[char] for char in sorted(self)).__hash__()


def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """Given an array of strings strs, group the anagrams together. You can return the answer in any order.
    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once"""
    dict_of_anagrams: dict[HashableStringCounter, list[str]] = dict()
    for word in strs:
        hashable_counter = HashableStringCounter(word)
        if hashable_counter not in dict_of_anagrams:
            dict_of_anagrams[hashable_counter] = [word]
        else:
            dict_of_anagrams[hashable_counter].append(word)
    return list(dict_of_anagrams.values())


def test_examples():
    assert groupAnagrams([""]) == [[""]]
    assert groupAnagrams(["a"]) == [["a"]]
