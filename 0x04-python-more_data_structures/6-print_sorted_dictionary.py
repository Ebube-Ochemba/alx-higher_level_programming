#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for key, value in sorted(a_dictionary.items()):
        print("{}: {}".format(key, value))


"""
The items() method returns a list of tuple pairs; the first element of each \
        pair is a key and the second is it's value. The sorted() function \
        sorts list of tuples based on the first element of each tuple \
        (the key).
"""
