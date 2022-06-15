from collections import Counter


def partitionLabels(s: str) -> list[int]:
    """You are given a string s. We want to partition the string into as many parts as possible
    so that each letter appears in at most one part.
    Note that the partition is done so that after concatenating all the parts in order,
    the resultant string should be s.
    Return a list of integers representing the size of these parts."""
    # by default each symbol is
    get_partition_number = [len(s)] * len(s)
    # partitition = 'a' -> partition_number
    get_partition_start: dict[str, int] = dict()
    cur_partition_number = 0
    for i, char in enumerate(s):
        # new symbol
        if char not in get_partition_start:
            get_partition_start[char] = i
            cur_partition_number += 1
            get_partition_number[i] = cur_partition_number
            continue
        partition_start = get_partition_start[char]
        cur_partition_number = get_partition_number[partition_start]
        # merge partitions. put partition number = cur_number everywhere from partition_start
        # [0,0,2,3,4,2] -> [0,0,2,2,2,2]. Here 3, 4 are replaced by 2
        for j in reversed(range(partition_start + 1, i + 1)):
            if get_partition_number[j] == cur_partition_number:
                break
            get_partition_number[j] = cur_partition_number
    # compute the answer
    return list(Counter(get_partition_number).values())


def test_edge_cases():
    assert partitionLabels('a') == [1]
    assert partitionLabels('ab') == [1, 1]
    assert partitionLabels('abcd') == [1, 1, 1, 1]
    assert partitionLabels('abcda') == [5]
    assert partitionLabels('abcba') == [5]
    assert partitionLabels('abcbe') == [1, 3, 1]
    assert partitionLabels('abc') == [1, 1, 1]
    assert partitionLabels('abcabc') == [6]
    assert partitionLabels('aa') == [2]
    assert partitionLabels('aab') == [2, 1]
    assert partitionLabels('aabb') == [2, 2]
    assert partitionLabels('aacbb') == [2, 1, 2]
    assert partitionLabels('aaacbbddd') == [3, 1, 2, 3]


def test_case_tricky():
    assert partitionLabels('aabcb') == [2, 3]
    assert partitionLabels('aabbccddccb') == [2, 9]
    assert partitionLabels('aaabbbcccb') == [3, 7]


def test_examples():
    assert partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert partitionLabels("eccbbbbdec") == [10]
