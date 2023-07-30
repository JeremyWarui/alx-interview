#!/usr/bin/python3
"""
validUTF8: method that determines if a given data set represents
            a valid UTF-8 encoding.
    Returns: True if data is a valid UTF-8 encoding,
            else return False
    Conditions:
    - A character in UTF-8 can be 1 to 4 bytes long
    - The data set can contain multiple characters
    - The data will be represented by a list of integers
    - Each integer represents 1 byte of data, therefore you
      only need to handle the 8 least significant bits of each integer
"""


def validUTF8(data: int) -> bool:
    """Returns true if data is valid utf8 else false"""
    n = 0
    # loop through the data
    for num in data:
        # get each binary rep of 8 bits
        binary_str = bin(num)[2:].zfill(8)
        # check if n is 0 then check first four bits
        if n == 0:
            # if starts with 0 then byte is 1
            if binary_str.startswith("0"):
                n = 0
            # if byte starts with 110 then its a 2 byte character
            elif binary_str.startswith("110"):
                n = 1
            # if byte starts with 1110, then its a 3 byte character
            elif binary_str.startswith("1110"):
                n = 2
            # if byte starts with 11110, then its 4 byte
            elif binary_str.startswith("11110"):
                n = 3
            # if byte starts with any other pattern then its invalid
            else:
                return False
        # if n is not 0 then check if byte starts with 10
        else:
            # if not, then its invalid
            if not binary_str.startswith("10"):
                return False
            # decrease n by 1
            n -= 1
        # check if n is 0 at the end
        return n == 0
