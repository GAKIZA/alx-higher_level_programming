#!/usr/bin/python3
"""A function that determines that a given object is an instance
    of a given function"""


def is_same_class(obj, a_class):
    """return true if obj is an instance of a_class"""

    if type(obj) == a_class:
        return True
    return False
