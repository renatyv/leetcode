def backspaceCompare(s: str, t: str) -> bool:
    """Given two strings s and t, return true if they are equal when both are typed into empty text editors.
    '#' means a backspace character.
    Note that after backspacing an empty text, the text will continue empty.

    Idea: remove symbols preceding to # and compare resulting strings. """

    def process_string(string: str) -> list[str]:
        resulting_list: list[str] = []
        for char in string:
            if char == '#':
                if resulting_list:
                    resulting_list.pop()
                continue
            resulting_list.append(char)
        return resulting_list

    return process_string(s) == process_string(t)


def test_examples():
    assert backspaceCompare("ab#c", "ad#c")
    assert backspaceCompare("ab##", "c#d#")
    assert not backspaceCompare("a#c", "b")


def test_corner():
    assert backspaceCompare("###", "a,b,c######")
    assert backspaceCompare('', '#')
    assert backspaceCompare('', '')


def test_cases_1():
    assert backspaceCompare('a', 'a')
    assert backspaceCompare('a#', 'a#')
    assert backspaceCompare('ab#', 'a')
    assert backspaceCompare('a#ab#', 'a')
