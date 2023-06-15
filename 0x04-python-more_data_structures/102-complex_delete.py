#!/usr/bin/python3

def complex_delete(my_dict, value):
    interm = my_dict.copy()
    for a, b in interm.items():
        if value == b:
            my_dict.pop(a)
    return my_dict
