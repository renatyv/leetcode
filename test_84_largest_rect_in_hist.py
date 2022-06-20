class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        """Idea: use monotonically increasing stack"""

        # stores height indexes.
        # 1) for all i: monotonic_stack[i] < monotonic_stack[i+1]
        # 2) for all i: height[monotonic_stack[i]] < height[monotonic_stack[i+1]]
        # 3) for all i < x < i+1: height[monotonic_stack[x]] >= height[monotonic_stack[i]]

        def max_areas_for_rectangles_ending_at_i(heights: list[int]) -> list[int]:
            max_area_ending_at_index: list[int] = [-1] * len(heights)
            right = 0
            monotonic_stack: list[int] = []
            while right < len(heights):
                # keep monotonic stack structure.
                # Allows to find the closest rectangle to the left which is lower than current
                while monotonic_stack and heights[monotonic_stack[-1]] >= heights[right]:
                    # can not be extended further to the right, compute the answer
                    monotonic_stack.pop()
                # compute area of rectangle einding at index right
                if monotonic_stack:
                    last_lower_than_right = monotonic_stack[-1]
                    # the longest (to the left) rectangle ending at right with height heights[right]
                    width = right - last_lower_than_right
                    area_ending_at_right = width * heights[right]
                    # max area of rectangle with height heights[right]
                    max_area_ending_at_index[right] = max(heights[right],
                                                          area_ending_at_right)
                else:
                    # all heights before were larger:
                    width = right + 1
                    max_area_ending_at_index[right] = width * heights[right]
                monotonic_stack.append(right)
                right += 1
            return max_area_ending_at_index

        area_from_left = max_areas_for_rectangles_ending_at_i(heights)
        area_from_right = max_areas_for_rectangles_ending_at_i(heights[::-1])[::-1]
        # height[i] was count twice
        areas = [area_from_left + area_from_right - height for (area_from_left, area_from_right, height) in
                 zip(area_from_left, area_from_right, heights)]
        return max(areas)


def test_edge_cases():
    sol = Solution()
    assert sol.largestRectangleArea([0]) == 0
    assert sol.largestRectangleArea([0, 0]) == 0
    assert sol.largestRectangleArea([3]) == 3
    assert sol.largestRectangleArea([1, 0]) == 1
    assert sol.largestRectangleArea([1, 1]) == 2
    assert sol.largestRectangleArea([1, 2]) == 2
    assert sol.largestRectangleArea([1, 3]) == 3
    assert sol.largestRectangleArea([3, 2, 1]) == 4
    assert sol.largestRectangleArea([1, 2, 3, 2, 1]) == 6
    assert sol.largestRectangleArea([3, 2, 1, 2, 3]) == 5
    assert sol.largestRectangleArea([1, 2, 2, 1, 1, 1, 2, 2]) == 8


def test_examples():
    sol = Solution()
    assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert sol.largestRectangleArea([2, 4]) == 4
