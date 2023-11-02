#!/usr/bin/python3
for tens in range(10):
    for unit in range(tens + 1, 10):
        if tens == 8 and unit == 9:
            print("{:d}{:d}".format(tens, unit))
        else:
            print("{:d}{:d}".format(tens, unit), end=', ')
