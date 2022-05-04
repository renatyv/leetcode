def combine(n: int, k: int) -> list[list[int]]:
    """Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
    You may return the answer in any order.
    Idea: use recursion. """
    if k == n:
        return [list(range(1, k+1))]
    if k == 1:
        return [[k] for k in range(1, n+1)]
    # do not take n + take n
    combinations_if_n_is_taken = [arr + [n] for arr in combine(n-1, k-1)]
    combinations_if_n_is_skipped = combine(n-1, k)
    combined = combinations_if_n_is_taken + combinations_if_n_is_skipped
    return combined


def equal_as_sets(mat1: list[list[int]], mat2: list[list[int]]):
    return {frozenset(x) for x in mat1} == {frozenset(x) for x in mat2}


def test_example():
    assert equal_as_sets(combine(4, 2), [[2,4],
                                          [3,4],
                                          [2,3],
                                          [1,2],
                                          [1,3],
                                          [1,4]])
    assert equal_as_sets(combine(1, 1), [[1]])


def test_corner():
    assert equal_as_sets(combine(3, 1), [[1],[2],[3]])
    assert equal_as_sets(combine(3, 3), [[1,2,3]])
