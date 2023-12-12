#!/usr/bin/python3
"""Tests for the Base class"""

import unittest
import pep8

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """A class to test Rectangle Class"""

    def test_pep8_conformance_base(self):
        """Test that models/base.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """Test that tests/test_models/test_base.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def setUp(self):
        """Called for each test"""
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """Tests new rectangle"""
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_rectangle_2(self):
        """Tests new rectangle with all attrs"""
        new = Rectangle(2, 3, 5, 5, 4)
        self.assertEqual(new.width, 2)
        self.assertEqual(new.height, 3)
        self.assertEqual(new.x, 5)
        self.assertEqual(new.y, 5)
        self.assertEqual(new.id, 4)

    def test_new_rectangles(self):
        """Tests new rectangles"""
        new = Rectangle(1, 1)
        new2 = Rectangle(1, 1)
        self.assertEqual(False, new is new2)
        self.assertEqual(False, new.id == new2.id)

    def test_is_Base_instance(self):
        """Tests if Rectangle is an instance of Base"""
        new = Rectangle(1, 1)
        self.assertEqual(True, isinstance(new, Base))

    def test_incorrect_amount_attrs(self):
        """Tests error raised if 1 arg is passed"""
        with self.assertRaises(TypeError):
            new = Rectangle(1)

    def test_incorrect_amount_attrs_1(self):
        """ Tests error raised if no args is passed"""
        with self.assertRaises(TypeError):
            new = Rectangle()
