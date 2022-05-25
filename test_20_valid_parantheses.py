def isValid(s: str) -> bool:
    opened_parantheses: list[str] = []
    for char in s:
        if char in ('(', '{', '['):
            opened_parantheses.append(char)
        else:
            try:
                opened_paranthesis = opened_parantheses.pop()
                if (char == ')' and opened_paranthesis != '(') \
                        or (char == ']' and opened_paranthesis != '[') \
                        or (char == '}' and opened_paranthesis != '{'):
                    return False
            except IndexError:
                return False
    return not opened_parantheses


def corner_cases():
    assert not isValid("(")
    assert not isValid("}")
    assert not isValid("]{")
    assert not isValid("[}")
    assert not isValid("][")
    assert not isValid("(()")


def test_examples():
    assert isValid("()")
    assert isValid("()[]{}")
    assert not isValid("(]")


def test_additional_tests():
    assert isValid('([{}])')
    assert not isValid('[[()}]')
    assert isValid('({[][]})')
