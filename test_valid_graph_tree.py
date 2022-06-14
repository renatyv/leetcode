def valid_tree(n: int, edges: list[list[int]]) -> bool:
    """
    solution: https://iq.opengenus.org/union-find/
    :param n: number of nodes in a graph
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

    # union-find data structure to store disjoint sets
    # parents[child] == parent
    # parents[root] == root
    parents = list(range(n))

    def find_root_compressing_paths(parents: list[int], node: int) -> int:
        """find root starting from the node with path compression"""
        path = [node]
        # find root saving the path
        while parents[path[-1]] != path[-1]:
            path.append(parents[path[-1]])
        root = path[-1]
        # compress path to root
        for node in path:
            parents[node] = root
        return root

    for edge in edges:
        node1, node2 = edge
        # find roots for node1 and node2
        node1_root = find_root_compressing_paths(parents, node1)
        node2_root = find_root_compressing_paths(parents, node2)
        # if they are already in a tree, then there must be a cycle
        if node1_root == node2_root:
            return False
        # Union trees into one
        parents[node2_root] = node1_root
    # there are no cycles and number of edges == number of nodes -1
    return True


def test_edge_cases():
    assert valid_tree(1, [])
    assert not valid_tree(1, [[0, 0]])
    assert valid_tree(2, [[0, 1]])
    assert not valid_tree(2, [[0, 1], [1, 0]])
    assert not valid_tree(2, [[0, 0], [1, 0]])
    assert not valid_tree(8, [[0, 1], [0, 2], [2, 3], [3, 0], [0, 5], [0, 6], [7, 0]])


def test_wa1():
    assert valid_tree(8, [[0, 1], [0, 2], [3, 0], [4, 0], [0, 5], [0, 6], [7, 0]])


def test_examples():
    assert valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    assert not valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
