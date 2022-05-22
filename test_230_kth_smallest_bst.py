# Definition for a binary tree node.
from typing import Optional, Union, Tuple


class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """Given the root of a binary search tree, and an integer k,
        return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
        1 <= k <= n <= 10^4"""
        cur_path: list[TreeNode] = []
        cur_node: Optional[TreeNode] = root
        while True:
            # go to the leftmost element
            while cur_node:
                cur_path.append(cur_node)
                cur_node = cur_node.left
            # take the leftomost out of current path, so that we will not check it in the future again
            leftmost = cur_path.pop()
            k -= 1
            if k == 0:
                return leftmost.val
            # check the right path
            cur_node = leftmost.right


def test_corner_cases():
    s = Solution()
    assert s.kthSmallest(TreeNode(2,
                                  TreeNode(1),
                                  TreeNode(3)), 1) == 1
    assert s.kthSmallest(TreeNode(2,
                                  TreeNode(1),
                                  TreeNode(3)), 2) == 2
    tree = TreeNode(2,
                    TreeNode(1),
                    TreeNode(3))
    assert s.kthSmallest(tree, 3) == 3


def test_cases_2():
    s = Solution()
    tree = TreeNode(3,
                    TreeNode(2,
                             TreeNode(1)),
                    TreeNode(4,
                             None,
                             TreeNode(5)))
    assert s.kthSmallest(tree, 1) == 1
    assert s.kthSmallest(tree, 2) == 2
    assert s.kthSmallest(tree, 3) == 3
    assert s.kthSmallest(tree, 4) == 4
    assert s.kthSmallest(tree, 5) == 5


def test_examples():
    s = Solution()
    assert s.kthSmallest(TreeNode(3,
                                  TreeNode(1,
                                           None,
                                           TreeNode(2)),
                                  TreeNode(4)), 1) == 1
    assert s.kthSmallest(TreeNode(5,
                                  TreeNode(3,
                                           TreeNode(2,
                                                    TreeNode(1)),
                                           TreeNode(4)),
                                  TreeNode(6)), 3) == 3
