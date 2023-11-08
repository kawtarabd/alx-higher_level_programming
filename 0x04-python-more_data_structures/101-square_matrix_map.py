#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda k: list(map(lambda y: y ** 2, k)), matrix))
