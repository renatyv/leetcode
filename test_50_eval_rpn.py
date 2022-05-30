def evalRPN(tokens: list[str]) -> int:
    """Evaluate the value of an arithmetic expression in Reverse Polish Notation.
    Valid operators are +, -, *, and /. Each operand may be an integer or another expression.
    Note that division between two integers should truncate toward zero.

    It is guaranteed that the given RPN expression is always valid.
    That means the expression would always evaluate to a result,
    and there will not be any division by zero operation.
    Idea: use stack"""
    if len(tokens) == 1:
        return int(tokens[0])
    stack = []
    for cur_char in tokens:
        if cur_char in ('+', '-', '*', '/'):
            right = stack.pop()
            left = stack.pop()
            if cur_char == '+':
                stack.append(left + right)
            elif cur_char == '-':
                stack.append(left - right)
            elif cur_char == '*':
                stack.append(left * right)
            elif cur_char == '/':
                stack.append(int(left / right))
        else:
            stack.append(int(cur_char))
    return stack[0]


def test_edge_cases():
    assert evalRPN(['1']) == 1
    assert evalRPN(['1', '2', '+']) == 3
    assert evalRPN(['4', '3', '-']) == 1
    assert evalRPN(['2', '3', '*']) == 6
    assert evalRPN(['2', '3', '/']) == 0
    assert evalRPN(['3', '2', '/']) == 1
    assert evalRPN(['4', '2', '/']) == 2
    assert evalRPN(['2', '-3', '/']) == 0


def test_examples():
    assert evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
