def isPowerOfTwo(n: int) -> bool:
    """Given an integer n, return true if it is a power of two.
    Otherwise, return false
    Idea 1: use recursion
    Idea 2: use bitwise AND operation: 1111 & 1110 == 0"""
    if n <= 0:
        return False
    return n & (n-1) == 0
    # if n == 1:
    #     return True
    # return n % 2 == 0 and isPowerOfTwo(n // 2)


def test_examples():
    assert isPowerOfTwo(1)
    assert isPowerOfTwo(16)
    assert not isPowerOfTwo(3)


def test_poweroftwo():
    assert isPowerOfTwo(2**31)
    assert not isPowerOfTwo(-2)
    assert not isPowerOfTwo(-1)
    assert not isPowerOfTwo(6)
    assert not isPowerOfTwo(5)
    assert not isPowerOfTwo(7)
    assert not isPowerOfTwo(18)
