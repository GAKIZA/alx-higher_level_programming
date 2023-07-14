#!/usr/bin/python3
"""Defining an empty class"""


class BaseGeometry:
    """Class for Base Geometry"""
    def area(self):
        """Area that raises an exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """the method that validates integers"""
        if type(value) != int:
            raise TypeError(f"{name} must be integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
