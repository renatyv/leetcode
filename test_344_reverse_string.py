def reverseString(s: list[str]) -> None:
    """Idea: just swap em"""
    if len(s) == 1:
        return
    left = 0
    right = len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return


def test_rever_string_edgecases():
    s = ['1']
    reverseString(s)
    assert s == ['1']


def test_even_uneven_length():
    s = ['1','2']
    reverseString(s)
    assert s == ['2','1']
    s = ['1','2','3']
    reverseString(s)
    assert s == ['3','2','1']


def test_reverse_string_examples():
    s = ["h","e","l","l","o"]
    reverseString(s)
    assert s == ["o","l","l","e","h"]
    s = ["H","a","n","n","a","h"]
    reverseString(s)
    assert s == ["h","a","n","n","a","H"]
