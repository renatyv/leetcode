class Trie:
    class _Node:
        def __init__(self, is_terminal: bool = False, children: dict = None):
            if children is None:
                self.children = dict()
            self.is_terminal = is_terminal

    def __init__(self):
        self._head = Trie._Node(False)

    def insert(self, word: str) -> None:
        """ Inserts the string word into the trie."""
        if not word:
            self._head.is_terminal = True
        else:
            cur_node = self._head
            for char in word:
                if char not in cur_node.children:
                    cur_node.children[char] = Trie._Node()
                cur_node = cur_node.children[char]
            cur_node.is_terminal = True

    def search(self, word: str) -> bool:
        """
        :returns true if the string word is in the trie (i.e., was inserted before),
                false otherwise."""
        if word == '':
            return self._head.is_terminal
        cur_node = self._head
        try:
            for char in word:
                cur_node = cur_node.children[char]
            return cur_node.is_terminal
        except KeyError:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        :returns true if there is a previously inserted string word that has the prefix,
                false otherwise."""
        if prefix == '':
            return not (self._head.children is None)
        try:
            cur_node = self._head
            for char in prefix:
                cur_node = cur_node.children[char]
        except KeyError:
            return False
        else:
            return True


def test_examples():
    trie = Trie()
    inserted_words = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    for word in inserted_words:
        trie.insert(word)
    for word in inserted_words:
        assert trie.search(word)
    assert not trie.search("T")
    assert not trie.search("Tri")
    assert not trie.search("search2")
    assert not trie.search("")
    assert trie.startsWith('Tr')
    assert trie.startsWith('search')
    assert trie.startsWith('startsWith')
    assert trie.startsWith('startsWit')
    assert trie.startsWith('s')
