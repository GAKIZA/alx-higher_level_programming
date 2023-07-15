#!/usr/bin/python3
""" Function that writes an object to a text file"""

import json


def save_to_json_file(my_obj, filename):
    "Writes a given object to a text file"""
    with open(filename, 'w') as j:
        return json.dump(my_obj, j)
