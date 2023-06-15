#!/usr/bin/python3

new_dict = {}

def multiply_by_2(a_dictionary):

    for keys, values in a_dictionary.items():
 
        new_dict[keys] = 2 * values

    return new_dict
