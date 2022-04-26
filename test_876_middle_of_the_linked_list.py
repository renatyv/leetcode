from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    """Given the head of a singly linked list, return the middle node of the linked list.
    If there are two middle nodes, return the second middle node."""
    cur_node: Optional[ListNode] = head
    middle_node: Optional[ListNode] = head
    move_middle: bool = False
    while cur_node:
        cur_node = cur_node.next
        if move_middle:
            middle_node = middle_node.next
        move_middle = not move_middle
    return middle_node


def list_to_ListNode(nodes: list) -> Optional[ListNode]:
    if not nodes:
        return None
    head = ListNode(nodes[0],None)
    cur_node = head
    for node in nodes[1:]:
        cur_node.next = ListNode(node, None)
        cur_node = cur_node.next
    return head


def listNode_to_list(head = Optional[ListNode]) -> list[int]:
    cur_node: Optional[ListNode] = head
    resulting_list = []
    while cur_node:
        resulting_list.append(cur_node.val)
        cur_node = cur_node.next
    return resulting_list


def test_list_converters():
    assert listNode_to_list(list_to_ListNode([1])) == [1]
    assert listNode_to_list(list_to_ListNode([1,2])) == [1,2]
    assert listNode_to_list(list_to_ListNode([1,2,3])) == [1,2,3]


def test_examples():
    assert listNode_to_list(middleNode(list_to_ListNode([1,2,3,4,5]))) == [3,4,5]
    assert listNode_to_list(middleNode(list_to_ListNode([1,2,3,4,5,6]))) == [4,5,6]


def test_middleNode_1():
    assert listNode_to_list(middleNode(list_to_ListNode([1]))) == [1]
    assert listNode_to_list(middleNode(list_to_ListNode([1, 2]))) == [2]
    assert listNode_to_list(middleNode(list_to_ListNode([1, 2, 3]))) == [2, 3]
