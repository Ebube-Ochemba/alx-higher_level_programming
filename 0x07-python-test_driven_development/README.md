# Python - Test-driven development

> This project was on Test-driven development in python.

## Summary

I learnt about interactive test and the importance of tests, how to write Docstrings to create tests, and how to write documentation for each module and function, what basic option flags to create tests are and how to find edge cases.

1. To run all tests at the same time;
```sh
$ python3 -m doctest ./tests/*
```
2. To run a particular test;
```sh
$ python3 -m doctest <./path/to/test_file>
```
3. To read module documentation;
```sh
$ python3 -c 'print(__import__("my_module").__doc__)'
```
4. To read function documentation;
```sh
$ python3 -c 'print(__import__("my_module").my_function.__doc__)'
```

## Files

> Each file contains the solution to a task in the project.

- [x] [0-add_integer.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/0-add_integer.py): A function that adds 2 integers.
> 	- [x] [0-add_integer.txt](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/0-add_integer.txt): A file containing doctests for the function.
- [x] [2-matrix_divided.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/2-matrix_divided.py): A function that divides all elements of a matrix.
>	- [x] [2-matrix_divided.txt](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/2-matrix_divided.txt): A file containing doctests for the function.
- [x] [3-say_my_name.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/3-say_my_name.py): A function that prints My name is `<first name> <last name>`.
>	- [x] [3-say_my_name.txt](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/3-say_my_name.txt): A file containing doctests for the function.
- [x] [4-print_square.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/4-print_square.py): A function that prints a square with the character `#`.
>	- [x] [4-print_square.txt](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/4-print_square.txt): A file containing doctests for the function.
- [x] [5-text_indentation.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/5-text_indentation.py): A function that prints a text with 2 new lines after each of these characters: `.`, `?` and `:`.
>	- [x] [5-text_indentation.txt](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/5-text_indentation.txt): A file containing doctests for the function.
- [6-max_integer.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/6-max_integer.py): A function `def max_integer(list=[]):` provided by Alx.
>	- [x] [6-max_integer_test.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/6-max_integer_test.py): A file containing unittests for the function.
- [ ] [100-matrix_mul.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/100-matrix_mul.py): A function that multiplies 2 matrices.
>	- [ ] [100-matrix_mul.txt](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/100-matrix_mul.txt): A file containing doctests for the function.
- [ ] [101-lazy_matrix_mul.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/101-lazy_matrix_mul.py): A function that multiplies 2 matrices by using the module [NumPy](https://numpy.org/).
>	- [ ] [101-lazy_matrix_mul.txt](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/tests/101-lazy_matrix_mul.txt): A file containing doctests for the function.
- [ ] [102-python.c](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/102-python.c): A C function that prints Python strings.

> - [tests](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/tests): A folder containing `.txt` files each containing doctests for the tasks.
> - [main_test_files](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x07-python-test_driven_development/main_test_files): A folder of test files. Provided by Alx.
