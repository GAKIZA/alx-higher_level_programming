#!/usr/bin/python3

"""creating a private attribute of a class"""


class Square:
    """ Representing a square"""
    def __init__(self, size=0):
        """Initializes a new square

        args:
        size: the size of new square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
