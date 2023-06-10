#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    r = len(my_list) - 1
    for i in range(r + 1):
        print("{}".format(my_list[r - i]))
