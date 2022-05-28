def isValidSudoku(board: list[list[str]]) -> bool:
    """Determine if a 9 x 9 Sudoku board is valid.
    Only the filled cells need to be validated according to the following rules:
    Each row must contain the digits 1-9 without repetition.
    Each column must contain the digits 1-9 without repetition.
    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
    Idea: straightforward solution using sets"""
    nrows = len(board)
    ncols = len(board[0])
    row_sets = [set() for row in range(9)]
    col_sets = [set() for row in range(9)]
    square_sets = [[set() for col in range(3)] for row in range(3)]
    for row in range(nrows):
        for col in range(ncols):
            num = board[row][col]
            if num == '.':
                continue
            if num in row_sets[row]:
                return False
            if num in col_sets[col]:
                return False
            if num in square_sets[row // 3][ col // 3]:
                return False
            row_sets[row].add(num)
            col_sets[col].add(num)
            square_sets[row // 3][ col // 3].add(num)
    return True


def test_examples():
    assert isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                          ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                          ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                          ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                          ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                          [".", "6", ".", ".", ".", ".", "2", "8", "."],
                          [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                          [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
    assert not isValidSudoku([["8", "3", ".", ".", "7", ".", ".", ".", "."],
                              ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                              [".", "9", "8", ".", ".", ".", ".", "6", "."],
                              ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                              ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                              ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                              [".", "6", ".", ".", ".", ".", "2", "8", "."],
                              [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
