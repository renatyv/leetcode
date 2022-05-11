from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """Given the roots of two binary trees root and subRoot,
    return true if there is a subtree of root with the same structure and node values of subRoot
    and false otherwise.
    A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants.
    The tree tree could also be considered as a subtree of itself.

    Idea: recursion"""

    def trees_equal(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None and tree2:
            return False
        if tree1 and tree2 is None:
            return False
        return tree1.val == tree2.val and \
               trees_equal(tree1.left, tree2.left) and \
               trees_equal(tree1.right, tree2.right)

    if trees_equal(root, subRoot):
        return True
    if root.left and isSubtree(root.left, subRoot):
        return True
    if root.right and isSubtree(root.right, subRoot):
        return True
    return False


def test_example_1():
    tree = TreeNode(3,
                    TreeNode(4,
                             TreeNode(1),
                             TreeNode(2)),
                    TreeNode(5))
    assert isSubtree(tree, TreeNode(4,
                                    TreeNode(1),
                                    TreeNode(2)))
    assert isSubtree(tree, TreeNode(2))
    assert isSubtree(tree, TreeNode(1))
    assert isSubtree(tree, TreeNode(5))
    assert isSubtree(tree, TreeNode(3,
                                    TreeNode(4,
                                             TreeNode(1),
                                             TreeNode(2)),
                                    TreeNode(5)))
    assert not isSubtree(tree, TreeNode(4))
    assert not isSubtree(tree, TreeNode(4, TreeNode(4), TreeNode(5)))
    assert not isSubtree(tree, TreeNode(4, TreeNode(4), TreeNode(5)))
