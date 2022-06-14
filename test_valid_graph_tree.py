def valid_tree(n: int, edges: list[list[int]]) -> bool:
    """
    https://www.lintcode.com/problem/178/description
    Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes),
    write a function to check whether these edges make up a valid tree.
    Idea: Disjoint Set Union"""
    # init: each node is a tree
    # each tree is labeled with minimal node within it

    if len(edges) == 0:
        return n <= 1
    if len(edges) != n - 1:
        return False

    trees = [{k} for k in range(n)]

    def find_tree_index(trees: list[set[int]], node: int) -> int:
        for tree_index, tree in enumerate(trees):
            if node in tree:
                return tree_index

    for edge in edges:
        node1, node2 = edge
        # find tree for node1
        node1_tree_index = find_tree_index(trees, node1)
        node2_tree_index = find_tree_index(trees, node2)
        # cycle
        if node1_tree_index == node2_tree_index:
            return False
        # connect trees into one
        trees[node1_tree_index] = trees[node1_tree_index].union(trees[node2_tree_index])
        del trees[node2_tree_index]
    return len(trees) == 1


def test_edge_cases():
    assert valid_tree(1, [])
    assert not valid_tree(1, [[0, 0]])
    assert valid_tree(2, [[0, 1]])
    assert not valid_tree(2, [[0, 1], [1, 0]])
    assert not valid_tree(2, [[0, 0], [1, 0]])


def test_examples():
    assert valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    assert not valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
