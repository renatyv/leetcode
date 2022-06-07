def solve(board: list[list[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """

    nrows = len(board)
    ncols = len(board[0])

    def dfs_mark_o_with_c(start_row: int, start_col: int, board: list[list[str]]):
        if board[start_row][start_col] != 'O':
            return
        board[start_row][start_col] = 'C'
        dfs_stack = [(start_row, start_col)]
        while dfs_stack:
            row, col = dfs_stack.pop()
            neighbor_candidates = [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]
            neighbors = [(r, c) for (r, c) in neighbor_candidates if 0 <= r < nrows and 0 <= c < ncols]
            for r, c in neighbors:
                if board[r][c] == 'O':
                    board[r][c] = 'C'
                    dfs_stack.append((r, c))

    # mark with 'C' all 'O' regions touching the borders
    for col in range(ncols):
        dfs_mark_o_with_c(0, col, board)
        dfs_mark_o_with_c(nrows - 1, col, board)
    for row in range(nrows):
        dfs_mark_o_with_c(row, 0, board)
        dfs_mark_o_with_c(row, ncols - 1, board)
    # mark with 'X' everything except 'C'
    # mark 'C' with 'O'
    for row in range(nrows):
        for col in range(ncols):
            if board[row][col] == 'C':
                board[row][col] = 'O'
            else:
                board[row][col] = 'X'


def test_edge_cases():
    board = [['O']]
    solve(board)
    assert board == [['O']]
    board = [['O', 'X']]
    solve(board)
    assert board == [['O', 'X']]
    board = [['O'], ['X']]
    solve(board)
    assert board == [['O'], ['X']]
    board = [['X', 'X'],
             ['X', 'X']]
    solve(board)
    assert board == [['X', 'X'],
                     ['X', 'X']]
    board = [['X', 'O'],
             ['X', 'X']]
    solve(board)
    assert board == [['X', 'O'],
                     ['X', 'X']]
    board = [["X", "X", "X"],
             ["X", "O", "O"],
             ["X", "O", "O"]]
    solve(board)
    assert board == [["X", "X", "X"],
                     ["X", "O", "O"],
                     ["X", "O", "O"]]
    board = [["X", "X", "X"],
             ["X", "O", "X"],
             ["X", "X", "X"]]
    solve(board)
    assert board == [["X", "X", "X"],
                     ["X", "X", "X"],
                     ["X", "X", "X"]]
    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "O", "O", "X"],
             ["X", "O", "X", "X"]]
    solve(board)
    assert board == [["X", "X", "X", "X"],
                     ["X", "O", "O", "X"],
                     ["X", "O", "O", "X"],
                     ["X", "O", "X", "X"]]


def test_examples():
    board = [["X", "X", "X", "X"],
             ["X", "O", "O", "X"],
             ["X", "X", "O", "X"],
             ["X", "O", "X", "X"]]
    solve(board)
    assert board == [["X", "X", "X", "X"],
                     ["X", "X", "X", "X"],
                     ["X", "X", "X", "X"],
                     ["X", "O", "X", "X"]]
    board = [['X']]
    solve(board)
    assert board == [['X']]
