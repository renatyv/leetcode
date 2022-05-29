from typing import Optional

from test_143_reorder_list import list_to_ListNode, listNode_to_list, ListNode


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Given the head of a linked list, remove the nth node from the end of the list and return its head.
    Idea: skip first n, to find element to remove"""
    if head.next is None:
        return None
    pre_remove = ListNode(-1, head)
    tail = head
    for i in range(n-1):
        tail = tail.next
    # move both tail and pre_remove until the end
    while tail.next:
        tail = tail.next
        pre_remove = pre_remove.next
    # remove head
    if pre_remove.next == head:
        return head.next
    # remove the necessary element
    pre_remove.next = pre_remove.next.next
    return head


def test_corner_cases():
    head = list_to_ListNode([1])
    removed_nth_head = removeNthFromEnd(head, 1)
    assert listNode_to_list(removed_nth_head) == []
    head = list_to_ListNode([1, 2])
    removed_nth_head = removeNthFromEnd(head, 1)
    assert listNode_to_list(removed_nth_head) == [1]
    head = list_to_ListNode([1, 2])
    removed_nth_head = removeNthFromEnd(head, 2)
    assert listNode_to_list(removed_nth_head) == [2]
    head = list_to_ListNode([1, 2, 3])
    removed_nth_head = removeNthFromEnd(head, 1)
    assert listNode_to_list(removed_nth_head) == [1, 2]
    head = list_to_ListNode([1, 2, 3])
    removed_nth_head = removeNthFromEnd(head, 2)
    assert listNode_to_list(removed_nth_head) == [1, 3]
    head = list_to_ListNode([1, 2, 3])
    removed_nth_head = removeNthFromEnd(head, 3)
    assert listNode_to_list(removed_nth_head) == [2, 3]
    head = list_to_ListNode([1, 2, 3, 4])
    removed_nth_head = removeNthFromEnd(head, 1)
    assert listNode_to_list(removed_nth_head) == [1, 2, 3]
    head = list_to_ListNode([1, 2, 3, 4])
    removed_nth_head = removeNthFromEnd(head, 2)
    assert listNode_to_list(removed_nth_head) == [1, 2, 4]
    head = list_to_ListNode([1, 2, 3, 4])
    removed_nth_head = removeNthFromEnd(head, 3)
    assert listNode_to_list(removed_nth_head) == [1, 3, 4]
    head = list_to_ListNode([1, 2, 3, 4])
    removed_nth_head = removeNthFromEnd(head, 4)
    assert listNode_to_list(removed_nth_head) == [2, 3, 4]


def test_examples():
    head = list_to_ListNode([1])
    removed_nth_head = removeNthFromEnd(head, 1)
    assert listNode_to_list(removed_nth_head) == []
    head = list_to_ListNode([1, 2, 3, 4, 5])
    removed_nth_head = removeNthFromEnd(head, 2)
    assert listNode_to_list(removed_nth_head) == [1, 2, 3, 5]
    head = list_to_ListNode([1, 2])
    removed_nth_head = removeNthFromEnd(head, 1)
    assert listNode_to_list(removed_nth_head) == [1]
