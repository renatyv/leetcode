def maxArea(height: list[int]) -> int:
    """Idea: Greedy.
    Container area (i,j) = width * height =  (j-i)*min(height[i], height[j])
    Start with widest container. Move left or right side if height can be increased."""
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        max_area = max(max_area,
                       (right - left) * min(height[right], height[left]))
        # take the smaller
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_area


def test_examples():
    assert maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert maxArea([1, 1]) == 1


def test_corner():
    assert maxArea([1, 1]) == 1
    assert maxArea([1, 2]) == 1
    assert maxArea([1, 2, 1]) == 2
    assert maxArea([2, 1, 1, 2]) == 6
