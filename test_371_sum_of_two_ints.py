def getSum(a: int, b: int) -> int:
    """Given two integers a and b,
    return the sum of the two integers without using the operators + and -.
    Idea: sum bit by bit
    zero ones
    one one
    two ones
    three ones"""

    def add(a, b):
        if a == 0 or b == 0:
            return a | b
        # a ^ b = different bits, will add up to 1
        # a & b = bits equal to 1, will add up to 0 and shifted
        return add(a ^ b, (a & b) << 1)

    if a * b < 0:  # assume a < 0, b > 0
        if a > 0:
            return getSum(b, a)
        # -a = 1 + (~a)
        if add(~a, 1) == b:  # -a == b
            return 0
        if add(~a, 1) < b:  # -a < b
            # (-a) + (-b)
            return add(~add(add(~a, 1), add(~b, 1)), 1)

    return add(a, b)  # a*b >= 0 or (-a) > b > 0


def test_getSum():
    assert getSum(-1, 1) == 0
    assert getSum(0, 0) == 0
    assert getSum(0, 1) == 1
    assert getSum(1, 1) == 2
    assert getSum(1, 2) == 3
    assert getSum(2, 2) == 4
    assert getSum(1, 4) == 5
    assert getSum(2, 4) == 6
    assert getSum(3, 4) == 7
    assert getSum(4, 4) == 8
