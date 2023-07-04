#!/usr/bin/python3
# 3-say_my_name

def say_my_name(first_name, last_name=""):
    """A function that print out the names of a user"""
    """when string first_name and last_name have ben input."""
    """otherwise raise a type Error when a non -string value is input"""

    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
