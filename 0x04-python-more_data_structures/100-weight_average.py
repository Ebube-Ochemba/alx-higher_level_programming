#!/usr/bin/python3

def weight_average(my_list=[]):
    total = 0
    weights = 0

    for score, weight in my_list:
        total += score * weight
        weights += weight

    if weights != 0:
        return total / weights
