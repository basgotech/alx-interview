#!/usr/bin/python3
"""UTF-8 Validation"""


def cal_le_1bit_8bit(num):
    """
    Calculate the number of leading 1 bits in an 8-bit integer.
    """
    bits = 0
    loader = 1 << 7
    while loader & num:
        bits += 1
        loader = loader >> 1
    return bits


def validUTF8(data):
    """
    Determine if the data represents a valid UTF-8 encoding.
    """
    count_the_bit = 0
    for x in range(len(data)):
        if count_the_bit == 0:
            count_the_bit = cal_le_1bit_8bit(data[x])
            if count_the_bit == 0:
                continue
            if count_the_bit == 1 or count_the_bit > 4:
                return False
        else:
            if not (data[x] & (1 << 7) and not (data[x] & (1 << 6))):
                return False
        count_the_bit -= 1
    return count_the_bit == 0
