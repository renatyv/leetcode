from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def reorderList(head: Optional[ListNode]) -> None:
    """
    You are given the head of a singly linked-list l0 -> l1 -> l2 -> ... ln
    Reorder the list to be on the following form: l0 -> ln -> l2 -> ln-1 -> ...
    Ideas:
    1) find middle using slow and fast pointer.
    2) reverse the second half
    3) merge first half and reversed second half
    """
    if head is None or head.next is None:
        return

    # find middle
    middle = head
    tail = head
    pre_middle = None
    while tail and tail.next:
        tail = tail.next.next
        pre_middle = middle
        middle = middle.next
    # split lists
    if pre_middle:
        pre_middle.next = None

    # reverse second half
    def reverse_list(head: ListNode) -> ListNode:
        reversed_head = middle
        unreversed_head = middle
        while unreversed_head:
            temp = unreversed_head
            unreversed_head = unreversed_head.next
            temp.next = reversed_head
            reversed_head = temp
        head.next = None
        return reversed_head

    reversed_second_half = reverse_list(middle)

    def merge_lists(shorter: ListNode, longer: ListNode) -> ListNode:
        """
        head: a -> b -> d
        list2: d -> e -> f
        :return:  a -> d -> b -> e
        """
        sho = shorter
        lo = longer
        while sho.next:
            temp1 = sho.next
            temp2 = lo.next
            sho.next = lo
            lo.next = temp1
            sho = temp1
            lo = temp2
        # check if number is odd
        if lo.next:  # odd number. cur_1.next = None
            sho.next = lo
        else:  # even number
            temp1 = sho.next
            sho.next = lo
            lo.next = temp1
        return shorter

    merge_lists(head, reversed_second_half)
    return


def test_examples():
    lst1_head = list_to_ListNode([1])
    reorderList(lst1_head)
    assert listNode_to_list(lst1_head) == [1]
    lst1_head = list_to_ListNode([1, 2])
    reorderList(lst1_head)
    assert listNode_to_list(lst1_head) == [1, 2]
    lst1_head = list_to_ListNode([1, 2, 3])
    reorderList(lst1_head)
    assert listNode_to_list(lst1_head) == [1, 3, 2]
    lst1_head = list_to_ListNode([1, 2, 3, 4])
    reorderList(lst1_head)
    assert listNode_to_list(lst1_head) == [1, 4, 2, 3]
    lst1_head = list_to_ListNode([1, 2, 3, 4, 5])
    reordered = reorderList(lst1_head)
    assert listNode_to_list(lst1_head) == [1, 5, 2, 4, 3]
    lst1_head = list_to_ListNode([1, 2, 3, 4, 5, 6])
    reordered = reorderList(lst1_head)
    assert listNode_to_list(lst1_head) == [1, 6, 2, 5, 3, 4]


def list_to_ListNode(nodes: list) -> Optional[ListNode]:
    if not nodes:
        return None
    head = ListNode(nodes[0], None)
    cur_node = head
    for node in nodes[1:]:
        cur_node.next = ListNode(node, None)
        cur_node = cur_node.next
    return head


def listNode_to_list(head=Optional[ListNode]) -> list[int]:
    cur_node: Optional[ListNode] = head
    resulting_list = []
    while cur_node:
        resulting_list.append(cur_node.val)
        cur_node = cur_node.next
    return resulting_list
