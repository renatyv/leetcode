import copy


def solveNQueens(n: int) -> list[list[str]]:
    """The n-queens puzzle is the problem of placing n queens on an n x n chessboard
    such that no two queens attack each other.
    Given an integer n, return all distinct solutions to the n-queens puzzle.
    You may return the answer in any order.
    Each solution contains a distinct board configuration of the n-queens' placement,
    where 'Q' and '.' both indicate a queen and an empty space, respectively.
    1) Keep set of free (not under attack) positions for each row
    2) Put first queen on first available position in the row
    3) Remove all positions below queen which are under attack
    4) Continue with the next queen on the next row"""
    resulting_combinations = []

    def recursive(available_columns_in_row: dict[int, set[int]],
                  queen_row: int,
                  current_combination: list[int]):
        nonlocal resulting_combinations
        # if we are at the last row, return the result
        if queen_row == n - 1:
            for available_col in available_columns_in_row[queen_row]:
                resulting_combinations.append(current_combination + [available_col])
            return
        # find next available position position
        for queen_column in available_columns_in_row[queen_row]:
            # remove positions below and 'diagonally below' from sets of available elements
            put_back_positions: set[tuple[int, int]] = set()
            for row_delta in range(1, n - queen_row):
                row = queen_row + row_delta
                for col in [queen_column, queen_column - row_delta, queen_column + row_delta]:
                    if col in available_columns_in_row[row]:
                        # save positions which are under attack to put them back later
                        put_back_positions.add((row, col))
                        # remove from list of available
                        available_columns_in_row[row].discard(col)
            # check the queen in the next row
            recursive(available_columns_in_row,
                      queen_row + 1,
                      current_combination + [queen_column])
            # put back positions which are not under attack anymore
            for row, col in put_back_positions:
                available_columns_in_row[row].add(col)

    available_columns_in_row: dict[int, set[int]] = {row: {x for x in range(n)} for row in range(n)}
    recursive(available_columns_in_row, 0, [])

    resulting_matricies = []
    for combination in resulting_combinations:
        current_matrix = []
        for queen_position in combination:
            current_matrix.append('.' * (queen_position) + 'Q' + '.' * (n - queen_position - 1))
        resulting_matricies.append(current_matrix)

    return resulting_matricies


def test_corener_cases():
    assert solveNQueens(1) == [["Q"]]
    assert solveNQueens(2) == []
    assert solveNQueens(3) == []


def test_examples():
    assert solveNQueens(4) == [[".Q..",
                                "...Q",
                                "Q...",
                                "..Q."],
                               ["..Q.",
                                "Q...",
                                "...Q",
                                ".Q.."]]


def test_largest():
    assert solveNQueens(9) == []
