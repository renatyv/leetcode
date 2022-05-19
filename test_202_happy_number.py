def isHappy(n: int) -> bool:
    """A happy number is a number defined by the following process:
    1. Starting with any positive integer,
    replace the number by the sum of the squares of its digits.
    2. Repeat the process until the number equals 1 (where it will stay),
    or it loops endlessly in a cycle which does not include 1.
    3. Those numbers for which this process ends in 1 are happy.
    Idea: use hashset to save history"""
    history: set[int] = set()
    while n not in history:
        if n == 1:
            return True
        history.add(n)
        squared_digits_sum = 0
        while n > 0:
            squared_digits_sum += (n % 10) ** 2
            n = n//10
        n = squared_digits_sum
    return False


def test_examples():
    assert isHappy(19)
    assert not isHappy(2)


def test_cases():
    assert isHappy(1)