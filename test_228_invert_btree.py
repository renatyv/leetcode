from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


def test_example_1():
    tree = TreeNode(4,
                    TreeNode(2,
                             TreeNode(1),
                             TreeNode(3)),
                    TreeNode(7,
                             TreeNode(6),
                             TreeNode(9)))
    reversed_tree = invertTree(tree)
    assert reversed_tree.val == 4
    assert reversed_tree.left.val == 7
    assert reversed_tree.left.left.val == 9
    assert reversed_tree.left.right.val == 6
    assert reversed_tree.right.val == 2
    assert reversed_tree.right.left.val == 3
    assert reversed_tree.right.right.val == 1


def test_example_2():
    tree = TreeNode(2,
                    TreeNode(1),
                    TreeNode(3))
    reversed_tree = invertTree(tree)
    assert reversed_tree.val == 2
    assert reversed_tree.left.val == 3
    assert reversed_tree.right.val == 1
