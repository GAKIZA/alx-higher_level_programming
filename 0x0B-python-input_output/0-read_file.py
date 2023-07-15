#!/usr/bin/python3
"""Reading a file """


def read_file(filename=""):
    """The function that reads a file line per line"""
    with open(filename, encoding="utf-8") as k:
        print(k.read(), end="")
