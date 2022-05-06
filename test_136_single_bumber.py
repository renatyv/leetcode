# def singleNumber(nums: list[int]) -> int:
#     """Given a non-empty array of integers nums, every element appears twice except for one.
#     Find that single one.
#     Idea: use hashset"""
#     nums_set = set()
#     for num in nums:
#         if num not in nums_set:
#             nums_set.add(num)
#         else:
#             nums_set.remove(num)
#     return nums_set.pop()


def singleNumber(nums: list[int]) -> int:
    """Given a non-empty array of integers nums, every element appears twice except for one.
    Find that single one.
    Idea: use XOR"""
    res = 0
    for num in nums:
        res = res ^ num
    return res


def test_singleNumber_examples():
    assert singleNumber([2,2,1]) == 1
    assert singleNumber([4,1,2,1,2]) == 4
    assert singleNumber([1]) == 1
