def longestConsecutive(nums: list[int]) -> int:
    """Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
    You must write an algorithm that runs in O(n) time."""
    if len(nums) == 0:
        return 0
    nums_set = set(nums)
    global_max = 1
    while len(nums_set) > global_max:
        num = nums_set.pop()
        cur_seq_len = 1
        for k in range(1, 10**6):
            if (num + k) in nums_set:
                nums_set.remove(num+k)
            else:
                cur_seq_len += k-1
                break
        for k in range(1, 10**6):
            if (num - k) in nums_set:
                nums_set.remove(num-k)
            else:
                cur_seq_len += k-1
                break
        global_max = max(cur_seq_len, global_max)
    return global_max


def test_edge_cases():
    assert longestConsecutive([1, 2, 3, 4]) == 4
    assert longestConsecutive([4, 1, 3, 2]) == 4
    assert longestConsecutive([]) == 0
    assert longestConsecutive([1, 2]) == 2
    assert longestConsecutive([1, 3]) == 1
    assert longestConsecutive([1, 2, 4]) == 2
    assert longestConsecutive([1,5,2,4,6]) == 3
    assert longestConsecutive([0,-1]) == 2


def test_examples():
    assert longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
