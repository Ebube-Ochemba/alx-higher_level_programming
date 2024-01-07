# Python - Inheritance

> This project was on class inheritance in python.

## Summary

I learnt about superclass, baseclass or parentclass. Also, how to inherit class from another, how to define a class with multiple base classes, the default class every class inherit from, how to override a method or attribute inherited from the base class, which attributes or methods are available by heritage to subclasses, what is the purpose of inheritance and what are, when and how to use `isinstance`, `issubclass`, `type` and `super` built-in functions.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-lookup.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/0-lookup.py): A function that returns the list of available attributes and methods of an object
- [ ] [1-my_list.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/1-my_list.py): A class `MyList` that inherits from `list`.
	- [1-my_list.txt](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/tests/1-my_list.txt): A doctest for [`1-my_list.py`](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/1-my_list.py).
- [x] [2-is_same_class.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/2-is_same_class.py): A function that returns `True` if the object is exactly an instance of the specified class, otherwise `False`.
- [x] [3-is_kind_of_class.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/3-is_kind_of_class.py): A function that returns `True` if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class, otherwise `False`.
- [x] [4-inherits_from.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/4-inherits_from.py): A function that returns `True` if the object is an instance of a class that inherited (directly or indirectly) from the specified class, otherwise `False`.
- [x] [5-base_geometry.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/5-base_geometry.py): An empty class `BaseGeometry`.
- [x] [6-base_geometry.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/6-base_geometry.py): A class `BaseGeometry` (based on [`5-base_geometry.py`](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/5-base_geometry.py)).
> (check task for specifications)
- [ ] [7-base_geometry.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/7-base_geometry.py): A class `BaseGeometry` (based on [`6-base_geometry.py`](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/6-base_geometry.py)).
> (check task for specifications)

	- [7-base_geometry.txt](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/tests/7-base_geometry.txt):  A doctest for [7-base_geometry.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/7-base_geometry.py).
- [x] [8-rectangle.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/8-rectangle.py):  A class `Rectangle` that inherits from `BaseGeometry` ([`7-base_geometry.py`](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/7-base_geometry.py)).
> (check task for specifications)
- [x] [9-rectangle.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/9-rectangle.py): A class `Rectangle` that inherits from `BaseGeometry` ([`7-base_geometry.py`](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/7-base_geometry.py)) (based on [`8-rectangle.py`](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/8-rectangle.py)).
> (check task for specifications)
- [x] [10-square.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/10-square.py): A class `Square` that inherits from `Rectangle` ([`9-rectangle.py`](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/9-rectangle.py)).
> (check task for specifications)
- [x] [11-square.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/11-square.py): A class `Square` that inherits from `Rectangle` ([`9-rectangle.py`](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/9-rectangle.py)) (based on [`10-square.py`](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/10-square.py)).
> (check task for specifications)
- [x] [100-my_int.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/100-my_int.py): A class `MyInt` that inherits from `int`.
- [x] [101-add_attribute.py](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/101-add_attribute.py): A function that adds a new attribute to an object if it’s possible

> - [tests](https://github.com/Ebube-Ochemba/alx-higher_level_programming/tree/master/0x0A-python-inheritance/tests): A folder of Doctest `.txt` files.
> - [main_test_files](https://github.com/Ebube-Ochemba/alx-higher_level_programming/blob/master/0x0A-python-inheritance/main_test_files): A folder of test files. Provided by Alx.
