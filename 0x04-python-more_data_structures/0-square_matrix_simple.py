#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    result = []
    for item in matrix:
        result.append([c**2 for c in item])
    return result
