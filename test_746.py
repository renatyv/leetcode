def minCostClimbingStairs(cost: list[int]) -> int:
    """Idea: save minimal cost for climbing step i into min_cost array. Use that to cimpute step n+1"""
    if len(cost) < 2:
        return 0
    if len(cost) == 2:
        return min(cost[0], cost[1])
    min_cost: list[int] = [0, 0]
    for n in range(2, len(cost)+1):
        min_cost.append(min(min_cost[-1] + cost[n - 1], min_cost[-2] + cost[n - 2]))
    return min_cost[len(cost)]


def test_minCostClimbingStairs():
    assert minCostClimbingStairs([1, 2]) == 1
    assert minCostClimbingStairs([2, 1]) == 1
    assert minCostClimbingStairs([1, 100, 2]) == 3
    assert minCostClimbingStairs([100, 1, 1]) == 1
    assert minCostClimbingStairs([100, 1, 1, 1]) == 2
    assert minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6