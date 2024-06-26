#!/usr/bin/python3
"""
utf-8 validation task
"""


def validUTF8(data):
    """
    method that determines if a given data set
    represents a valid UTF-8 encoding.
    """

    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                num_bytes = 0
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            if byte >> 6 == 0b10:
                num_bytes -= 1
            else:
                return False

    return num_bytes == 0
