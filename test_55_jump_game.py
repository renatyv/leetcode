def canJump_recursive(nums: list[int]) -> bool:
    """Idea 1: create bool array of reachable steps
    Idea 2: try jumping the longest distance first"""
    if len(nums) == 1:
        return True
    if nums[0] == 0:
        return False
    visited = [False] * len(nums)

    def recursive_try_jump(cur_step: int, nums: list[int], visited: list[bool]):
        if cur_step >= len(nums) - 1:
            return True
        if nums[cur_step] == 0:
            return False
        if visited[cur_step]:
            return False
        visited[cur_step] = True
        max_step = cur_step + nums[cur_step]
        for next_step in range(max_step,
                               cur_step,
                               -1):
            if recursive_try_jump(next_step, nums, visited):
                return True
        return False

    return recursive_try_jump(0, nums, visited)


def canJump(nums: list[int]) -> bool:
    """Idea: create bool array of reachable steps
    Idea: DFS"""
    if len(nums) == 1:
        return True
    if nums[0] == 0:
        return False
    visited = [False] * len(nums)
    unvisited_indexes_stack = [0]
    while unvisited_indexes_stack:
        cur_step = unvisited_indexes_stack.pop()
        max_index = cur_step + nums[cur_step]
        if max_index >= len(nums) - 1:
            return True
        for next_step in range(cur_step + 1, max_index + 1):
            if not visited[next_step]:
                unvisited_indexes_stack.append(next_step)
                visited[next_step] = True
    return False


def test_canJump_1():
    assert not canJump([1, 0, 2, 3, 4])


def test_canJump():
    assert canJump([0])
    assert canJump([1])
    assert canJump([2, 3, 1, 1, 4])
    assert canJump([1, 1, 1, 1, 1])
    assert canJump([2, 4, 0, 1, 0, 0])
    assert not canJump([0, 1])
    assert not canJump([1, 0, 0])
    assert not canJump([2, 4, 0, 2, 0, 0, 0])
    assert not canJump([3, 2, 1, 0, 4])
