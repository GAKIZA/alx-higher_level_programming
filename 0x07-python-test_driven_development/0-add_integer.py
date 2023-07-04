#!/usr/bin/python3
# 0-add_integer.py

def add_integer(a, b=98):
    """ a function that adds two numbers and return an integer result
    Float numbers are typecasted into integer.
    Returns - Type Error if either value is a non number type """

    if((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer or a float number")
    if((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer or a float number")

    return (int(a) + int(b))
