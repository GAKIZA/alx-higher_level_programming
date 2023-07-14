#!/usr/bin/python3
"""Defining an empty class"""


class BaseGeometry:
    """Class for Base Geometry"""
    def area(self):
        """Area that raises an exception"""
        raise Exception("Area() is not implemented")
