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
        # Check if the byte is the start of a new UTF-8 character
        if num_bytes == 0:
            # Count the number of leading 1s to determine the number of bytes
            if byte >> 7 == 0b0:  # 1-byte character
                num_bytes = 0
            elif byte >> 5 == 0b110:  # 2-byte character
                num_bytes = 1
            elif byte >> 4 == 0b1110:  # 3-byte character
                num_bytes = 2
            elif byte >> 3 == 0b11110:  # 4-byte character
                num_bytes = 3
            else:
                return False  # Invalid start byte

        else:
            # Check if the byte is a continuation byte
            if byte >> 6 == 0b10:
                num_bytes -= 1
            else:
                return False  # Invalid continuation byte

    # Check if all bytes have been consumed (i.e., num_bytes == 0)
    return num_bytes == 0
