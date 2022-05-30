from collections import deque
from typing import Optional, Deque


class TreeNode:
    def __init__(self, val=0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def btree_to_list(root: Optional[TreeNode]):
    def recursive_btree_to_list(root: Optional[TreeNode], index: int, level: int, btree_list: list[int]) -> list[int]:
        if index - 1 >= len(btree_list):
            btree_list += [None] * (2 ** level)
        btree_list[index - 1] = root.val
        if root.left:
            btree_list = recursive_btree_to_list(root.left, 2 * index, level + 1, btree_list)
        if root.right:
            btree_list = recursive_btree_to_list(root.right, 2 * index + 1, level + 1, btree_list)
        return btree_list

    return recursive_btree_to_list(root, 1, 0, [])


def maxPathSum(root: TreeNode) -> int:
    """
    A path in a binary tree is a sequence of nodes where
    each pair of adjacent nodes in the sequence has an edge connecting them.
    A node can only appear in the sequence at most once.
    Note that the path does not need to pass through the root.
    The path sum of a path is the sum of the node's values in the path.
    Given the root of a binary tree, return the maximum path sum of any non-empty path.
    Idea:
    Use recursion.
    1) Compute max sum for paths starting at left node
    2) Compute max sum for paths starting at right node
    3) Maxp path starting from root is either a path going though left or right node
    Update the required max path sum on each step: it is either left, or right, or left + root.val + right
    """
    global_max_path_sum = -1001

    # contains pairs (max path sum ending at parent, tree node)
    def recursive_max_path_sum_starting_from_root(root: Optional[TreeNode]):
        nonlocal global_max_path_sum
        if root is None:
            return 0
        # if path starting from left node is negative, don't go there
        max_path_sum_from_left = max(0, recursive_max_path_sum_starting_from_root(root.left))
        # if path starting from right node is negative, don't go there
        max_path_sum_from_right = max(0, recursive_max_path_sum_starting_from_root(root.right))
        global_max_path_sum = max(global_max_path_sum,
                                  max_path_sum_from_left + root.val + max_path_sum_from_right)
        return max(max_path_sum_from_left, max_path_sum_from_right) + root.val

    recursive_max_path_sum_starting_from_root(root)
    return global_max_path_sum


def test_edge_cases():
    btree = [1]
    assert maxPathSum(list_to_btree(btree)) == 1
    btree = [-1]
    assert maxPathSum(list_to_btree(btree)) == -1
    btree = [-1, 2, -1]
    assert maxPathSum(list_to_btree(btree)) == 2
    btree = [1, 2, -3]
    assert maxPathSum(list_to_btree(btree)) == 3
    btree = [1, -2, -3]
    assert maxPathSum(list_to_btree(btree)) == 1


def test_examples():
    btree = [1, 2, 3]
    assert maxPathSum(list_to_btree(btree)) == 6
    btree = [-10, 9, 20, None, None, 15, 7]
    assert maxPathSum(list_to_btree(btree)) == 42


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


def test_recursive_list_to_btree():
    btree = list_to_btree([0])
    assert btree.left is None and btree.right is None and btree.val == 0
    btree = list_to_btree([0, 1, 2])
    assert btree.left.val == 1
    assert btree.right.val == 2
    assert btree.val == 0
    btree = list_to_btree([0, None, 2, None, None, None, 4])
    assert btree.left is None and btree.right.val == 2 and btree.val == 0 and btree.right.right.val == 4
