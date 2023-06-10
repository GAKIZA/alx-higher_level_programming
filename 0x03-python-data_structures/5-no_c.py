#!/usr/bin/env python3

def no_c(my_string):
    new_string = ""
    for letter in my_string:
        if letter in "cC":
            continue
        else:
            new_string += letter
    return new_string
