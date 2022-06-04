def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """Given an array of integers temperatures represents the daily temperatures,
    return an array answer such that
    answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
    If there is no future day for which this is possible, keep answer[i] == 0 instead.

    1 <= temperatures.length <= 10^5
    30 <= temperatures[i] <= 100
    Idea:
    keep stack of indexes for decreasing temps"""
    n = len(temperatures)
    days_to_warmer = [0] * n
    deacreasing_temps_indexes = []
    for curr_day, curr_temp in enumerate(temperatures):
        while deacreasing_temps_indexes and temperatures[deacreasing_temps_indexes[-1]] < curr_temp:
            prev_day = deacreasing_temps_indexes.pop()
            days_to_warmer[prev_day] = curr_day - prev_day
        deacreasing_temps_indexes.append(curr_day)
    return days_to_warmer


def test_edge_cases():
    assert dailyTemperatures([31]) == [0]
    assert dailyTemperatures([31, 32]) == [1, 0]
    assert dailyTemperatures([32, 31]) == [0, 0]
    assert dailyTemperatures([30, 30]) == [0, 0]
    assert dailyTemperatures([31, 31, 32]) == [2, 1, 0]
    assert dailyTemperatures([32, 30, 30, 31]) == [0, 2, 1, 0]
    assert dailyTemperatures([30, 31, 32, 33]) == [1, 1, 1, 0]
    assert dailyTemperatures([33, 32, 31, 31]) == [0, 0, 0, 0]


def test_cases_1():
    assert dailyTemperatures([35, 33, 35, 36, 30, 33, 35, 34]) == [3, 1, 1, 0, 1, 1, 0, 0]


def test_examples():
    assert dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert dailyTemperatures([30, 60, 90]) == [1, 1, 0]
