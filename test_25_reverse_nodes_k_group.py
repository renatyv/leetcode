from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '->' + str(self.val) + (str(self.next) if self.next else '')


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


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Reverse nodes until counter is equal to k, then reset counter and keep reversing
        If end of list, reverse back last elements"""

        def reverse_k_elements(head: Optional[ListNode], k) -> tuple[Optional[ListNode], Optional[ListNode]]:
            """:returns pair (head, tail)
            returns head, None, if number of elements is less than k"""
            if not head:
                return None, None
            if k == 1:
                return head, head
            prev = None
            cur = head
            next = cur.next
            # None cur -> cur.next
            n_elements = 1
            while n_elements < k and cur:
                n_elements += 1
                next = cur.next
                # None    cur -> next
                cur.next = prev
                # prev <- cur    next
                prev, cur = cur, next
                #      <- prev   cur
            if not cur:
                return reverse_k_elements(prev, n_elements - 1)
            rest_of_list = cur.next
            #      <- prev   cur -> rest_of_list
            new_head = cur
            cur.next = prev
            #  prev <- new_head  rest_of_list ->
            # head <- .... -< new_head  rest_of_list ->
            new_tail = head
            new_tail.next = rest_of_list
            return new_head, new_tail

        main_head, new_tail = reverse_k_elements(head, k)
        while new_tail:
            new_tail.next, new_tail = reverse_k_elements(new_tail.next, k)
        return main_head


def test_edge_cases():
    solution = Solution()
    head = list_to_ListNode([1])
    res = solution.reverseKGroup(head, 1)
    assert listNode_to_list(res) == [1]


def test_size_two():
    solution = Solution()
    head = list_to_ListNode([1, 2])
    res = solution.reverseKGroup(head, 1)
    assert listNode_to_list(res) == [1, 2]
    head = list_to_ListNode([1, 2])
    res = solution.reverseKGroup(head, 2)
    assert listNode_to_list(res) == [2, 1]


def test_size_three():
    solution = Solution()
    head = list_to_ListNode([1, 2, 3])
    res = solution.reverseKGroup(head, 2)
    assert listNode_to_list(res) == [2, 1, 3]
    head = list_to_ListNode([1, 2, 3])
    res = solution.reverseKGroup(head, 3)
    assert listNode_to_list(res) == [3, 2, 1]


def test_size_four():
    solution = Solution()
    head = list_to_ListNode([1, 2, 3, 4])
    res = solution.reverseKGroup(head, 2)
    assert listNode_to_list(res) == [2, 1, 4, 3]
    head = list_to_ListNode([1, 2, 3, 4])
    res = solution.reverseKGroup(head, 3)
    assert listNode_to_list(res) == [3, 2, 1, 4]


def test_size_large():
    solution = Solution()
    head = list_to_ListNode([1, 2, 3, 4, 5, 6, 7, 8])
    res = solution.reverseKGroup(head, 3)
    assert listNode_to_list(res) == [3, 2, 1, 6, 5, 4, 7, 8]
    head = list_to_ListNode([1, 2, 3, 4, 5, 6, 7, 8])
    res = solution.reverseKGroup(head, 4)
    assert listNode_to_list(res) == [4, 3, 2, 1, 8, 7, 6, 5]
    head = list_to_ListNode([1, 2, 3, 4, 5, 6, 7, 8])
    res = solution.reverseKGroup(head, 7)
    assert listNode_to_list(res) == [7, 6, 5, 4, 3, 2, 1, 8]


def test_examples():
    solution = Solution()
    head = list_to_ListNode([1, 2, 3, 4, 5])
    res = solution.reverseKGroup(head, 2)
    assert listNode_to_list(res) == [2, 1, 4, 3, 5]
    head = list_to_ListNode([1, 2, 3, 4, 5])
    res = solution.reverseKGroup(head, 3)
    assert listNode_to_list(res) == [3, 2, 1, 4, 5]
