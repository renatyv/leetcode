def deleteAndEarn(nums: list[int]) -> int:
    """Idea:
    1. compute cost: dict[num]-> number of points by deleting all elements equal to num
    2. get sorted list of distinct numbers: sorted_keys
    3. Solved subtask: if we have first n-1 numbers from sorted_keys, which of them should we take
    4. Carefully add n-th number using solutions for (n-1) keys and (n-2) keys"""
    if len(nums) == 1:
        return nums[0]
    cost = dict()
    for num in nums:
        if num in cost:
            cost[num] += num
        else:
            cost[num] = num
    sorted_keys = sorted(cost.keys())
    # number of points for given number of taken keys from sorted_taken
    # [(last key, sum of points)]
    taken: list[tuple[int,int]] = [(-2, 0),
                                   (sorted_keys[0], cost[sorted_keys[0]])]
    # should we tak next one or not?
    for num in sorted_keys[1:]:
        last_taken_num, last_sum = taken[-1]
        penult_num, penult_sum = taken[-2]
        if last_taken_num + 1 != num:
            # we can freely add next key
            new_last_taken_num = num
            new_sum = last_sum + cost[num]
        else:
            if penult_sum + cost[num] > last_sum :
                # do not take num, take previous value
                new_last_taken_num = num
                new_sum = penult_sum + cost[num]
            else:
                # take num, remove last element (take solution for taken_keys[-2] and add num)
                new_last_taken_num = last_taken_num
                new_sum = last_sum
        taken.append((new_last_taken_num, new_sum))
    _, final_sum = taken[-1]
    return final_sum


def test_deleteAndEarn_example_1():
    assert deleteAndEarn([3,4,2]) == 6


def test_deleteAndEarn_example_2():
    assert deleteAndEarn([2,2,3,3,3,4]) == 9


def test_deleteAndEarn_small():
    assert deleteAndEarn([1]) == 1
    assert deleteAndEarn([1,3]) == 4
    assert deleteAndEarn([1,2]) == 2
    assert deleteAndEarn([2,1]) == 2


def test_deleteAndEarn_3():
    assert deleteAndEarn([1, 3, 5]) == 9
    assert deleteAndEarn([1, 2, 3]) == 4
    assert deleteAndEarn([3, 2, 1]) == 4
    assert deleteAndEarn([1, 3, 2]) == 4
    assert deleteAndEarn([1, 5, 2]) == 7
    assert deleteAndEarn([1, 5, 4]) == 6
    assert deleteAndEarn([5, 2, 4]) == 7



def test_deleteAndEarn_4():
    assert deleteAndEarn([1, 2, 3, 3, 4]) == 7
    assert deleteAndEarn([1, 2, 2, 2, 3]) == 6
    assert deleteAndEarn([1, 1, 1, 2]) == 3
    assert deleteAndEarn([1, 2, 2, 2]) == 6
    assert deleteAndEarn([1, 1, 1, 1]) == 4


def test_test_5():
    assert deleteAndEarn([1, 1, 2, 2, 3]) == 5
    assert deleteAndEarn([1, 1, 2, 2, 3, 4, 4, 5, 5]) == 15
    assert deleteAndEarn([1, 1, 2, 2, 3, 4, 4, 5, 5]) == 15
    assert deleteAndEarn([1, 1, 2, 2, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 9]) == 61
    assert deleteAndEarn([8,3,4,7,6,6,9,2,5,8,2,4,9,5,9,1,5,7,1,4]) == 61
    assert deleteAndEarn([8, 3, 4, 7, 6, 6, 9, 2, 5, 8, 2, 4, 9, 5, 9, 1, 5, 7, 1]) == 61

