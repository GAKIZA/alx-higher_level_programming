#!/usr/bin/python3

"""creating a private attribute of a class"""


class Square:

    """ Representing a square"""

    def __init__(self, size=0):
        """Initializes a new square

        args:
        size: the size of new square"""
        self.__size = size

    @property
    def size(self):
        """Contains the current size of a square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Return the current area of a square """
        return (self.__size * self.__size)
