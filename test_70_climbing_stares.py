def climbStairs(n: int) -> int:
    """You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Idea: dynamic programming.
    Number of ways to climb current step =
        number of ways to climb one step down
        + number of ways to climb two steps down.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    ways_to_climb_pre_pre_step = 1
    ways_to_climb_prev_step = 1
    current_step_number = 2
    ways_to_climb_current_step = 2
    while current_step_number < n:
        ways_to_climb_pre_pre_step, ways_to_climb_prev_step, ways_to_climb_current_step =\
            ways_to_climb_prev_step, ways_to_climb_current_step, (ways_to_climb_current_step + ways_to_climb_prev_step)
        current_step_number += 1
    return ways_to_climb_current_step


def test_climbStairs():
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3
    assert climbStairs(4) == 5
