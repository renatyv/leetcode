def findOrder(numCourses: int, prerequisites: list[list[int]]) -> list[int]:
    """Idea: topological sorting"""
    if not prerequisites:
        return list(range(numCourses))
    # reversed_prereqs[x] = set of coursed requiring x
    reversed_adj: dict[int, set[int]] = dict()
    # i_degree[x] number of incoming edges to node x
    out_degree: dict[int, int] = dict()
    for course in range(numCourses):
        out_degree[course] = 0
        reversed_adj[course] = set()
    for prerequisite in prerequisites:
        course, required = prerequisite
        reversed_adj[required].add(course)
        out_degree[course] += 1

    topologically_sorted_courses = []

    while reversed_adj:
        take_courses = []
        # select nodes with zero prerequisites
        for course in out_degree:
            if out_degree[course] == 0:
                take_courses.append(course)
        #  remove edges to selected nodes
        for course in take_courses:
            for depending_course in reversed_adj[course]:
                out_degree[depending_course] -= 1
            del out_degree[course]
            del reversed_adj[course]
        # if some nodes are left, but they all have out_degree > 0
        if not take_courses:
            return []
        topologically_sorted_courses += take_courses
    return topologically_sorted_courses


def test_examples():
    assert findOrder(3, [[1, 0]]) == [0, 2, 1]
    assert findOrder(2, [[1, 0]]) == [0, 1]
    assert findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3]
    assert findOrder(1, []) == [0]
    assert findOrder(2, [[1, 0], [0, 1]]) == []
    assert findOrder(3, [[1, 0], [0, 1]]) == []
    assert findOrder(4, [[3, 2], [1, 2], [1, 0], [2, 0]]) == [0, 2, 1, 3]
    assert findOrder(4, [[3, 2], [1, 0], [2, 0]]) == [0, 1, 2, 3]
    assert findOrder(4, [[3, 2], [1, 2]]) == [0, 2, 1, 3]
