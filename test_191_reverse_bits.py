def reverseBits(n: int) -> int:
    """Reverse bits of a given 32 bits unsigned integer."""
    reversed_bit_order: int = 0
    for i in range(32):
        bit_i = (n >> i) & 1
        reversed_bit = bit_i << (31-i)
        reversed_bit_order = reversed_bit_order | reversed_bit
    return reversed_bit_order


def test_example():
    assert reverseBits(0b00000010100101000001111010011100) == 0b00111001011110000010100101000000
    assert reverseBits(0b11111111111111111111111111111101) == 0b10111111111111111111111111111111


def test_reverse_bits():
    assert reverseBits(0b00000000000000000000000000000000) == 0b00000000000000000000000000000000
