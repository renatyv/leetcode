from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def listNode_to_list(head: Optional[ListNode]) -> list[int]:
    if not head:
        return []
    resulting_list = []
    cur_node = head
    while cur_node:
        resulting_list.append(cur_node.val)
        cur_node = cur_node.next
    return resulting_list


def list_to_ListNode(l: list[int]) -> Optional[ListNode]:
    if not l:
        return None
    head = ListNode(l[0])
    cur_node = head
    for num in l[1:]:
        cur_node.next = ListNode(num)
        cur_node = cur_node.next
    return head


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    """Given the head of a singly linked list, reverse the list, and return the reversed list."""
    reversed_list_head = None
    cur_elem = head
    while cur_elem:
        new_reversed_head = ListNode(cur_elem.val)
        new_reversed_head.next = reversed_list_head
        reversed_list_head = new_reversed_head
        cur_elem = cur_elem.next
    return reversed_list_head


def test_examples():
    assert listNode_to_list(reverseList(list_to_ListNode([1,2,3,4,5]))) == [5,4,3,2,1]
    assert listNode_to_list(reverseList(list_to_ListNode([1,2]))) == [2,1]
    assert listNode_to_list(reverseList(list_to_ListNode([]))) == []
