import heapq
from collections import Counter


def leastInterval(tasks: list[str], n: int) -> int:
    """Idea: use two max heap
    1) count number of each tasks
    2) pop tasks with the largest number and decrease counter
    3) if the largest count is one, execute each task once and return the answer"""
    # no cooldown, execute each task once
    if n == 0:
        return len(tasks)
    # count number of each task
    task_counter = Counter(tasks)
    # heapq provides min heap. Therefore, we put negative numbers as count to get max_heap
    cur_tasks_heap = [(-count, task) for task, count in task_counter.items()]
    heapq.heapify(cur_tasks_heap)
    n_iterations = 0
    while cur_tasks_heap:
        # if maximal number of tasks = 1, then all tasks have count = 1.
        # Execute each of them once and return the answer
        largest_count = -cur_tasks_heap[0][0]
        if largest_count == 1:
            return n_iterations + len(cur_tasks_heap)
        executed_tasks = []
        # execute n+1 largest tasks (idle if no more tasks left)
        for i in range(n + 1):
            # if no more tasks left
            if not cur_tasks_heap:
                break
            minus_count, task = heapq.heappop(cur_tasks_heap)
            executed_tasks.append((minus_count + 1, task))
        n_iterations += n + 1
        # put tasks back
        for minus_count, task in executed_tasks:
            if minus_count < 0:
                heapq.heappush(cur_tasks_heap, (minus_count, task))
    return n_iterations


def test_edge_cases():
    assert leastInterval(['A'], 0) == 1
    assert leastInterval(['A'], 1) == 1
    assert leastInterval(['A'], 2) == 1
    assert leastInterval(['A', 'A'], 0) == 2
    assert leastInterval(['A', 'A'], 1) == 3
    assert leastInterval(['A', 'A'], 2) == 4
    assert leastInterval(['A', 'A', 'A'], 2) == 7
    assert leastInterval(['A', 'B'], 0) == 2
    assert leastInterval(['A', 'B'], 1) == 2
    assert leastInterval(['A', 'B', 'C', 'D'], 1) == 4
    assert leastInterval(['A', 'B', 'C', 'D'], 4) == 4
    assert leastInterval(['A', 'B'], 2) == 2
    assert leastInterval(['A', 'B', 'A'], 0) == 3
    assert leastInterval(['A', 'B', 'A'], 1) == 3
    assert leastInterval(['A', 'B', 'A'], 2) == 4
    assert leastInterval(['B', 'A', 'B'], 2) == 4


def test_examples():
    assert leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    assert leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
    assert leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16
