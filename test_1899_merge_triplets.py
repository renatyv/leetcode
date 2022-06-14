import functools


def mergeTriplets(triplets: list[list[int]], target: list[int]) -> bool:
    """
    Idea: keep merging while triplet <= target
    """
    merged_triplet = [0, 0, 0]
    for triplet in triplets:
        # skip if current triplet contains value higher than target
        if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
            continue
        merged_triplet = [max(triplet[0], merged_triplet[0]),
                          max(triplet[1], merged_triplet[1]),
                          max(triplet[2], merged_triplet[2])]
    return merged_triplet == target


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
