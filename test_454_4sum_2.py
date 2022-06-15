from collections import Counter
from functools import cache


def fourSumCount(nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
    """Given four integer arrays nums1, nums2, nums3, and nums4 all of length n,
    return the number of tuples (i, j, k, l) such that:
    0 <= i, j, k, l < n
    nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
    """
    counter1 = Counter(nums1)
    counter2 = Counter(nums2)
    counter3 = Counter(nums3)
    counter4 = Counter(nums4)

    @cache
    def twoSumCount(num_3_plus_num_4: int):
        """
        :param num_3_plus_num_4 = num3+num4, where num3 is from nums3 and num4 is from nums4
        :returns number of elements num1 from nums1 and num2 from nums2 such that
        num1 + num2 + sum_3_and_4 = 0
        num1 = -(num2 + sum_3_and_4)"""
        count = 0
        for num2, num_count2 in counter2.items():
            count += counter1.get(-(num_3_plus_num_4 + num2), 0) * num_count2
        return count

    global_count = 0

    for num4, num_count4 in counter4.items():
        for num3, num_count3 in counter3.items():
            global_count += twoSumCount(num3 + num4) * num_count3 * num_count4
    return global_count


def test_edge_cases():
    assert fourSumCount([1], [1], [-1], [-1]) == 1
    assert fourSumCount([1], [1], [1], [-1]) == 0
    assert fourSumCount([0], [0], [1], [-1]) == 1
    assert fourSumCount([0, 1], [0, 1], [0, 1], [0, 1]) == 1
    assert fourSumCount([0, 1], [0, 1], [0, 1], [0, -1]) == 4
    assert fourSumCount([0, 0], [2, 2], [2, -2], [0, 1]) == 4


def test_large():
    assert fourSumCount([2 ** 28], [2 ** 28], [-2 ** 28], [-2 ** 28]) == 1


def test_examples():
    assert fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2
    assert fourSumCount([0], [0], [0], [0]) == 1
