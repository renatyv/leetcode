def mergeTriplets(triplets: list[list[int]], target: list[int]) -> bool:
    """
    Idea: keep merging while triplet <= target
    """
    merged_triplet = [0, 0, 0]
    for triplet in triplets:
        if triplet == target:
            return True
        # skip if current triplet contains value higher than target
        if any(triplet[i] > target[i] for i in range(3)):
            continue
        # merge
        merged_triplet = [max(triplet[i], merged_triplet[i]) for i in range(3)]
        if merged_triplet == target:
            return True
    return False


def test_examples():
    assert mergeTriplets([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5])
    assert not mergeTriplets([[3, 4, 5], [4, 5, 6]], [3, 2, 5])
    assert mergeTriplets([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5])


def test_wa1():
    assert mergeTriplets([[7, 15, 15],
                          [11, 8, 3],
                          [5, 3, 4],
                          [12, 9, 9],
                          [5, 12, 10],
                          [7, 15, 10],
                          [7, 6, 4],
                          [3, 9, 8],
                          [2, 13, 1],
                          [14, 2, 3]], [14, 6, 4])
