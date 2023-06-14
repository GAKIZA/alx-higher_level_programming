#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique = []
    sum = 0
    for item in my_list:
        if item not in unique:
            unique.append(item)
    for element in unique:
        sum += element
    return (sum)
