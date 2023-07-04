#!/usr/bin/python3
# 4-print_square.py

""" Draw a square using #"""

def print_square(size):
    """ print_square print square using #
    size is the length of the side otherwise print TypeError
    when size is not a positive non-zero integer number

    args:
    size - number type
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    else:
        for i in range(size):
            [print("#", end="") for j in range(size)]
            print("")
