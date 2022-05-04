from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists in a one sorted list.
    The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.

    Idea: use two pointers to merge lists"""
    cur_node_l1 = list1
    cur_node_l2 = list2
    # create dummy node, so that we can call .next on it
    resulting_list_pre_head = ListNode(-1)
    cur_resulting_node: Optional[ListNode] = resulting_list_pre_head
    while cur_node_l1 or cur_node_l2:
        if not cur_node_l1:
            take_from = cur_node_l2
            cur_node_l2 = cur_node_l2.next
        elif not cur_node_l2:
            take_from = cur_node_l1
            cur_node_l1 = cur_node_l1.next
        elif cur_node_l1.val <= cur_node_l2.val:
            take_from = cur_node_l1
            cur_node_l1 = cur_node_l1.next
        else:
            take_from = cur_node_l2
            cur_node_l2 = cur_node_l2.next
        cur_resulting_node.next = ListNode(take_from.val)
        cur_resulting_node = cur_resulting_node.next
    return resulting_list_pre_head.next


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


def test_converters():
    assert listNode_to_list(ListNode(1)) == [1]
    assert listNode_to_list(None) == []
    assert list_to_ListNode([]) is None
    assert list_to_ListNode([1]).val == 1 and list_to_ListNode([1]).next == None
    assert listNode_to_list(list_to_ListNode([1,2,3])) == [1,2,3]
    assert listNode_to_list(list_to_ListNode([])) == []


def test_example_1():
    l1 = list_to_ListNode([1,2,4])
    l2 = list_to_ListNode([1,3,4])
    assert listNode_to_list(mergeTwoLists(l1,l2)) == [1,1,2,3,4,4]


def test_example_2():
    l1 = list_to_ListNode([])
    l2 = list_to_ListNode([])
    assert listNode_to_list(mergeTwoLists(l1,l2)) == []


def test_example_3():
    l1 = list_to_ListNode([])
    l2 = list_to_ListNode([0])
    assert listNode_to_list(mergeTwoLists(l1,l2)) == [0]


def test_merge_lists():
    l1 = list_to_ListNode([1,2,4])
    l2 = list_to_ListNode([3])
    assert listNode_to_list(mergeTwoLists(l1,l2)) == [1,2,3,4]
    l2 = list_to_ListNode([1,2,4])
    l1 = list_to_ListNode([3])
    assert listNode_to_list(mergeTwoLists(l1,l2)) == [1,2,3,4]
