from typing import Optional


class Solution:
    """Idea: use a prefix tree (trie)"""

    class TrieNode:
        def __init__(self):
            self.is_final = False
            self.prev: Optional[Solution.TrieNode] = None
            self.adjacent: dict[str, Solution.TrieNode] = {}

        def add_word(self, word: str):
            if not word:
                return
            cur_node: Solution.TrieNode = self
            for char in word:
                if char not in cur_node.adjacent:
                    cur_node.adjacent[char] = Solution.TrieNode()
                cur_node.adjacent[char].prev = cur_node
                cur_node = cur_node.adjacent[char]
            cur_node.is_final = True

        def remove_word_from_end(self, word):
            self.is_final = False
            cur_node = self
            i = len(word) - 1
            while i >= 0 and \
                    (not cur_node.is_final) and \
                    (not cur_node.adjacent) and \
                    cur_node.prev:
                del cur_node.prev.adjacent[word[i]]
                i -= 1
                cur_node = cur_node.prev

        def __str__(self):
            return ('F' if self.is_final else '') + '(' + ','.join(k + str(v) for (k, v) in self.adjacent.items()) + ')'

    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        trie = Solution.TrieNode()
        for word in words:
            trie.add_word(word)
        nrows = len(board)
        ncols = len(board[0])

        found_words: set[str] = set()

        def find_all_words_dfs(row: int, col: int, trie: Solution.TrieNode, cur_word: str):
            """Recursive Depth-First Search"""
            # mark as visited with symbol '.' to prevent self-intersection
            if row < 0 or row >= nrows \
                    or col < 0 or col >= ncols or \
                    board[row][col] not in trie.adjacent:
                return
            tmp = board[row][col]
            board[row][col] = '.'
            trie = trie.adjacent[tmp]
            new_word = cur_word + tmp
            if trie.is_final:
                found_words.add(new_word)
                trie.remove_word_from_end(new_word)
            # don't need to check for != '.', since symbol '.' does not belong to any word
            find_all_words_dfs(row + 1, col, trie, new_word)
            find_all_words_dfs(row - 1, col, trie, new_word)
            find_all_words_dfs(row, col + 1, trie, new_word)
            find_all_words_dfs(row, col - 1, trie, new_word)
            # put back the symbol
            board[row][col] = tmp

        # search for words starting from each symbol
        for row in range(nrows):
            for col in range(ncols):
                find_all_words_dfs(row, col, trie, '')
        return list(found_words)


def test_edge_cases():
    solution = Solution()
    assert solution.findWords([['a']], ['abcde', 'feg']) == []
    assert solution.findWords([['a']], ['a']) == ['a']
    assert solution.findWords([['a', 'a', 'a'],
                               ['a', 'a', 'a'],
                               ['a', 'a', 'a']], ['aaaa', 'aa', 'a']) == ['aaaa', 'aa', 'a']
    assert solution.findWords([['a']], ['e']) == []


def test_examples():
    solution = Solution()
    assert solution.findWords(
        board=[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
        words=["oath", "pea", "eat", "rain"]) == ["eat", "oath"]
    assert solution.findWords(board=[["a", "b"], ["c", "d"]], words=["abcb"]) == []
