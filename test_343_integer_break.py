def integerBreak(n: int) -> int:
    """Given an integer n, break it into the sum of k positive integers, where k >= 2,
    and maximize the product of those integers.
    Return the maximum product you can get.
    2 <= n <= 58
    Idea: Dynamic programming.
    integerBreak(n) = max (integerBreak(n-k)*k), k=1...n"""
    if n == 2:
        return 1
    if n == 3:
        return 2
    max_product = [1] * (n+1)
    for m in range(2, n+1):
        for k in range(2, m+1):
            max_product[m] = max(max_product[m],
                                 max_product[m-k]*k)
    return max_product[-1]


def test_cases():
    assert integerBreak(2) == 1
    assert integerBreak(3) == 2
    assert integerBreak(4) == 4
    assert integerBreak(5) == 6
    assert integerBreak(6) == 9
    assert integerBreak(7) == 12
    assert integerBreak(8) == 18
    assert integerBreak(9) == 27
    assert integerBreak(10) == 36
    assert integerBreak(58) == 1549681956
