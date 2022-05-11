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
    """Populate each next pointer to point to its next right node.
    If there is no next right node, the next pointer should be set to None.
    Initially, all next pointers are set to None.

    Idea: use .next to go over current row, modifying children"""
    if root is None:
        return None
    cur_node = root
    while cur_node:
        row_below: list[Node] = []
        while cur_node:
            if cur_node.left:
                row_below.append(cur_node.left)
            if cur_node.right:
                row_below.append(cur_node.right)
            cur_node = cur_node.next
        for i, node in enumerate(row_below[1:], start=1):
            row_below[i-1].next = node
        if row_below:
            cur_node = row_below[0]
    return root


def test_corner():
    tree = None
    assert connect(tree) is None


def test_example_1():
    tree = Node(1,
                Node(2, Node(4), Node(5)),
                Node(3, None, Node(7)),
                None)
    connect(tree)
    assert tree.left.next == tree.right
    assert tree.left.left.next == tree.left.right
    assert tree.left.right.next == tree.right.right


def test_example_2():
    tree = Node(1)
    connect(tree)
    assert tree.next is None and tree.left is None and tree.right is None


def test_example_3():
    tree = Node(1, Node(2), Node(3))
    connect(tree)
    assert tree.left.next == tree.right
