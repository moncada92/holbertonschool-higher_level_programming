#!/usr/bin/python3
"""Unittest for class rectangle
"""

import io
import sys
import unittest
from models.square import Square
from models.base import Base


class Testsquare(unittest.TestCase):
    """test for class square"""

    def test_init(self):
        Base._Base__nb_objects = 0

    def test_validate_0(self):
        "Cases 0"
        rect0 = Square(1, 2)
        rect1 = Square(3, 2)
        self.assertEqual(rect0.id, 1)
        self.assertEqual(rect1.id, 2)

    def test_validate_1(self):
        "Cases 1"
        rect = Square(1, 3)
        self.assertIsInstance(rect, Square, True)
