from collections import Counter


def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    """Alice has some number of cards and she wants to rearrange the cards into groups
    so that each group is of size groupSize, and consists of groupSize consecutive cards.
    Given an integer array hand
    where hand[i] is the value written on the ith card and an integer groupSize,
    return true if she can rearrange the cards, or false otherwise.
    1 <= hand.length <= 10^4
    0 <= hand[i] <= 10^9
    1 <= groupSize <= hand.length

    Idea: try doing that"""
    if len(hand) % groupSize != 0:
        return False
    hand_nums_count = Counter(hand)
    sorted_unique_nums_from_hand = sorted(hand_nums_count.keys())
    # take the smallest num from hand
    for group_start in sorted_unique_nums_from_hand:
        # go over all nums which should be in the same group
        take_cards_count = hand_nums_count[group_start]
        if take_cards_count == 0:
            continue
        for group_index in range(group_start, group_start + groupSize):
            # remove necessary amount of nums
            hand_nums_count[group_index] = hand_nums_count.get(group_index, 0) - take_cards_count
            # if result is negative, impossible
            if hand_nums_count[group_index] < 0:
                return False
    return True


def test_edge_cases():
    assert isNStraightHand([1], 1)
    assert isNStraightHand([1, 1], 1)
    assert not isNStraightHand([1, 1], 2)
    assert not isNStraightHand([1, 3], 2)
    assert isNStraightHand([1, 2], 2)
    assert isNStraightHand([2, 1], 2)
    assert isNStraightHand([2, 3, 1], 3)
    assert isNStraightHand([1, 2, 3], 3)
    assert not isNStraightHand([1, 2, 3], 2)
    assert not isNStraightHand([1, 3, 5, 7], 2)
    assert isNStraightHand([1, 2, 3, 3, 4, 5], 3)
    assert not isNStraightHand([1, 2, 2, 3, 3, 4, 5], 2)
    assert isNStraightHand([1, 2, 2, 3, 3, 4], 3)



def test_cases_1():
    assert isNStraightHand([1, 2, 3, 4, 5, 6], 2)
    assert isNStraightHand([1, 2, 3, 4, 5, 6], 3)
    assert isNStraightHand([1, 2, 3, 4, 5, 6], 6)
    assert isNStraightHand([1, 2, 3, 1, 2, 3], 3)
    assert not isNStraightHand([1, 2, 3, 1, 2, 3], 2)
    assert not isNStraightHand([1, 2, 3, 5, 6, 8], 3)


def test_examples():
    assert isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
    assert not isNStraightHand([1, 2, 3, 4, 5], 4)
