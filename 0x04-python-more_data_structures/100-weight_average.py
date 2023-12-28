#!/usr/bin/python3

# Grades(score, weight) = [(A, 2), (B, 1), (C, 10), (D, 2)]
# Weighted average = ((A * 2) + (B * 1) + (C* 10) + (D * 2)) / (2 + 1 + 10 + 2)


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
