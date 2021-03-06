#!/usr/bin/python3
"""Unittest for class Square
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

    def test_validate_2(self):
        "Cases 2"
        rect = Square(1)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.height, 1)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)
        rect_1 = Square(1, 2, 4)
        self.assertEqual(rect_1.width, 1)
        self.assertEqual(rect_1.height, 1)
        self.assertEqual(rect_1.x, 2)
        self.assertEqual(rect_1.y, 4)

    def test_validate_3(self):
        "Cases 3"
        self.assertRaises(TypeError, Square, "2")
        self.assertRaises(TypeError, Square, "hola")

    def test_validate_4(self):
        "Cases 4"
        self.assertRaises(TypeError, Square, "2.5")
        self.assertRaises(TypeError, Square, "4.5")

    def test_validate_5(self):
        "Cases 5"
        self.assertRaises(ValueError, Square, -2)
        self.assertRaises(ValueError, Square, 0)

    def test_validate_6(self):
        "Cases 6"
        self.assertRaises(ValueError, Square, 2, 4, -1)
        self.assertRaises(ValueError, Square, 2, -1, 2,)

    def test_validate_7(self):
        "Cases 7"
        self.assertRaises(TypeError, Square, 3, 4, "b")
        self.assertRaises(TypeError, Square, 2, "c", 6)

    def test_validate_8(self):
        "Cases 8"
        self.assertRaises(TypeError, Square, [2])
        self.assertRaises(TypeError, Square, ['hello'])

    def test_validate_9(self):
        "Cases 9"
        self.assertRaises(TypeError, Square, (2, 4))
        self.assertRaises(TypeError, Square, ('2', '4'))

    def test_validate_10(self):
        "Cases 10"
        self.assertRaises(TypeError, Square, {'size': 5})
        self.assertRaises(TypeError, Square, {'size': 'dos'})

    def test_validate_11(self):
        "Cases 11"
        self.assertRaises(TypeError, Square, 5.6)
        self.assertRaises(TypeError, Square, 4.5)

    def test_validate_12(self):
        "Cases 12"
        self.assertRaises(TypeError, Square, 6, 5, [2])
        self.assertRaises(TypeError, Square, 4, [3], 8)

    def test_validate_13(self):
        "Cases 13"
        self.assertRaises(TypeError, Square, 6, (2, 4), 4)
        self.assertRaises(TypeError, Square, 6, 5, (2, 4))

    def test_validate_14(self):
        "Cases 14"
        self.assertRaises(TypeError, Square, 6, {'x': 5}, 4)
        self.assertRaises(TypeError, Square, 6, 5, {'y': 5})

    def test_validate_15(self):
        "Cases 15"
        self.assertRaises(TypeError, Square, 6, 5.6, 4)
        self.assertRaises(TypeError, Square, 6, 2, 4.5)

    def test_Square16(self):
        "Cases 16"
        r = Square(24)
        self.assertEqual(r.size, 24)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_validate_17(self):
        "Case 17"
        with self.assertRaises(TypeError) as e:
            s = Square(None)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test_validate_19(self):
        """Case 19"""
        rect = Square(2)
        self.assertEqual(rect.area(), 4)

    def test_validate_20(self):
        """Case 20"""
        r = Square(5)
        r.update(12)
        self.assertEqual(r.__str__(), "[Square] (12) 0/0 - 5")
        r.update(1, 2)
        self.assertEqual(r.__str__(), "[Square] (1) 0/0 - 2")
        r.update(1, 2, 3)
        self.assertEqual(r.__str__(), "[Square] (1) 3/0 - 2")
        r.update(1, 2, 3, 4)
        self.assertEqual(r.__str__(), "[Square] (1) 3/4 - 2")
        r = Square(1, 1)
        r.update(76, 2, 3, 4)
        self.assertEqual(r.__str__(), "[Square] (76) 3/4 - 2")

    def test_validate_21(self):
        """Case 21"""
        r = Square(10, 10, 10, 1)
        r.update(size=12)
        self.assertEqual(r.__str__(), "[Square] (1) 10/10 - 12")
        r.update(y=12, x=2)
        self.assertEqual(r.__str__(), "[Square] (1) 2/12 - 12")
        r.update(y=1, size=2, x=3, id=2)
        self.assertEqual(r.__str__(), "[Square] (2) 3/1 - 2")

    def test_validate_22(self):
        """Case 22"""
        r = Square(1, 2, 3, 4)
        r.update()
        self.assertEqual(r.__str__(), "[Square] (4) 2/3 - 1")

    def test_validate_23(self):
        """Case 23"""
        r1 = Square(10, 2, 1, 9)
        r2 = {'id': 9, 'x': 2, 'size': 10, 'y': 1}
        r3 = r1.to_dictionary()
        self.assertEqual(r2, r3)

    def test_validate_24(self):
        s1 = Square(12, 12, 2)
        s2 = Square(2, 4)
        Square.save_to_file([s1, s2])
        res = '[{"x": 12, "y": 2, "id": 21, "size": 12},' + \
            ' {"x": 4, "y": 0, "id": 22, "size": 2}]'
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))

    def test_validate_25(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual((s1 == s2), False)
        self.assertEqual((s1 is s2), False)

    def test_validate_26(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 2)

    def test_validate_27(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        e = []
        Square.save_to_file(e)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_validate_28(self):
        with self.assertRaises(TypeError) as e:
            s = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'",
            str(e.exception))

    def test_validate_29(self):
        s = Square(6, 0)
        self.assertEqual(s.x, 0)
        with self.assertRaises(ValueError) as e:
            s = Square(0, 2)
        self.assertEqual(
            "width must be > 0",
            str(e.exception))
        s = Square(1, 0, 0, 0)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 0)

    def test_validate_30(self):
        s = Square(4, 2)
        self.assertEqual(s.area(), 16)
        s = Square(2, 20, 1)
        self.assertEqual(s.area(), 4)
        s = Square(10, 5, 6, 2)
        self.assertEqual(s.area(), 100)
        s = Square(12, 7, 4, 6)
        self.assertEqual(s.area(), 144)

    def test_validate_31(self):
        s = Square(3, 7, 1, 1)
        self.assertEqual(s.__str__(), "[Square] (1) 7/1 - 3")
        s = Square(1, 1, 0)
        self.assertEqual(s.__str__(), "[Square] (32) 1/0 - 1")
        s = Square(1, 1)
        self.assertEqual(s.__str__(), "[Square] (33) 1/0 - 1")

    def test_validate_32(self):
        r = Square(5)
        self.assertEqual(r.size, 5)
        r.size = 25
        self.assertEqual(r.size, 25)
        with self.assertRaises(TypeError) as e:
            r.size = "hello"
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.size = [1, 2]
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.size = (2,)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.size = {"a": 1}
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.size = True
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r.size = {1, 2}
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test_validate_33(self):
        s = Square(12, 2, 1, 9)
        s_dict = {'x': 2, 'size': 12, 'y': 1, 'id': 9}
        self.assertEqual(s.to_dictionary(), s_dict)
        self.assertEqual(s.to_dictionary() is s_dict, False)
        s = Square(12, 4, 15)
        s_dict = {'x': 4, 'id': 35, 'y': 15, 'size': 12}
        self.assertEqual(s.to_dictionary(), s_dict)
        self.assertEqual(s.to_dictionary() is s_dict, False)
        s = Square(96, 313)
        s_dict = {'x': 313, 'id': 36, 'y': 0, 'size': 96}
        self.assertEqual(s.to_dictionary(), s_dict)
        self.assertEqual(s.to_dictionary() is s_dict, False)

    def test_validate_34(self):
        r = Square(12, 12, 2)
        d = r.to_dictionary()
        json_d = Base.to_json_string([d])
        self.assertEqual(type(json_d), str)
        self.assertEqual(d, {'id': 37, 'x': 12, 'y': 2, 'size': 12})

    def test_validate_35(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 2)
