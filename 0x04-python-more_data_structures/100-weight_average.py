#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    numerator = 0
    denominator = 0

    for tupl in my_list:
        numerator += tupl[0] * tupl[1]
        denominator += tupl[1]

    return (numerator / denominator)
