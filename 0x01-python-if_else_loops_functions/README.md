# Python - if/else, loops, functions

> This project was an introduction to more fundamental concepts and syntax in Python programming.

## Summary

I learnt about conditionals and loops in Python. `if`, `if ... else`, `break`, `continue`, `pass`, and `range` statements with `while` and `for loops`. I also wrote my own Python functions and learnt about scope of variables, tracebacks, and arithmetic operators.

## Files

> Each file contains the solution to a task in the project.

- [0-positive_or_negative.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/0-positive_or_negative.py): Python program that assigns a random signed `number` to the variable `number` each time it is executed and prints whether number is positive or negative.
	- Prints the number followed by;
		- If the number is greater than 0: `is positive`
		- If the number is 0: `is zero`
		- If the number is less than 0: `is negative`
		- Followed by a new line.
	- Incomplet [source code](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py) to be completed
- [1-last_digit.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/1-last_digit.py): Python program that assigns a random signed number to the variable `number` each time it is executed and prints its last digit.
	- Prints the string `Last digit of [number] is [last_digit]` followed by:
		- if the number is greater than 5: `and is greater than 5`
		- If the number is 0: `and is 0`
		- If the number is less than 6 and not 0: `and is less than 6 and not 0`
		- Followed by a new line.
	- Incomplet [source code](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py) to be completed
- [2-print_alphabet.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/2-print_alphabet.py): Python program that prints the alphabet in lowercase, not followed by a new line.
	- Using only one `print` and one loop.
	- Without storing characters in variables or importing modules.
- [3-print_alphabt.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/3-print_alphabt.py): Python program that prints the alphabet in lowercase, followed by a new line.
	- Using only one `print` and one loop
	- Without storing characters in variables or importing modules.
	- Prints every letter except for `q` and `e`.
- [4-print_hexa.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/4-print_hexa.py): Python program that prints all numbers from `0` to `98` in decimal and hexadecimal.
	- Using only one `print` and one loop.
	- Without storing numbers or strings in variables or importing modules.
	- Printing format: `[decimal] = [hexadecimal]`
- [5-print_comb2.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/5-print_comb2.py):  Python program that prints numbers from `0` to `99` two digits each.
        - Numbers are separated by `,` , except for the last number, which is followed by a new line.
        - Using no more than two `print` functions and one loop.
        - Without storing numbers or strings in variables or importing modules.
- [6-print_comb3.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/6-print_comb3.py): Python program that prints all possible different combinations of two digits in ascending order.
	- Numbers are separated by `,` , except for the last number, which is followed by a new line.
	- The two digits must be different - `01` and `10` are considered identical.
	- Using no more than three `print` functions and two loops.
	- Without storing numbers or strings in variables or importing modules.
- [7-islower.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/7-islower.py): Python function that checks for lowercase characters.
	- Returns `True` if `c` is lowercase, `False` otherwise.
	- Without importing modules or using `str.upper()` or `str.isupper()`.
- [8-uppercase.py)](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/8-uppercase.py): Python function that prints a string in uppercase followed by a new line.
	- Using no more than two `print` functions and one loop.
	- Without importing modules or using `str.upper()` or `str.isupper()`.
- [9-print_last_digit.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/9-print_last_digit.py): Python function that prints the last digit of a number.
	- Returns the value of the last digit.
	- Without importing modules.
- [10-add.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/10-add.py): Python function that returns the addition of two integers.
	- Without importing modules.
- [11-pow.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/11-pow.py): Python function that returns `a` to the power of `b`.
	- Without importing modules.
- [12-fizzbuzz.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/12-fizzbuzz.py): Python function that prints the numbers from `1` to `100` followed by a space.
	- For multiples of three, `Fizz` is printed instead of the number.
	- For multiples of five, `Buzz` is printed instead of the number.
	- For multiples of three and five, `FizzBuzz` is printed instead of the number.
	- Without importing modules.
- [13-insert_number.c](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/13-insert_number.c): C function that inserts a number into a sorted linked list.
	- If the function fails, returns `NULL`.
	- Otherwise, returns the address of the new node.
>	- Test files:
>	- [linked_lists.c](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/test_files/linked_lists.c): C functions that handle linked lists.
>	- [13-main.c](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/test_files/13-main.c): A test case for the function.
>	- [lists.h](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x01-python-if_else_loops_functions/lists.h): Header file containing definitions and prototypes of all types and functions used for the task.
- [100-print_tebahpla.py](): Python program that prints the alphabet in reverse order, alternating lowercase and uppercase, not followed by a new line.
	- Using only one `print` and one loop.
	- Without storing characters in variables or importing modules.
- [101-remove_char_at.p](): Python function that creates a copy of a string without the character at position `n`.
	- Without importing modules.
- [102-magic_calculation.py](): Python function matching exactly a bytecode provided by Holberton School.

> [test_files](https://github.com/Ebube-Ochemba/alx-higher_level_programming/tree/master/0x01-python-if_else_loops_functions/test_files): A folder of test files. Provided by Alx.
