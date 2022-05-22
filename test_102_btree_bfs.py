from typing import Optional


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """Given the root of a binary tree,
        return the level order traversal of its nodes' values.
        (i.e., from left to right, level by level)."""
        if not root:
            return []
        list_of_levels_of_values: list[list[int]] = []
        cur_level_of_nodes: list[TreeNode] = [root]
        while cur_level_of_nodes:
            # add values from current level
            vals_from_cur_level = []
            for node in cur_level_of_nodes:
                vals_from_cur_level.append(node.val)
            list_of_levels_of_values.append(vals_from_cur_level)
            # schedule next level
            next_nodes_level = []
            for node in cur_level_of_nodes:
                if node.left:
                    next_nodes_level.append(node.left)
                if node.right:
                    next_nodes_level.append(node.right)
            cur_level_of_nodes = next_nodes_level
        return list_of_levels_of_values


def test_corner_cases():
    s = Solution()
    assert s.levelOrder(TreeNode(0,
                                 TreeNode(1))) == [[0], [1]]
    assert s.levelOrder(TreeNode(0,
                                 None,
                                 TreeNode(1))) == [[0], [1]]
    assert s.levelOrder(TreeNode(0,
                                 TreeNode(1),
                                 TreeNode(2))) == [[0], [1, 2]]
    assert s.levelOrder(TreeNode(0,
                                 TreeNode(1),
                                 TreeNode(2,
                                          TreeNode(3)))) == [[0], [1, 2], [3]]


def test_examples():
    s = Solution()
    assert s.levelOrder(None) == []
    assert s.levelOrder(TreeNode(1)) == [[1]]
    assert s.levelOrder(TreeNode(3,
                                 TreeNode(9),
                                 TreeNode(20,
                                          TreeNode(15),
                                          TreeNode(7)))) == [[3], [9, 20], [15, 7]]
