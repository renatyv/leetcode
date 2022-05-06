def hammingWeight(n: int) -> int:
    """Write a function that takes an unsigned integer and returns the number of '1' bits it has
    (also known as the Hamming weight)."""
    if n == 0:
        return 0
    number_of_bits = 0
    while n >=1 :
        number_of_bits += n & 1 # n % 2
        n = n >> 1 # n // 2
    return number_of_bits


def test_hammingWeight():
    assert hammingWeight(0) == 0
    assert hammingWeight(1) == 1
    assert hammingWeight(2) == 1
    assert hammingWeight(3) == 2
    assert hammingWeight(4) == 1
    assert hammingWeight(5) == 2
    assert hammingWeight(6) == 2
    assert hammingWeight(7) == 3