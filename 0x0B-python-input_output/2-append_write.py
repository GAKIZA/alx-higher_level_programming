#!/usr/bin/python3
"""Appending a string at the end of a file"""

def append_write(filename="", text=""):
    """Appending a text at the end of a file

    args:
        filename: the filename to append to 
        text: the text to append at the end of filename
        Returns: the number of characters """
    with open(filename, 'a', encoding='utf-8') as g:
        return (g.write(text))
