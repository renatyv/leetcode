def checkValidString(s: str) -> bool:
    """Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
    The following rules define a valid string:

    1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
    3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

    1 <= s.length <= 100
    s[i] is '(', ')' or '*'.

    Idea: greedy solution.
    Keep track of interval (open_min, open_max) of possible number of open brackets.
    If we encounter '(', we increase the left-hand side of the interval
    If we encounter ')', we decrease the right-hand side of the interval
    Since '*' can be '(' or ')' or '', it increases the right hand-side of the interval
    Examples:
    '' - 0,0
    '(' - 1,1
    '()' - 0,0
    '((' - 2,0
    '((*' - 2,1
    '((*)' -
    """
    min_number_of_open_parenthesis = 0
    max_number_of_open_parenthesis = 0
    for char in s:
        if char == '(':
            min_number_of_open_parenthesis += 1
            max_number_of_open_parenthesis += 1
        elif char == ')':
            min_number_of_open_parenthesis -= 1
            max_number_of_open_parenthesis -= 1
        else:  # char == '*'
            min_number_of_open_parenthesis -= 1
            max_number_of_open_parenthesis += 1
        if max_number_of_open_parenthesis < 0:
            return False
        # number of left open parenthesis must be non-negative
        min_number_of_open_parenthesis = max(0, min_number_of_open_parenthesis)
    return min_number_of_open_parenthesis == 0


def test_edge_cases():
    assert checkValidString('')
    assert checkValidString('*')
    assert checkValidString('**')
    assert checkValidString('*)')
    assert checkValidString('(*')
    assert checkValidString('(*)')
    assert checkValidString('(**)')
    assert checkValidString('(*))')
    assert checkValidString('((**')
    assert checkValidString('((*)')
    assert checkValidString('**))')
    assert checkValidString('**))')
    assert checkValidString('*)*')
    assert checkValidString('*(*')
    assert checkValidString('*()')
    assert checkValidString('()*')
    assert checkValidString('()*()')
    assert checkValidString('(**')
    assert checkValidString('**)')
    assert not checkValidString('(')
    assert not checkValidString(')')
    assert not checkValidString(')*')
    assert not checkValidString('*(')
    assert not checkValidString('(*)(')
    assert not checkValidString('((*')
    assert not checkValidString('*))')


def test_examples():
    assert checkValidString('()')
    assert checkValidString('(*)')
    assert checkValidString('(*))')


def test_wa1():
    assert checkValidString(
        "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()")
    assert checkValidString(
        "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()")
