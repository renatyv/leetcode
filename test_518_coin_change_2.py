from functools import cache


def change(amount: int, coins: list[int]) -> int:
    """Idea: recursive + memoization
    number of ways =
    change(amount, coins[:-1])
    + change(amount-coins[-1], coins[:-1])
    + change(amount-2*coins[-1], coins[:-1])
    +...
    + 1 if amount can be given with the largest coin only
    """

    @cache
    def recursive_number_of_changes(amount: int, coins_number: int) -> int:
        """number of ways to change with first n coins"""
        nonlocal coins
        if amount < coins[0]:
            return 0
        if coins_number == 1:
            if amount % coins[0] == 0 and amount // coins[0] > 0:
                return 1
            return 0
        nominal = coins[coins_number - 1]
        coin_n_max_count = amount // nominal

        number_of_changes = 0
        if amount % nominal == 0 and coin_n_max_count > 0:
            number_of_changes = 1
        # take
        for number_of_coin_n in range(coin_n_max_count + 1):
            amount_taken = number_of_coin_n * nominal
            number_of_changes += recursive_number_of_changes(amount - amount_taken, coins_number - 1)
        return number_of_changes

    if amount == 0:
        return 1
    coins.sort()
    return recursive_number_of_changes(amount, len(coins))


def test_edge_cases():
    assert change(0, [7]) == 1
    assert change(0, [1, 2, 3, 4, 4, 5, 5]) == 1
    assert change(1, [1, 2]) == 1
    assert change(2, [1, 2]) == 2
    assert change(4, [1, 2]) == 3
    assert change(2, [1, 2, 3]) == 2
    assert change(3, [1, 2, 3]) == 3
    assert change(4, [1, 2, 3]) == 4
    assert change(4, [1, 2, 3, 4]) == 5


def test_wa1():
    assert change(200, [89, 76, 50, 37]) == 3
    assert change(200, [89, 76, 63, 50, 37]) == 5
    assert change(200, [102, 89, 76, 63, 50, 37]) == 5
    assert change(200, [102, 89, 76, 63, 50, 37, 24]) == 13
    assert change(200, [102, 89, 76, 63, 50, 37, 24, 11]) == 24


def test_max_cases():
    assert change(1, list(range(1, 301))) == 1
    assert change(2, list(range(1, 301))) == 2
    assert change(3, list(range(1, 301))) == 3


def test_examples():
    assert change(5, [1, 2, 5]) == 4
    assert change(3, [2]) == 0
    assert change(10, [10]) == 1
