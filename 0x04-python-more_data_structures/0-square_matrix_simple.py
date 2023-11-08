#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(lambda submat: [x ** 2 for x in submat], matrix))
    return new_matrix
