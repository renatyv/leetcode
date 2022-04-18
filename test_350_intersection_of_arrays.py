import pytest


def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    """Idea: count number of elements in nums1 using dict"""
    dict1 = dict()
    for num in nums1:
        if num in dict1:
            dict1[num] += 1
        else:
            dict1[num] = 1
    intersection = []
    for num in nums2:
        if num in dict1:
            intersection.append(num)
            dict1[num] -= 1
            if dict1[num] == 0:
                dict1.pop(num)
    return intersection


def test_intersect_empty():
    assert intersect([1], [2, 2]) == []
    assert intersect([2, 2], [1]) == []
    assert intersect([1, 2,3,4,5,6], [7,8,9,10,11]) == []


def test_intersect_the_same():
    res = intersect([1, 2], [2, 1])
    assert res == [1, 2] or res == [2,1]


def test_intersect_example_1():
    assert intersect([1, 2, 2, 1],[2,2]) == [2,2]


def test_intersect_example_2():
    res = intersect([9,4,5],[9,4,9,8,4])
    assert res == [9,4] or res == [4,9]
