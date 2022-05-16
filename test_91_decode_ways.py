def numDecodings(s: str) -> int:
    """see https://leetcode.com/problems/decode-ways/
    Idea: dynamic programminc
    compute number of decodings for s[:i] using number of decodings for s[:i-1] and for s[:i-2]"""
    # skip leading zeros
    if s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    # n_decodings[j] = number of decodings for string of first j-1 characters
    n_decodings = [0] * (len(s) + 1)
    n_decodings[0] = 1
    n_decodings[1] = 1
    for i in range(1, len(s)):
        j = i + 1
        if s[i - 1] == '0':
            if s[i] == '0':  # '00'
                return 0
            else:  # 01,02,...09
                n_decodings[j] = n_decodings[j - 1]
        elif s[i - 1] == '1':
            if s[i] == '0':  # 10
                n_decodings[j] = n_decodings[j - 2]
            else:  # s[i] <= '9'. 11, 12,..19
                n_decodings[j] = n_decodings[j - 1] + n_decodings[j - 2]
        elif s[i - 1] == '2':
            if s[i] == '0':  # 20
                n_decodings[j] = n_decodings[j - 2]
            elif s[i] <= '6':  # 21,22..26
                n_decodings[j] = n_decodings[j - 1] + n_decodings[j - 2]
            else:  # 27, 28,..
                n_decodings[j] = n_decodings[j - 1]
        else:  # 3x, 4x,
            if s[i] == '0':  # 30, 40,
                return 0
            else:  # 31, 32,.. 41, 42,.. 91, 92...
                n_decodings[j] = n_decodings[j - 1]
    return n_decodings[-1]


def test_corner():
    for i in range(1, 10):
        assert numDecodings(str(i)) == 1
    assert numDecodings('01') == 0
    assert numDecodings('09') == 0
    assert numDecodings('10') == 1
    assert numDecodings('11') == 2
    assert numDecodings('19') == 2
    assert numDecodings('20') == 1
    assert numDecodings('21') == 2
    assert numDecodings('26') == 2
    assert numDecodings('26') == 2
    assert numDecodings('27') == 1
    assert numDecodings('28') == 1
    assert numDecodings('29') == 1
    assert numDecodings('30') == 0
    assert numDecodings('31') == 1
    assert numDecodings('39') == 1
    assert numDecodings('99') == 1
    assert numDecodings("100") == 0


def test_examples():
    assert numDecodings("12") == 2
    assert numDecodings("226") == 3
    assert numDecodings("06") == 0


def test_wa_1():
    assert numDecodings("210") == 1
    assert numDecodings("2101") == 1


def test_wa2():
    assert numDecodings("111") == 3
    assert numDecodings("1111") == 5
    assert numDecodings('210111134201') == 8


def test_wa3():
    assert numDecodings("10011") == 0
