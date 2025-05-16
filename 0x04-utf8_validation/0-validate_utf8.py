#!/usr/bin/env python3
"""
    a function that determines if a given data set represens a valid
    UTF-8 encoding
"""
def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    bytes_left = 0
    for byte in data:
        # Get the 8 least significant bits of the byte
        bits = byte & 0xFF

        # Checks for valid start byte if not expecting continuation bytes
        if bytes_left == 0:
            if bits < 0x80:  # 1-byte sequence
                continue
            elif bits < 0xE0:  # 2-byte sequence
                bytes_left = 1
            elif bits < 0xF0:  # 3-byte sequence
                bytes_left = 2
            elif bits < 0xF8:  # 4-byte sequence
                bytes_left = 3
            else:
                return False  # Invalid start byte
        else:
            # Checks for valid continuation byte
            if bits < 0x80 or bits > 0xBF:
                return False  # Invalid continuation byte
            bytes_left -= 1

    # Checks if all expected bytes have been processed
    return bytes_left == 0
