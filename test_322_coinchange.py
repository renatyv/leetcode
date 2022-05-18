def coinChange(coins: list[int], amount: int) -> int:
    """You are given an integer array coins representing coins of different denominations
    and an integer amount representing a total amount of money.
    Return the fewest number of coins that you need to make up that amount.
    If that amount of money cannot be made up by any combination of the coins, return -1.
    You may assume that you have an infinite number of each kind of coin.
    Idea: greedy recursion
    1. Sort in descending order
    F(amount, [c1,c2,c3]) = min(F(amount-c1)+1,F(amount-c2)+1,(amount-c3)+1)"""
    MAX_COINS = amount+1
    min_count_for = [MAX_COINS] * (amount+1)
    min_count_for[0] = 0
    for cur_amount in range(amount+1):
        for nominal in coins:
            if cur_amount >= nominal:
                min_count_for[cur_amount] = min(min_count_for[cur_amount],
                                                min_count_for[cur_amount-nominal]+1)
    if min_count_for[-1] == MAX_COINS:
        return -1
    else:
        return min_count_for[-1]


def test_corner():
    assert coinChange([1], 1) == 1
    assert coinChange([1], 2) == 2
    assert coinChange([2], 1) == -1
    assert coinChange([2, 3], 1) == -1
    assert coinChange([1, 2], 1) == 1
    assert coinChange([1, 2], 2) == 1


def test_examples():
    assert coinChange([1, 2, 5], 11) == 3
    assert coinChange([2], 3) == -1
    assert coinChange([1], 0) == 0


def test_wa1():
    assert coinChange([186, 419, 83, 408], 6249) == 20


def test_tle():
    assert coinChange([208,170,205,425,124,375], 7130)
    assert coinChange([429,171,485,26,381,31,290], 8440)
