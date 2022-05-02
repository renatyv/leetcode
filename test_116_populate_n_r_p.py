from typing import Optional


class Node:
    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return str(self.val)


def connect(root: Optional[Node]) -> Optional[Node]:
    """You are given a perfect binary tree where all leaves are on the same level,
    and every parent has two children.
    Populate each next pointer to point to its next right node.
    If there is no next right node, the next pointer should be set to None.
    Initially, all next pointers are set to None."""
    if root is None:
        return root
    cur_level_leftmost_node = root
    while cur_level_leftmost_node.left:
        cur_level_leftmost_node.left.next = cur_level_leftmost_node.right
        cur_node = cur_level_leftmost_node
        while cur_node.next:
            # right element to next tree
            cur_node.right.next = cur_node.next.left
            cur_node = cur_node.next
            cur_node.left.next = cur_node.right
        #  work on next level
        cur_level_leftmost_node = cur_level_leftmost_node.left
    return root


def test_connect_example_1():
    tree = Node(1,
                Node(2, Node(4), Node(5)),
                Node(3, Node(6), Node(7)),
                None)
    connect(tree)
    assert tree.left.next == tree.right
    assert tree.left.right.next == tree.right.left


def test_connect_example_2():
    tree = None
    connect(tree)
    assert tree is None
