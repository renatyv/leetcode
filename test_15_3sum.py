def threeSum(nums: list[int]) -> list[list[int]]:
    """Given an integer array nums, return all the triplets
    [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    Notice that the solution set must not contain duplicate triplets.

    Idea: solve using sorting + three pointers
    Optimization: binary search can be used"""

    sorted_nums: list[int] = nums.copy()
    sorted_nums.sort()
    resulting_list = []
    for i in range(len(sorted_nums)-2):
        # avoid duplicates. i never points to the same element twice
        if i != 0 and sorted_nums[i] == sorted_nums[i-1]:
            continue
        low = i+1
        high = len(sorted_nums) - 1
        while low < high:
            if sorted_nums[i] + sorted_nums[low] + sorted_nums[high] == 0:
                resulting_list.append([sorted_nums[i], sorted_nums[low], sorted_nums[high]])
                low += 1
                # avoid duplicates. low never points to the same element twice
                while low < high and sorted_nums[low] == sorted_nums[low-1]:
                    low += 1
            elif sorted_nums[low] + sorted_nums[high] + sorted_nums[i] < 0:
                low += 1
            else:
                high -= 1
    return resulting_list


def test_examples():
    assert threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert threeSum([]) == []
    assert threeSum([0]) == []
    assert threeSum([0,0,0]) == [[0,0,0]]
    assert threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]) == [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]
