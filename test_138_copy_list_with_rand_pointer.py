from typing import Optional


def copyRandomList(head: Optional['Node']) -> Optional['Node']:
    """Idea: create a dict old node -> new node"""
    new_nodes = {None: None}
    old_node = head
    # create list of new nodes
    while old_node:
        # map old node -> new node
        new_nodes[old_node] = Node(old_node.val)
        old_node = old_node.next
    old_node = head
    # iterate over the old list
    while old_node:
        new_nodes[old_node].next = new_nodes[old_node.next]
        new_nodes[old_node].random = new_nodes[old_node.random]
        old_node = old_node.next
    return new_nodes[head]


class Node:
    def __init__(self, val=0, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val: int = val
        self.next: Optional[Node] = next
        self.random: Optional[Node] = random

    def __str__(self):
        return str(self.val)


def list_to_Node(num_random_index_list: list[tuple[int, int]]) -> Optional[Node]:
    if not num_random_index_list:
        return None
    # create all nodes
    nodes_list: list[Node] = []
    for num_random in num_random_index_list:
        num, _ = num_random
        nodes_list.append(Node(num))
    # set next pointer
    for i in range(1, len(num_random_index_list)):
        nodes_list[i - 1].next = nodes_list[i]
    # set random pointer
    for i in range(len(num_random_index_list)):
        _, random_index = num_random_index_list[i]
        if random_index is not None:
            nodes_list[i].random = nodes_list[random_index]
    return nodes_list[0]


def test_list_to_head():
    head = list_to_Node([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]])
    assert True


def test_examples():
    assert list_to_Node([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]).next.random.val == 7
