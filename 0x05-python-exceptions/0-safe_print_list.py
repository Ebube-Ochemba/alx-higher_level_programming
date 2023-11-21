#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    for obj in range(0, x):
        try:
            print(my_list[obj], end="")
            count += 1
        except IndexError:
            break
    print("\n", end="")
    return count
