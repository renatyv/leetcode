from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


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


def deleteDuplicates_dict_solution(head: Optional[ListNode]) -> Optional[ListNode]:
    """Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
    leaving only distinct numbers from the original list.
    Return the linked list sorted as well."""
    if not head:
        return None
    num_elements: dict[int] = {}
    cur_elem: Optional[ListNode] = head
    while cur_elem:
        num_elements[cur_elem.val] = num_elements.get(cur_elem.val, 0) + 1
        cur_elem = cur_elem.next
    pre_head: ListNode = ListNode(-101)
    cur_elem = pre_head
    for val in sorted(num_elements.keys()):
        if num_elements[val] == 1:
            cur_elem.next = ListNode(val)
            cur_elem = cur_elem.next
    return pre_head.next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    """Given the head of a sorted linked list, delete all nodes that have duplicate numbers,
    leaving only distinct numbers from the original list.
    Return the linked list sorted as well."""
    if not head:
        return None
    pre_head: ListNode = ListNode(-101)
    cur_resulting_elem = pre_head
    cur_elem = head
    while cur_elem:
        if cur_elem.next and cur_elem.next.val == cur_elem.val:
            #         skip until next value
            while cur_elem.next and cur_elem.next.val == cur_elem.val:
                cur_elem = cur_elem.next
        else:
            cur_resulting_elem.next = ListNode(cur_elem.val)
            cur_resulting_elem = cur_resulting_elem.next
        cur_elem = cur_elem.next
    return pre_head.next



def test_examples():
    assert listNode_to_list(deleteDuplicates(list_to_ListNode([1,2,3,3,4,4,5]))) == [1,2,5]
    assert listNode_to_list(deleteDuplicates(list_to_ListNode([1,1,1,2,3]))) == [2,3]


def test_corner():
    assert deleteDuplicates(None) is None
    assert deleteDuplicates(list_to_ListNode([1,1,1,1])) is None
    assert deleteDuplicates(list_to_ListNode([1, 1, 2, 2])) is None
    assert deleteDuplicates(list_to_ListNode([1, 1, 2, 2, 2, 4, 4])) is None


def test_cases():
    assert listNode_to_list(deleteDuplicates(list_to_ListNode([1,2,3,4]))) == [1,2,3,4]
    assert listNode_to_list(deleteDuplicates(list_to_ListNode([1, 2,2,2,2, 3, 4]))) == [1, 3, 4]
    assert listNode_to_list(deleteDuplicates(list_to_ListNode([1, 2, 3, 3,3 ,3, 4]))) == [1, 2,4]
    assert listNode_to_list(deleteDuplicates(list_to_ListNode([1, 2, 3, 4,4,4,4]))) == [1, 2, 3]
