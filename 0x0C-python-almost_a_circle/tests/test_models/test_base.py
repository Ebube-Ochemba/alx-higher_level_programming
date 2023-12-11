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

    def test_init(self):
        """Tests that id is updated when arg is passed"""
        base = Base(1)
        self.assertEqual(base.id, 1)

    def test_init_default(self):
        """Tests that id is updated when arg isn't passed"""
        base = Base()
        self.assertEqual(base.id, 1)

    def test_module_docstring(self):
        """Tests for the module docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the Base class docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)
