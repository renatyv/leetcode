from typing import Optional


class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """Given two integer arrays preorder and inorder
        where preorder is the preorder traversal of a binary tree
        and inorder is the inorder traversal of the same tree,
        construct and return the binary tree.

        Pre-order, NLR
        # [root|left subtree|right subtree]

        In-order, LNR
        [left subtree|root|right subtree]"""
        inorder_positions_map = {}
        for pos, num in enumerate(inorder):
            inorder_positions_map[num] = pos

        def recursive_build_tree(preorder_left, preorder_right,
                                 inorder_left, inorder_right) -> TreeNode:
            nonlocal inorder
            nonlocal preorder
            nonlocal inorder_positions_map
            # in pre-order root is the first element
            root_val = preorder[preorder_left]
            root = TreeNode(root_val)
            # find root position in inorder array using hashmap
            inorder_root = inorder_positions_map[root_val]
            # compute length of left subtree
            left_length = inorder_root - inorder_left
            # compute length of right subtree
            right_length = inorder_right - inorder_root
            if left_length > 0:
                root.left = recursive_build_tree(preorder_left + 1, preorder_left + left_length,
                                                 inorder_left, inorder_left + left_length - 1)
            if right_length > 0:
                # [left subtree|root|right subtree]
                root.right = recursive_build_tree(preorder_right - right_length + 1, preorder_right,
                                                  inorder_root + 1, inorder_right)
            return root

        return recursive_build_tree(0, len(preorder) - 1, 0, len(inorder) - 1)


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


def test_btree_to_list():
    assert btree_to_list(TreeNode(1)) == [1]
    assert btree_to_list(TreeNode(1,
                                  TreeNode(2))) == [1, 2, None]
    assert btree_to_list(TreeNode(1,
                                  TreeNode(2),
                                  TreeNode(3))) == [1, 2, 3]
    assert btree_to_list(TreeNode(1,
                                  None,
                                  TreeNode(3))) == [1, None, 3]
    assert btree_to_list(TreeNode(1,
                                  None,
                                  TreeNode(3,
                                           None,
                                           TreeNode(4)))) == [1,
                                                              None, 3,
                                                              None, None, None, 4]


def test_corner_cases():
    s = Solution()
    tree = s.buildTree([1, 2, 3], [2, 1, 3])
    assert btree_to_list(tree) == [1, 2, 3]
    tree = s.buildTree([2, 1], [1, 2])
    assert btree_to_list(tree) == [2, 1, None]
    tree = s.buildTree([2, 1], [2, 1])
    assert btree_to_list(tree) == [2, None, 1]
    tree = s.buildTree([2], [2])
    assert btree_to_list(tree) == [2]
    tree = s.buildTree([1, 2, 3], [3, 2, 1])
    assert btree_to_list(tree) == [1, 2, None, 3, None, None, None]
    tree = s.buildTree([1, 2, 3], [1, 2, 3])
    assert btree_to_list(tree) == [1, None, 2, None, None, None, 3]
    tree = s.buildTree([1, 2, 3, 4, 5], [2, 3, 1, 5, 4])
    assert btree_to_list(tree) == [1, 2, 4, None, 3, 5, None]


def test_examples():
    s = Solution()
    tree = s.buildTree([3, 9, 20, 15, 7],
                       [9, 3, 15, 20, 7])
    assert btree_to_list(tree) == [3, 9, 20, None, None, 15, 7]
    tree = s.buildTree([-1], [-1])
    assert btree_to_list(tree) == [-1]
