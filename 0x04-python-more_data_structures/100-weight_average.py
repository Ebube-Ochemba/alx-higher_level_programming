#!/usr/bin/python3

# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)


def weight_average(my_list=[]):
    if not my_list:
        return 0

    total = 0
    weights = 0

    for score, weight in my_list:
        total += score * weight
        weights += weight

    if weights != 0:
        return total / weights
