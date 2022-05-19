def rangeBitwiseAnd(left: int, right: int) -> int:
    """Given two integers left and right that represent the range [left, right],
    return the bitwise AND of all numbers in this range, inclusive.

    Idea.
    If number of bits is different, return 0
    When we start &-ing numbers, most of the bits from the left will become 0.
    Only '1's are these, which are common to both numbers.
    We need to find the longest common prefix of '1's.
    To do that, shift to the right until numbers are equal"""

    l, r = left, right
    n_shifted_bits = 0
    while l != r and l >= 0:
        l = l >> 1
        r = r >> 1
        n_shifted_bits += 1
    for i in range(n_shifted_bits):
        l = l << 1
    return l


def bruteforce(left: int, right: int):
    ans = left
    for i in range(left, right + 1):
        ans = ans & i
    return ans


def test_examples():
    assert rangeBitwiseAnd(5, 7) == 4
    assert rangeBitwiseAnd(0, 0) == 0
    assert rangeBitwiseAnd(1, 2147483647) == 0


def test_cases_1():
    assert rangeBitwiseAnd(0b0, 0b1) == 0
    assert rangeBitwiseAnd(0b11, 0b111) == bruteforce(0b11, 0b111)
    assert rangeBitwiseAnd(0b1, 0b1) == 0b1
    assert rangeBitwiseAnd(0b10011, 0b10111) == bruteforce(0b10011, 0b10111)
