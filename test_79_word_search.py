def exist(board: list[list[str]], word: str) -> bool:
    """Given an m x n grid of characters board and a string word, return true if word exists in the grid.
    The word can be constructed from letters of sequentially adjacent cells,
    where adjacent cells are horizontally or vertically neighboring.
    The same letter cell may not be used more than once.
    1 <= m, n <= 6
    1 <= word.length <= 15"""

    # 1. find all start positions
    # 2. start DFS from each position
    # 3. Reverse the word if it starts with long repeating sequence

    def check_word_DFS(row: int, col: int, letter_index, word) -> bool:
        if word[letter_index] != board[row][col]:
            return False
        if letter_index == len(word) - 1:
            return True
        tmp = board[row][col]
        board[row][col] = '*'
        candidate_neighbors = [(row + 1, col), (row - 1, col), (row, col - 1), (row, col + 1)]
        neighbors = [(row, col) for (row, col) in candidate_neighbors if 0 <= row < nrows and 0 <= col < ncols]
        for neighbor_row, neighbor_col in neighbors:
            # check if neighbor is the same as next letter. At the same time it should not be in prefix already.
            if check_word_DFS(neighbor_row, neighbor_col, letter_index + 1, word):
                return True
        board[row][col] = tmp
        return False

    nrows = len(board)
    ncols = len(board[0])
    # reverse the word, if first 6 characters are the same
    reference_word = word
    if len(word) >= 6 and all(char == word[0] for char in word[:6]):
        reference_word = word[::-1]
    for row in range(nrows):
        for col in range(ncols):
            if check_word_DFS(row, col, 0, reference_word):
                return True
    return False


def test_edge_cases():
    assert exist([['A']], 'A')
    assert not exist([['B']], 'A')
    assert exist([['A'], ['B']], 'A')
    assert exist([['A', 'B'], ['C', 'A']], 'A')
    assert exist([['A', 'B'], ['C', 'D']], 'D')
    assert not exist([['A', 'B'], ['C', 'D']], 'E')


def test_2d():
    assert exist([['a', 'b'], ['b', 'a']], 'a')
    assert exist([['a', 'b'], ['b', 'a']], 'b')
    assert exist([['a', 'b'], ['b', 'a']], 'ab')
    assert exist([['a', 'b'], ['b', 'a']], 'ba')
    assert exist([['a', 'b'], ['a', 'b']], 'baab')
    assert exist([['a', 'b'], ['a', 'b']], 'aabb')
    assert not exist([['a', 'b'], ['b', 'a']], 'c')
    assert exist([['a', 'b'], ['a', 'b']], 'abba')
    assert exist([['a', 'b'],
                  ['b', 'a']], 'abab')


def test_3d():
    assert exist([['a', 'b', 'c'],
                  ['b', 'a', 'd'],
                  ['c', 'b', 'c']], 'abcdcbabc')
    assert not exist([['a', 'b', 'c'],
                      ['b', 'a', 'd'],
                      ['c', 'b', 'c']], 'abcdcbaba')


def test_examples():
    assert exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
    assert exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
    assert exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE")
    assert not exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB")


def test_tla():
    assert not exist([["A", "A", "A", "A", "A", "A"],
                      ["A", "A", "A", "A", "A", "A"],
                      ["A", "A", "A", "A", "A", "A"],
                      ["A", "A", "A", "A", "A", "A"],
                      ["A", "A", "A", "A", "A", "B"],
                      ["A", "A", "A", "A", "B", "A"]], "AAAAAAAAAAAAABB")
