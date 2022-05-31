from collections import deque
from enum import Enum


def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """There are a total of numCourses courses you have to take,
    labeled from 0 to numCourses - 1.
    You are given an array prerequisites where
    prerequisites[i] = [ai, bi]
    indicates that you must take course bi first if you want to take course ai.
    Return true if you can finish all courses. Otherwise, return false.

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.

    Idea:
    1. costruct adjacency list
    2. Use BFS to check if there are cycles"""

    NEW_NODE = 0
    DISCOVERED = 1
    NO_CYCLES = 2

    def no_cycles(node: int) -> bool:
        # DFS
        if status[node] == NO_CYCLES:
            return True
        if status[node] == DISCOVERED:
            return False
        # new nodem mark as discovered
        status[node] = DISCOVERED
        # discover all children
        for i in adjacent[node]:
            # if there is cycle inside, return False
            if not no_cycles(i):
                return False
        # mark that there are no cycles here
        status[node] = NO_CYCLES
        return True

    # fill adjacency list
    adjacent = [[] for _ in range(numCourses)]
    status: list[int] = [NEW_NODE] * numCourses
    for node, dependancy in prerequisites:
        adjacent[node].append(dependancy)
    # check every node
    for i in range(numCourses):
        # if there is cycle
        if not no_cycles(i):
            return False
    return True


def test_edge_cases():
    assert canFinish(1, [])
    assert canFinish(2, [[0, 1]])
    assert canFinish(2, [[1, 0]])
    assert canFinish(3, [[1, 0], [2, 1]])
    assert canFinish(3, [[1, 0], [2, 0]])
    assert canFinish(5, [[2, 1], [2, 0], [3, 2]])
    assert canFinish(5, [[4, 3], [3, 2], [2, 1], [4, 1]])
    assert canFinish(3, [[0, 1], [0, 2], [1, 2]])
    assert canFinish(7, [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]])
    assert not canFinish(3, [[1, 0], [1, 2], [0, 1]])
    assert not canFinish(5, [[4, 3], [3, 2], [2, 1], [1, 4]])
    assert not canFinish(3, [[1, 0], [2, 1], [0, 1]])
    assert not canFinish(3, [[1, 2], [0, 1], [2, 0]])
    assert not canFinish(4, [[1, 2], [0, 1], [2, 0]])
    # 4 -> [3], 3->[0,1], 2->[3], 1->[2], cycle: 3->1->2->3
    assert not canFinish(5, [[4, 3], [3, 0], [3, 1], [2, 3], [1, 2]])


def test_examples():
    assert canFinish(2, [[1, 0]])
    assert not canFinish(2, [[1, 0], [0, 1]])
