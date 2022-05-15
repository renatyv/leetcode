def letterCombinations(digits: str) -> list[str]:
    """Given a string containing digits from 2-9 inclusive,
    return all possible letter combinations that the number could represent.
    Return the answer in any order.
    A mapping of digit to letters (just like on the telephone buttons) is given below.
    Note that 1 does not map to any letters.
    Idea: recursion.
    1. Compute combinations for digits after the first
    2. Append all necessary letters corresponding to the first digit"""
    digit_to_letters: dict[str, list[str]] = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }
    if not digits:
        return []
    if len(digits) == 1:
        return digit_to_letters[digits[0]]
    remaining_digits_combinations: list[str] = letterCombinations(digits[1:])
    resulting_combinations = []
    for letter in digit_to_letters[digits[0]]:
        for remaining_combination in remaining_digits_combinations:
            resulting_combinations.append(letter + remaining_combination)
    return resulting_combinations


def test_examples():
    assert letterCombinations('23') == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    assert letterCombinations('') == []
    assert letterCombinations('2') == ['a', 'b', 'c']
