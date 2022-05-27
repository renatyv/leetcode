def maxProfit(prices: list[int]) -> int:
    """You are given an array prices where prices[i] is the price of a given stock on the ith day.
    Find the maximum profit you can achieve. You may complete as many transactions as you like
    (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:
    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
    Note: You may not engage in multiple transactions simultaneously
    (i.e., you must sell the stock before you buy again).

    Dynamic programming.
    Two arrays:
    buy[i] - msx profit if last operation was buying;
    sell[i] - max profit if last operation was selling.
    buy[i] = max(buy[i-1], sell[i-2]-price[i]), do nothing or buy after you sold
    sell[i] = max(sell[i-1], buy[i]+price[i]), do nothing or sell after you bought"""
    if len(prices) == 1:
        return 0
    if len(prices) == 2:
        return max(0, prices[1] - prices[0])
    # init arrays
    buy = [0] * len(prices)
    sell = [0] * len(prices)
    buy[0] = -prices[0]
    buy[1] = max(-prices[0], -prices[1])

    sell[0] = 0
    sell[1] = max(0, buy[0] + prices[1])
    for i, price in enumerate(prices[2:], start=2):
        buy[i] = max(buy[i - 1], sell[i - 2] - price)
        sell[i] = max(sell[i - 1], buy[i - 1] + price)
    return max(buy[-1], sell[-1])


def test_corner_cases():
    assert maxProfit([0]) == 0
    assert maxProfit([1, 1]) == 0
    assert maxProfit([2, 1]) == 0
    assert maxProfit([1, 2]) == 1
    assert maxProfit([1, 0]) == 0
    assert maxProfit([1, 0]) == 0
    assert maxProfit([0, 1]) == 1
    assert maxProfit([0, 1, 2]) == 2
    assert maxProfit([1, 0, 2]) == 2
    assert maxProfit([1, 2, 4, 1]) == 3
    assert maxProfit([1, 4, 2]) == 3


def test_examples():
    assert maxProfit([1, 2, 3, 0, 2]) == 3
    assert maxProfit([1]) == 0
