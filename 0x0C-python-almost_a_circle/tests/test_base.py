#!/usr/bin/python3
"""Unittest for class Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """test for class Base"""

    def test_init(self):
        Base._Base__nb_objects = 0

    def test_validate_0(self):
        "Cases 0"
        base0 = Base()
        base1 = Base()
        self.assertEqual(base0.id, 1)
        self.assertEqual(base1.id, 2)

    def test_validate_1(self):
        "Cases 1"
        base2 = Base(3)
        base3 = Base(5)
        self.assertEqual(base2.id, 3)
        self.assertEqual(base3.id, 5)

    def test_validate_2(self):
        "Cases 2"
        base4 = Base()
        base5 = Base(3)
        base4.id = 10
        base5.id = 11
        self.assertEqual(base4.id, 10)
        self.assertEqual(base5.id, 11)

    def test_validate_3(self):
        "Cases 3"
        base6 = Base("hola")
        self.assertEqual(base6.id, "hola")

    def test_validate_4(self):
        "Cases 4"
        base7 = Base(6.5)
        self.assertEqual(base7.id, 6.5)

    def test_validate_5(self):
        "Cases 5"
        base8 = Base([2, 4])
        self.assertEqual(base8.id, [2, 4])

    def test_validate_6(self):
        "Cases 6"
        base9 = Base(-3)
        self.assertEqual(base9.id, -3)

    def test_validate_7(self):
        "Cases 7"
        base10 = Base({'id': 5})
        self.assertEqual(base10.id, {'id': 5})

    def test_validate_8(self):
        "Cases 8"
        base11 = Base((2, 4))
        self.assertEqual(base11.id, (2, 4))

    def test_validate_9(self):
        """Cases 9"""
        base12 = Base()
        self.assertEqual(str(type(base12)), "<class 'models.base.Base'>")
        self.assertEqual(base12.__dict__, {"id": 4})

    def test_validate_10(self):
        """Cases 10"""
        list_n = Base.to_json_string(None)
        self.assertEqual(list_n, "[]")
