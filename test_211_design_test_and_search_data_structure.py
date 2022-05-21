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

    def addWord(self, word: str) -> None:
        if not word:
            self._head.is_terminal = True
        else:
            char_index = 0
            cur_node = self._head
            try:
                # find prefix
                while char_index < len(word):
                    # raises KeyError if max prefix already found
                    cur_node = cur_node.children[word[char_index]]
                    char_index += 1
                cur_node.is_terminal = True
            except KeyError:
                # extend the trie with new characters
                while char_index < len(word):
                    new_node = WordDictionary._Node()
                    cur_node.children[word[char_index]] = new_node
                    cur_node = new_node
                    char_index += 1
                cur_node.is_terminal = True

    def search(self, word: str) -> bool:
        def search_recursive(node: WordDictionary._Node, word: str):
            if not word:
                return node.is_terminal
            # if not node.children:
            #     return False
            if word[0] == '.':
                return any(search_recursive(child,
                                            word[1:])
                           for child in node.children.values())
            try:
                return search_recursive(node.children[word[0]],
                                        word[1:])
            except KeyError:
                return False

        return search_recursive(self._head, word)


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
