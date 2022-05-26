def countBits(n: int) -> list[int]:
    """Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
    ans[i] is the number of 1's in the binary representation of i.
    0 <= n <= 10^5
    Idea: use dynamic programming
    """
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    n_ones: list[int] = [0] * (n + 1)
    for i in range(n + 1):
        n_ones[i] = n_ones[i // 2] + (i & 1)
    return n_ones


def test_examples():
    assert countBits(2) == [0, 1, 1]
    assert countBits(5) == [0, 1, 1, 2, 1, 2]
