from typing import Optional


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """Given the root of a binary tree, determine if it is a valid binary search tree (BST).
        Idea: DFS is sorted"""
        dfs_traversal_list = []

        def list_elements_dfs(root: Optional[TreeNode]) -> list[int]:
            """Traverse BST in ascending order:
            left subtree, current node, right subtree"""
            if root is None:
                return []
            traversal_list = []
            if root.left:
                traversal_list = list_elements_dfs(root.left)
            traversal_list.append(root.val)
            if root.right:
                traversal_list += list_elements_dfs(root.right)
            return traversal_list

        dfs_list = list_elements_dfs(root)
        if len(dfs_list) == 1:
            return True
        # check that elements are in ascending order
        for i in range(1, len(dfs_list)):
            if dfs_list[i - 1] >= dfs_list[i]:
                return False
        return True


def test_corner_cases():
    s = Solution()
    assert s.isValidBST(TreeNode(1))
    assert s.isValidBST(None)
    assert s.isValidBST(TreeNode(1,
                                 TreeNode(0)))
    assert not s.isValidBST(TreeNode(1,
                                     TreeNode(2)))
    assert s.isValidBST(TreeNode(1,
                                 None,
                                 TreeNode(2)))
    assert not s.isValidBST(TreeNode(1,
                                     None,
                                     TreeNode(0)))
    assert s.isValidBST(TreeNode(1,
                                 TreeNode(0),
                                 TreeNode(2)))
    assert not s.isValidBST(TreeNode(1,
                                     TreeNode(2),
                                     TreeNode(0)))


def test_examples():
    s = Solution()
    assert s.isValidBST(TreeNode(2,
                                 TreeNode(1),
                                 TreeNode(3)))
    assert not s.isValidBST(TreeNode(5,
                                     TreeNode(1),
                                     TreeNode(4,
                                              TreeNode(3),
                                              TreeNode(6))))


def test_wa1():
    s = Solution()
    assert not s.isValidBST(TreeNode(5,
                                     TreeNode(4),
                                     TreeNode(6,
                                              TreeNode(3),
                                              TreeNode(7))))
