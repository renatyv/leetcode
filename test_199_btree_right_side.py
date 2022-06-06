from collections import deque
from typing import Optional, Deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def rightSideView(root: Optional[TreeNode]) -> list[int]:
    """Idea: BFS"""
    if root is None:
        return []
    right_side_view = []
    # deque of pairs (level, node)
    bfs_deque: Deque[tuple[int, TreeNode]] = deque([(0, root)])
    while bfs_deque:
        cur_level, node = bfs_deque.pop()
        if node.left:
            bfs_deque.appendleft((cur_level + 1, node.left))
        if node.right:
            bfs_deque.appendleft((cur_level + 1, node.right))
        if not bfs_deque or (bfs_deque and bfs_deque[-1][0] > cur_level):
            right_side_view.append(node.val)
    return right_side_view


def test_edge_cases():
    assert rightSideView(list_to_btree([1])) == [1]
    assert rightSideView(list_to_btree([1, 2, None])) == [1, 2]
    assert rightSideView(list_to_btree([1, None, 2])) == [1, 2]


def test_my_examples():
    root = list_to_btree([1,
                          2, 3,
                          4, None, None, None])
    assert rightSideView(root) == [1, 3, 4]
    root = list_to_btree([1,
                          2, None,
                          4, None, None, None])
    assert rightSideView(root) == [1, 2, 4]
    root = list_to_btree([1,
                          2, None,
                          4, 5, None, None])
    assert rightSideView(root) == [1, 2, 5]


def test_examples():
    assert rightSideView(None) == []
    assert rightSideView(list_to_btree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert rightSideView(list_to_btree([1, None, 3])) == [1, 3]


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
