import collections
import random


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """Idea: use monotonic queue"""
        if k == len(nums):
            return [max(nums)]
        if k == 1:
            return nums
        # init resulting array. Faster than appending all the time
        result = [-10 ** 5] * (len(nums) - k + 1)
        # indecies of elements from nums[] in decreasing order
        monotonic_decreasing_queue = collections.deque([0])
        right_side_of_window = 0
        while right_side_of_window < len(nums):
            # if the first element in the deque is outside the window, remove it
            if monotonic_decreasing_queue:
                if (right_side_of_window - monotonic_decreasing_queue[0]) + 1 > k:
                    monotonic_decreasing_queue.popleft()
            # if next is higher than the highest, re-init deque
            if not monotonic_decreasing_queue \
                    or nums[right_side_of_window] >= nums[monotonic_decreasing_queue[0]]:
                monotonic_decreasing_queue = collections.deque([right_side_of_window])
            else:  # last element in the window is lower than the highest in the deque
                # pop from right (from the smallest) until it is in the correct place
                while nums[monotonic_decreasing_queue[-1]] < nums[right_side_of_window]:
                    monotonic_decreasing_queue.pop()
                monotonic_decreasing_queue.append(right_side_of_window)
            # skip first k-1 elements
            if right_side_of_window >= k - 1:
                result[right_side_of_window - k + 1] = nums[monotonic_decreasing_queue[0]]
            right_side_of_window += 1
        return result


def test_edge_cases():
    solution = Solution()
    assert solution.maxSlidingWindow([0], 1) == [0]
    assert solution.maxSlidingWindow([0, 1], 1) == [0, 1]
    assert solution.maxSlidingWindow([0, 1, 2], 1) == [0, 1, 2]
    assert solution.maxSlidingWindow([0, 1], 2) == [1]
    assert solution.maxSlidingWindow([0, 1, 2], 2) == [1, 2]
    assert solution.maxSlidingWindow([0, 1, 2], 3) == [2]
    assert solution.maxSlidingWindow([0, 1, 2, 3], 2) == [1, 2, 3]
    assert solution.maxSlidingWindow([0, 1, 2, 3], 3) == [2, 3]
    assert solution.maxSlidingWindow([0, 1, 2, 3], 4) == [3]


def test_wa_1():
    solution = Solution()
    assert solution.maxSlidingWindow([7, 2, 4], 2) == [7, 4]


def test_random():
    nums = []
    k = 50
    for i in range(100):
        nums.append(random.randint(-10 ** 4, 10 ** 4))
    correct_answer = [max(nums[i: i + k]) for i in range(len(nums) - k + 1)]
    assert Solution().maxSlidingWindow(nums, k) == correct_answer


def test_large():
    solution = Solution()
    assert solution.maxSlidingWindow(list(range(10000)), 2) == list(range(1, 10000))
    assert solution.maxSlidingWindow(list(range(10000)), 3) == list(range(2, 10000))
    assert solution.maxSlidingWindow(list(range(10000)), 4) == list(range(3, 10000))
    assert solution.maxSlidingWindow(list(range(10000)), 5) == list(range(4, 10000))
    assert solution.maxSlidingWindow(list(range(10000)), 6) == list(range(5, 10000))
    assert solution.maxSlidingWindow(list(range(10000)), 20) == list(range(19, 10000))
    assert solution.maxSlidingWindow(list(range(10000)), 21) == list(range(20, 10000))
    assert solution.maxSlidingWindow(list(range(10000)), 50) == list(range(49, 10000))
    assert solution.maxSlidingWindow(list(range(10000)), 100) == list(range(99, 10000))
    assert solution.maxSlidingWindow(list(range(10000)), 1000) == list(range(999, 10000))
    assert solution.maxSlidingWindow(list(range(10 ** 5)), 10 ** 4) == list(range(10 ** 4 - 1, 10 ** 5))
    assert solution.maxSlidingWindow(list(range(10 ** 5)), 10 ** 3) == list(range(10 ** 3 - 1, 10 ** 5))
    assert solution.maxSlidingWindow(list(range(10 ** 5)), 10 ** 2) == list(range(10 ** 2 - 1, 10 ** 5))
    assert solution.maxSlidingWindow(list(range(10000, -9995, -1)), 10007)


def test_examples():
    solution = Solution()
    assert solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert solution.maxSlidingWindow([1], 1) == [1]
