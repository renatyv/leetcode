from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not isinstance(other, TreeNode):
            return False
        if other.val != self.val:
            return False
        return self.left == other.left and self.right == other.right


def merge_two_btrees(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
    """You are given two binary trees root1 and root2.
    Imagine that when you put one of them to cover the other, some nodes of the two trees
    are overlapped while the others are not.
    You need to merge the two trees into a new binary tree.
    The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
    Otherwise, the NOT null node will be used as the node of the new tree.
    Return the merged tree.

    Idea."""
    if not root1:
        return root2
    if not root2:
        return root1
    merge_result = TreeNode(root1.val + root2.val,
                            merge_two_btrees(root1.left, root2.left),
                            merge_two_btrees(root1.right, root2.right))
    return merge_result


def test_edge_cases():
    assert True


def test_example_1():
    tree1 = TreeNode(1,
                     TreeNode(3,
                              TreeNode(5)),
                     TreeNode(2))
    tree2 = TreeNode(2,
                     TreeNode(1,
                              None,
                              TreeNode(4)),
                     TreeNode(3,
                              None,
                              TreeNode(7)))
    tree3 = TreeNode(3,
                     TreeNode(4,
                              TreeNode(5),
                              TreeNode(4)),
                     TreeNode(5,
                              None,
                              TreeNode(7)))
    assert merge_two_btrees(tree1, tree2) == tree3


def test_example_2():
    tree1 = TreeNode(1)
    tree2 = TreeNode(1, TreeNode(2))
    tree3 = TreeNode(2, TreeNode(2))
    assert merge_two_btrees(tree1, tree2) == tree3
