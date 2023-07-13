#!/usr/bin/python3
""" Defines an inherited class mylist from list"""


class MyList(list):
    """a class that prints sorted elements of a list """
    def print_sorted(self):
        """print elements of a list in ascending order"""
        print(sorted(self))
