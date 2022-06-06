from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    """Given the root of a binary tree, return the length of the diameter of the tree.
    The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
    This path may or may not pass through the root."""
    diameter = 0

    def max_depth(node: Optional[TreeNode]) -> int:
        nonlocal diameter
        left_path_depth = 1 + max_depth(node.left) if node.left else 0
        right_path_depth = 1 + max_depth(node.right) if node.right else 0
        # update diameter
        diameter = max(diameter,
                       left_path_depth + right_path_depth)
        # return depth
        return max(left_path_depth, right_path_depth)

    max_depth(root)
    return diameter


def test_edge_cases():
    assert diameterOfBinaryTree(list_to_btree([1, None, 2])) == 1
    assert diameterOfBinaryTree(list_to_btree([1, 2, 3])) == 2
    assert diameterOfBinaryTree(list_to_btree([1, None, 2, None, None, 3, None])) == 2
    assert diameterOfBinaryTree(list_to_btree([1, None, 2, None, None, 3, 4])) == 2
    assert diameterOfBinaryTree(TreeNode(1,
                                         None,
                                         TreeNode(2,
                                                  TreeNode(3,
                                                           TreeNode(5)),
                                                  TreeNode(4,
                                                           TreeNode(6))))) == 4
    assert diameterOfBinaryTree(list_to_btree([0])) == 0


def test_examples():
    assert diameterOfBinaryTree(list_to_btree([1, 2, 3, 4, 5])) == 3
    assert diameterOfBinaryTree(list_to_btree([1, 2, None])) == 1


def list_to_btree(nums: list[Optional[int]]) -> TreeNode:
    def recursive_list_to_btree(nums: list[Optional[int]], index: int) -> Optional[TreeNode]:
        """index = 1 for root,
        index = 2 for left child,
        index = 3 for right child"""
        i = index - 1
        if nums[i] is None:
            return None
        root = TreeNode(nums[i])
        if 2 * index < len(nums):
            root.left = recursive_list_to_btree(nums, 2 * index)
            root.right = recursive_list_to_btree(nums, 2 * index + 1)
        return root

    return recursive_list_to_btree(nums, 1)
