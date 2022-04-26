def reverseWords(s: str) -> str:
    """Given a string s, reverse the order of characters in each word within
    a sentence while still preserving whitespace and initial word order."""
    def reverse_a_word(word: str) -> str:
        return word[::-1]
    words = s.split(' ')
    reversed_sentence = " ".join(reverse_a_word(w) for w in words)
    return reversed_sentence


def test_examples():
    assert reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
    assert reverseWords("God Ding") == "doG gniD"


def test_reverse_words_1():
    assert reverseWords("1") == "1"
    assert reverseWords("12") == "21"
    assert reverseWords("12 34") == "21 43"

