from collections import Counter


def generateParenthesis(n: int) -> list[str]:
    """Given n pairs of parentheses,
    write a function to generate all combinations of well-formed parentheses.
    """
    combinations = []

    def generate_sequencies(current_list_of_parantesis, n_left_parantheses=0, n_right_parantheses=0):
        if len(current_list_of_parantesis) == 2 * n:
            combinations.append("".join(current_list_of_parantesis))
            return
        if n_left_parantheses < n:
            current_list_of_parantesis.append("(")
            generate_sequencies(current_list_of_parantesis,
                                n_left_parantheses + 1,
                                n_right_parantheses)
            current_list_of_parantesis.pop()
        if n_right_parantheses < n_left_parantheses:
            current_list_of_parantesis.append(")")
            generate_sequencies(current_list_of_parantesis,
                                n_left_parantheses,
                                n_right_parantheses + 1)
            current_list_of_parantesis.pop()

    generate_sequencies([])
    return combinations


def test_examples():
    assert set(generateParenthesis(1)) == {"()"}
    assert set(generateParenthesis(2)) == {"(())", "()()"}
    test_3 = ["((()))", "(()())", "(())()", "()(())", "()()()"]
    print(Counter(generateParenthesis(3)))
    assert len(set(generateParenthesis(3))) == len(generateParenthesis(3))
    assert len(generateParenthesis(3)) == len(test_3)
    assert set(generateParenthesis(3)) == set(test_3)
    test_4 = ["(((())))", "((()()))", "((())())", "(()(()))", "(()()())",
              "((()))()", "(()())()", "(())(())", "(())()()", "()((()))",
              "()(()())", "()(())()", "()()(())", "()()()()"]
    print(Counter(generateParenthesis(4)))
    assert len(generateParenthesis(4)) == len(set(generateParenthesis(4)))
    assert len(test_4) == len(generateParenthesis(4))
    assert set(generateParenthesis(4)) == set(test_4)
