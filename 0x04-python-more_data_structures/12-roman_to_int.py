#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or isinstance(roman_string, str) is False:
        return 0

    values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
    }

    total = 0
    prev_value = 0

    for char in roman_string:
        curr_value = values[char]

        total = total + curr_value

        if curr_value > prev_value:
            total = total - (2 * prev_value)

        prev_value = curr_value

    return total
