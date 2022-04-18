def maxProfit(prices: list[int]) -> int:
    """return max - min
    Idea: compute two arrays.
    min_price_before[i] = min(prices[0:i])
    max_price_after[i] = max(prices[i:])
    Then for each i profit is (max_price_after[i] - min_price_before[i])
    """
    if len(prices) == 1:
        return 0
    max_price_after_i_reversed = []
    cur_max_price = 0
    for price in prices[:0:-1]:
        cur_max_price = max(price, cur_max_price)
        max_price_after_i_reversed.append(cur_max_price)
    min_price_before_i = []
    cur_min_price = prices[0]
    for price in prices[:-1]:
        cur_min_price = min(cur_min_price, price)
        min_price_before_i.append(cur_min_price)
    max_profit = -10 ** 5
    for buy, sell in zip(min_price_before_i, max_price_after_i_reversed[::-1]):
        max_profit = max(max_profit, sell - buy)
    return max(0, max_profit)


def test_maxProfit_example_1():
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test_maxProfit_example_2():
    assert maxProfit([7, 6, 4, 3, 1]) == 0


def test_maxProfit_zero():
    assert maxProfit([1]) == 0
    assert maxProfit([0]) == 0
    assert maxProfit([1, 1, 1, 1, 1]) == 0
    assert maxProfit([5, 5, 5, 1]) == 0
    assert maxProfit([5, 3, 3, 1]) == 0
    assert maxProfit([4, 3, 2, 1, 0]) == 0
    assert maxProfit([2, 2, 1]) == 0
    assert maxProfit([2, 1]) == 0
    assert maxProfit([20, 0]) == 0


def test_max_profit_many_solutions():
    assert maxProfit([1, 2, 1]) == 1
    assert maxProfit([1, 2]) == 1
    assert maxProfit([2, 10]) == 8
    assert maxProfit([1, 2, 2, 1, 1, 1, 2, 2, 1]) == 1
