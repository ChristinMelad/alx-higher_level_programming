#!/usr/bin/python3
import numpy as np
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{}".format(i) for i in row))
