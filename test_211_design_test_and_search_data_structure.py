class WordDictionary:
    """Implements a trie(prefix tree)"""

    class _Node:
        def __init__(self, children=None, is_terminal: bool = False):
            if children is None:
                children = dict()
            self.children = children
            self.is_terminal = is_terminal

    def __init__(self):
        self._head = WordDictionary._Node(dict(), False)
        self._word_set = set()

    def addWord(self, word: str) -> None:
        cur_node = self._head
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = WordDictionary._Node()
            cur_node = cur_node.children[char]
        cur_node.is_terminal = True

    def search(self, word: str) -> bool:
        stack = [(self._head, 0)]
        while stack:
            node, char_index = stack.pop()
            if char_index == len(word):
                if node.is_terminal:
                    return True
                else:
                    continue
            if word[char_index] == '.':
                for child in node.children.values():
                    stack.append((child, char_index + 1))
            else:
                try:
                    stack.append((node.children[word[char_index]], char_index + 1))
                except KeyError:
                    continue
        return False

        # return search_recursive(self._head, word)


def test_a_trie():
    wdict = WordDictionary()
    added_words = ['I', 'Am', 'a', 'trie']
    for word in added_words:
        wdict.addWord(word)
    assert wdict.search('I')
    assert wdict.search('Am')
    assert wdict.search('a')
    assert wdict.search('.')
    assert wdict.search('trie')
    assert not wdict.search('')
    assert not wdict.search('As')
    assert wdict.search('A.')
    assert wdict.search('tr.e')
    assert not wdict.search('t.r.u')
    assert not wdict.search('t.r.ie')
