#!/usr/bin/python3
"""Tests for the Base class"""

import unittest
import pep8

from models.base import Base


class TestBase(unittest.TestCase):
    """A class to test Base Class"""

    def test_pep8_conformance_base(self):
        """Test that models/base.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_base(self):
        """Test that tests/test_models/test_base.py conforms to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def setUp(self):
        """Called for each test"""
        Base._Base__nb_objects = 0

    def test_init(self):
        """Tests that id when arg is passed"""
        base = Base(1)
        self.assertEqual(base.id, 1)

    def test_init_default(self):
        """Tests that id when arg isn't passed"""
        base = Base()
        self.assertEqual(base.id, 1)

    def test_id_nb_objects(self):
        """Tests nb object attribute"""
        base1 = Base()
        base2 = Base()
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)

    def test_id_mix(self):
        """Tests nb object attr and passed id"""
        base1 = Base()
        base2 = Base(1024)
        base3 = Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 1024)
        self.assertEqual(base3.id, 2)

    def test_string_id(self):
        """Test string id"""
        base = Base('7')
        self.assertEqual(base.id, '7')

    def test_more_args_id(self):
        """Tests passing more args to init method"""
        with self.assertRaises(TypeError):
            base = Base(5, 6)

    def test_access_private_attrs(self):
        """Tests access to private attributes"""
        base = Base()
        with self.assertRaises(AttributeError):
            base.__nb_objects
