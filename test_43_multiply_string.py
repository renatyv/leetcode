import textwrap


def multiply(num1: str, num2: str) -> str:
    """Idea: bignum"""
    if num1 == '0' or num2 == '0':
        return '0'
    N_DIGITS = 4
    DIVIDER = 10 ** (N_DIGITS)

    # pad with zeroes
    def pad_zeroes(s: str) -> str:
        if len(s) % N_DIGITS == 0:
            return s
        return '0' * (N_DIGITS - len(s) % N_DIGITS) + s

    num1 = pad_zeroes(num1)
    num2 = pad_zeroes(num2)
    # least significant number first
    bignum_1 = [int(x) for x in textwrap.wrap(num1, N_DIGITS)][::-1]
    bignum_2 = [int(x) for x in textwrap.wrap(num2, N_DIGITS)][::-1]
    # compute product
    max_product_len = len(bignum_1) + len(bignum_2) + 1
    product_bignum = [0] * max_product_len
    # multiply digit by digit
    for bigdigit_1 in range(len(bignum_1)):
        for bigdigit_2 in range(len(bignum_2)):
            product_bignum[bigdigit_1 + bigdigit_2] += bignum_1[bigdigit_1] * bignum_2[bigdigit_2]
            i = bigdigit_1 + bigdigit_2
            while product_bignum[i] >= DIVIDER:
                product_bignum[i + 1] += product_bignum[i] // DIVIDER
                product_bignum[i] = product_bignum[i] % DIVIDER
                i += 1
    # remove leading zeroes
    while product_bignum[-1] == 0:
        product_bignum = product_bignum[:-1]
    # convert int to string
    bigdigits = [str(num) for num in product_bignum[::-1]]
    # pad with zeroes each 'big digit'
    padded_product = ''.join(pad_zeroes(num) for num in bigdigits)
    # remove leading zeroes
    return padded_product.lstrip('0')


def test_edge_cases():
    assert multiply('34', '34') == '1156'
    a_s = [str(x) for x in range(100000)]
    b_s = [str(x) for x in range(100000)]
    for a, b in zip(a_s, b_s):
        assert multiply(a, b) == str(int(a) * int(b)), f'{a=}, {b=}'
