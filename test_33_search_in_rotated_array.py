def search(nums: list[int], target: int) -> int:
    """There is an integer array nums sorted in ascending order (with distinct values).
    Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k
    (1 <= k < nums.length) such that the resulting array is
    [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
    For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an integer target,
    return the index of target if it is in nums, or -1 if it is not in nums.
    You must write an algorithm with O(log n) runtime complexity.
    Idea: use modified binary search.
    m = min(nums)
    M = max(nums)
    l,r -- left and right indexes. Our target is somewhere inbetween
    p = (l+r)/2 -- in the middle
    [l................p...r], p > l, p < r, run standard binary search
    [l......t.....Mm..p...r], p < l, p < r, p < t, t > r    r := p
    [l.........Mm.p..t....r], p < l, p < r, p < t, t < r    l := p
    [l.........Mm....t.p..r], p < l, p < r, p > t, t < r    r := p
    [l....p....Mm....t....r], p > l, p > r, p > t, t < r    l := p
    [l......t..p..Mm......r], p > l, p > r, p > t, t > r    r := p
    [l...p..t.....Mm......r], p > l, p > r, p < t, t > r    l := p
    """

    def standard_binary_search(nums: list[int], target: int):
        left = 0
        right = len(nums) - 1
        while left + 1 < right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            if nums[pivot] > target:
                right = pivot
            else:
                left = pivot
        return -1

    if nums[0] == target:
        return 0
    if nums[-1] == target:
        return len(nums) - 1
    l = 0
    r = len(nums) - 1

    while l + 1 < r:
        # [l................p...r], p > l, p < r, run standard binary search
        if nums[l] < nums[r]:
            search_result = standard_binary_search(nums[l:r + 1], target)
            if search_result == -1:
                return -1
            return search_result + l
        p = l + (r - l) // 2
        if nums[p] == target:
            return p
        # [l......t.....Mm..p...r], p < l, p < r, p < t, t > r    r := p
        # [l.........Mm....t.p..r], p < l, p < r, p > t, t < r    r := p
        # [l......t..p..Mm......r], p > l, p > r, p > t, t > r    r := p
        if (nums[p] < nums[l] and nums[p] < nums[r] and nums[p] < target and target > nums[r]) \
                or (nums[p] < nums[l] and nums[p] < nums[r] and nums[p] > target and target < nums[r]) \
                or (nums[p] > nums[l] and nums[p] > nums[r] and nums[p] > target and target > nums[r]):
            r = p
        else:
            l = p
    return -1


def test_examples():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1


def test_corner():
    assert search([1, 3, 4, 5, 6], 2) == -1
    assert search([1], 1) == 0
    assert search([1, 2, 3, 4, 5], 5) == 4
    assert search([1, 2, 3, 4, 5], 1) == 0
    assert search([1, 2, 3, 4, 5], 2) == 1
    assert search([1, 2, 3, 4, 5], 4) == 3


def test_failed_1():
    assert search([5, 1, 2, 3, 4], 1) == 1
