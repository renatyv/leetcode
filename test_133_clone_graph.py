from collections import deque
from typing import Deque


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        return str(self.val)


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        """BFS"""
        if node is None:
            return None
        new_root = Node(node.val)
        created_nodes: dict[int, Node] = {new_root.val: new_root}
        # deque of (new_node, old_neighbors)
        unprocessed_nodes_deque: Deque[tuple[Node, list[Node]]] = deque([(new_root, node.neighbors)])
        while unprocessed_nodes_deque:
            cur_node, old_neighbors = unprocessed_nodes_deque.popleft()
            for old_neighbor in old_neighbors:
                if old_neighbor.val not in created_nodes:
                    new_neighbor_node = Node(old_neighbor.val)
                    created_nodes[old_neighbor.val] = new_neighbor_node
                    unprocessed_nodes_deque.append((new_neighbor_node, old_neighbor.neighbors))
                cur_node.neighbors.append(created_nodes[old_neighbor.val])
        return new_root


def test_corner_cases():
    s = Solution()
    root = Node(1, [])
    graph_copy = s.cloneGraph(root)
    assert root != graph_copy
    assert root.val == graph_copy.val
    assert [neighbor.val for neighbor in root.neighbors] == [neighbor.val for neighbor in graph_copy.neighbors]
    node1 = Node(1)
    node2 = Node(2)
    node1.neighbors += [node2]
    node2.neighbors += [node1]
    copied_graph = s.cloneGraph(node1)
    assert copied_graph != node1
