def allPathsSourceTarget(graph: list[list[int]]) -> list[list[int]]:
    """Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
    find all possible paths from node 0 to node n - 1 and return them in any order.
    The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
    (i.e., there is a directed edge from node i to node graph[i][j]).
    Idea: DFS"""
    def recursive_all_paths(start_node: int, graph: list[list[int]]) -> list[list[int]]:
        if start_node == len(graph)-1:
            return [[start_node]]
        resulting_paths = []
        for adjacent in graph[start_node]:
            paths = recursive_all_paths(adjacent, graph)
            for path in paths:
                resulting_paths.append([start_node] + path)
        return resulting_paths
    return recursive_all_paths(0, graph)


def test_corner_cases():
    assert allPathsSourceTarget([[1],
                                 []]) == [[0, 1]]
    assert allPathsSourceTarget([[1],
                                 [2],
                                 []]) == [[0,1,2]]
    assert allPathsSourceTarget([[1,2,3],[],[],[]]) == [[0,3]]
    assert allPathsSourceTarget([[1, 2, 3], [2], [3], []]) == [[0,1,2,3],[0,2,3],[0, 3]]


def test_examples():
    assert allPathsSourceTarget([[1,2],[3],[3],[]]) == [[0,1,3],[0,2,3]]
    assert allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]) == [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
