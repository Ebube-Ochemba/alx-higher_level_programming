#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
            if num is not row[len(row) - 1]:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num), end="")
        print()


'''
    for row in matrix:
        print(" ".join(['{:d}'.format(num) for num in row]))
'''
