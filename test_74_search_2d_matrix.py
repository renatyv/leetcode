def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    """Write an efficient algorithm that searches for a value target in an m x n integer matrix.
    This matrix has the following properties:
    1. Integers in each row are sorted from left to right.
    2. The first integer of each row is greater than the last integer of the previous row.

    Idea: 1. binary search for row
    2.binary search inside row
    """

    def binary_search_row(matrix: list[list[int]], target: int) -> list[int]:
        """returns row with the target if it is there"""
        if len(matrix) == 1:
            return matrix[0]
        left = 0
        right = len(matrix) - 1
        if matrix[1][0] == target:
            return matrix[1]
        # target is in the 0th row
        if matrix[1][0] > target:
            return matrix[0]
        # target is in the last row
        if matrix[-1][0] <= target:
            return matrix[-1]
        while left + 1 < right:
            pivot = left + (right - left) // 2
            if matrix[pivot][0] == target:
                return matrix[pivot]
            if matrix[pivot][0] > target:
                right = pivot
            else:
                left = pivot
        return matrix[left]

    def binary_search_in_row(row: list[int], target) -> bool:
        if row[0] == target or row[-1] == target:
            return True
        if row[0] > target or row[-1] < target:
            return False
        left, right = 0, len(row) - 1
        while left + 1 < right:
            pivot = left + (right - left) // 2
            if row[pivot] == target:
                return True
            if row[pivot] < target:
                left = pivot
            else:
                right = pivot
        return False

    return binary_search_in_row(binary_search_row(matrix, target), target)


def test_examples():
    assert searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3)
    assert not searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13)


def test_edge_cases():
    assert searchMatrix([[1]], 1)
    assert searchMatrix([[1], [2]], 2)
    assert searchMatrix([[1], [2], [3]], 2)
    assert searchMatrix([[-1], [-2], [2]], 2)
    assert not searchMatrix([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13]], -1)
    assert not searchMatrix([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13]], 14)


def test_my_examples():
    assert not searchMatrix([[0, 1, 2, 3, 4], [7, 8, 9], [10, 11, 12, 13]], 5)
    assert not searchMatrix([[0, 1, 2, 3, 4], [7, 8, 9], [11, 12, 13]], 10)
    assert searchMatrix([[0, 1, 2, 3, 4], [7, 8, 9], [10, 11, 12, 13]], 8)
    assert searchMatrix([[0, 1, 2, 3, 4], [7, 8, 9], [10, 11, 12, 13]], 4)
    assert searchMatrix([[0, 1, 2, 3, 4], [7, 8, 9], [10, 11, 12, 13]], 10)
    assert searchMatrix([[0, 1, 2, 3, 4], [7, 8, 9], [10, 11, 12, 13]], 13)
    assert searchMatrix([[0, 1, 2, 3, 4], [7, 8, 9], [10, 11, 12, 13]], 12)
    assert searchMatrix([[0, 1, 2, 3, 4], [7, 8, 9], [10, 11, 12, 13]], 11)


def test_wrong_answer_1():
    assert searchMatrix([[12, 14], [15, 16], [17, 19], [35, 36]], 16)
