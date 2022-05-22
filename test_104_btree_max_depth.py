from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    """Given the root of a binary tree, return its maximum depth.
    A binary tree's maximum depth is
    the number of nodes along the longest path from the root node down to the farthest leaf node.
    Idea: BFS or recursive"""
    if root is None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1


def test_examples():
    tree = TreeNode(3,
                    TreeNode(9),
                    TreeNode(20,
                             TreeNode(15),
                             TreeNode(7)))
    assert maxDepth(tree) == 3
    assert maxDepth(tree.right) == 2
    assert maxDepth(tree.right.right) == 1
    assert maxDepth(tree.left) == 1
    assert maxDepth(tree.left.left) == 0
