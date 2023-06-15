#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0
    converter = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                 'C': 100, 'D': 500, 'M': 1000}
    converted_number = [converter[k] for k in roman_string] + [0]
    n = 0

    for i in range(len(converted_number) - 1):
        if converted_number[i] >= converted_number[i + 1]:
            n += converted_number[i]
        else:
            n -= converted_number[i]
    return n
