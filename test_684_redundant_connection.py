from enum import Enum


def findRedundantConnection(edges: list[list[int]]) -> list[int]:
    """In this problem, a tree is an undirected graph that is connected and has no cycles.
    You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
    The added edge has two different vertices chosen from 1 to n,
    and was not an edge that already existed.
    The graph is represented as an array edges of length n where
    edges[i] = [ai, bi]
    indicates that there is an edge between nodes ai and bi in the graph.

    Return an edge that can be removed so that the resulting graph is a tree of n nodes.
    If there are multiple answers, return the answer that occurs last in the input.
    Idea: kruskal
    1) each node is a tree (a set of nodes)
    2) on each step join two trees using next edge"""
    trees: list[set[int]] = []
    for edge in edges:
        node1, node2 = edge
        node1_tree_index = -1
        node2_tree_index = -1
        for i, tree in enumerate(trees):
            if node1 in tree:
                node1_tree_index = i
                break
        for i, tree in enumerate(trees):
            if node2 in tree:
                node2_tree_index = i
                break
        if node1_tree_index == -1 and node2_tree_index == -1:
            trees.append({node1, node2})
        elif node1_tree_index == node2_tree_index:
            return edge
        elif node1_tree_index == -1:
            trees[node2_tree_index].add(node1)
        elif node2_tree_index == -1:
            trees[node1_tree_index].add(node2)
        else:
            trees[node2_tree_index] = trees[node2_tree_index].union(trees[node1_tree_index])
            del trees[node1_tree_index]
    return [-1, -1]


def test_edge_cases():
    assert findRedundantConnection([[1, 2], [2, 3], [3, 1]]) == [3, 1]
    assert findRedundantConnection([[1, 2], [3, 1], [2, 3]]) == [2, 3]
    assert findRedundantConnection([[1, 2],
                                    [2, 3], [3, 4], [4, 5], [5, 2],
                                    [4, 6], [5, 7]]) == [5, 2]
    assert findRedundantConnection([[1, 2],
                                    [2, 3], [3, 4], [5, 2],
                                    [4, 6], [5, 7], [4, 5]]) == [4, 5]


def test_examples():
    assert findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    assert findRedundantConnection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
