#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for obj in range(0, x):
        try:
            print("{:d}".format(my_list[obj]), end="")
            count += 1
        except (ValueError, TypeError, IndexError):
            pass
    print("\n", end="")
    return count
