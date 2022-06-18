class Solution:
    class UnionFind:

        def __init__(self, size: int):
            self.parent = list(range(size))
            self.rank = [0] * size

        def find_root(self, node):
            """ with path compression """
            # search for root
            path = [node]
            while self.parent[path[-1]] != path[-1]:
                path.append(self.parent[path[-1]])
            root = path[-1]
            # compress path. Map all nodes in path to root
            for node in path[1:]:
                self.parent[node] = root
                self.rank[node] = 1
            return root

        def union(self, node1: int, node2: int):
            root1 = self.find_root(node1)
            root2 = self.find_root(node2)
            if root1 == root2:
                return
            # connect tree with lower rank to a tree with higher rank,
            # so that hight of the whole forest does not increase
            if self.rank[root1] == self.rank[root2]:
                self.parent[root2] = root1
                self.rank[root1] = self.rank[root1] + 1
            elif self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            else:
                self.parent[root1] = root2

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        """You are given an array points representing integer coordinates
        of some points on a 2D-plane,where points[i] = [xi, yi].
        The cost of connecting two points [xi, yi] and [xj, yj]
        is the manhattan distance between them: |xi - xj| + |yi - yj|,
        where |val| denotes the absolute value of val.
        Return the minimum cost to make all points connected.
        All points are connected if there is exactly one simple path between any two points.

        Idea: MST. Kruskal or Prim's algorithm.
        We will implement Kruskal"""

        def distance(point1: list[int], point2: list[int]):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        # list of all edges. [(a1,b2),(a2,b2),.. (a,b) = edge from point with index a to point with index b
        # (distance, point_number1, point_number2)
        edge_t = tuple[int, int, int]
        edges: list[edge_t] = []
        for i in range(len(points) - 1):
            for j in range(i, len(points)):
                edges.append((distance(points[i], points[j]), i, j))
        mst_total_weight = 0
        union_find = Solution.UnionFind(len(points))
        # Kruskal algorithm. Edges are sorted by weight = distance
        for edge in sorted(edges):
            weight, point_index_1, point_index_2 = edge
            root1 = union_find.find_root(point_index_1)
            root2 = union_find.find_root(point_index_2)
            if root1 == root2:
                continue
            mst_total_weight += weight
            union_find.union(root1, root2)
        return mst_total_weight


def test_edge_cases():
    solution = Solution()
    assert solution.minCostConnectPoints([[0, 0]]) == 0
    assert solution.minCostConnectPoints([[0, 0], [0, 1]]) == 1


def test_examples():
    solution = Solution()
    assert solution.minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]) == 20
    assert solution.minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]) == 18
