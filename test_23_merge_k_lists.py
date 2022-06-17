# Definition for singly-linked list.
import heapq
from typing import Optional

from test_143_reorder_list import list_to_ListNode, listNode_to_list, ListNode


class Solution:
    class OrderedListNode(ListNode):
        def __init__(self, node: ListNode):
            self.val = node.val
            if node.next:
                self.next = Solution.OrderedListNode(node.next)
            else:
                self.next = None

        def __le__(self, other):
            return self.val <= other.val

        def __lt__(self, other):
            return self.val < other.val

        def __ge__(self, other):
            return self.val >= other.val

        def __gt__(self, other):
            return self.val > other.val

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        """Idea: use min heap"""
        min_heap: list[Solution.OrderedListNode] = [Solution.OrderedListNode(head) for head in lists if head]
        # add first elements from each sublist into heap
        heapq.heapify(min_heap)
        # if lists is empty or all lists inside are empty
        if not min_heap:
            return None
        # init head as with a minimal element
        head: Solution.OrderedListNode = heapq.heappop(min_heap)
        # put next element into the heap
        if head.next:
            heapq.heappush(min_heap, head.next)
        # keep getting the minimal element from the heap and pushing the next one
        tail = head
        while min_heap:
            next_min = heapq.heappop(min_heap)
            tail.next = next_min
            tail = tail.next
            if next_min.next:
                heapq.heappush(min_heap, tail.next)
        return head


def test_edge_cases():
    s = Solution()
    list_of_heads = [list_to_ListNode(l) for l in [[1]]]
    merged = s.mergeKLists(list_of_heads)
    assert listNode_to_list(merged) == [1]
    list_of_heads = [list_to_ListNode(l) for l in [[0], [1]]]
    merged = s.mergeKLists(list_of_heads)
    assert listNode_to_list(merged) == [0, 1]
    list_of_heads = [list_to_ListNode(l) for l in [[0, 1]]]
    merged = s.mergeKLists(list_of_heads)
    assert listNode_to_list(merged) == [0, 1]
    list_of_heads = [list_to_ListNode(l) for l in [[0, 1], [3, 4], [2, 3]]]
    merged = s.mergeKLists(list_of_heads)
    assert listNode_to_list(merged) == [0, 1, 2, 3, 3, 4]


def test_examples():
    s = Solution()
    list_of_heads = [list_to_ListNode(l) for l in [[1, 4, 5], [1, 3, 4], [2, 6]]]
    merged = s.mergeKLists(list_of_heads)
    assert listNode_to_list(merged) == [1, 1, 2, 3, 4, 4, 5, 6]
    list_of_heads = [list_to_ListNode(l) for l in []]
    merged = s.mergeKLists(list_of_heads)
    assert listNode_to_list(merged) == []
    list_of_heads = [list_to_ListNode(l) for l in [[]]]
    merged = s.mergeKLists(list_of_heads)
    assert listNode_to_list(merged) == []
