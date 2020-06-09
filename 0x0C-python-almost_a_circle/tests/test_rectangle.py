#!/usr/bin/env python3
"""Unittest for class rectangle
"""

import io
import sys
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """test for class rectangle"""

    def test_init(self):
        Base._Base__nb_objects = 0

    def test_validate_0(self):
        "Cases 0"
        rect0 = Rectangle(1, 2)
        rect1 = Rectangle(3, 2)
        self.assertEqual(rect0.id, 3)
        self.assertEqual(rect1.id, 4)

    def test_validate_1(self):
        "Cases 1"
        rect = Rectangle(1, 3)
        self.assertIsInstance(rect, Rectangle, True)

    def test_validate_2(self):
        "Cases 2"
        rect = Rectangle(1, 3)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_validate_3(self):
        "Cases 3"
        self.assertRaises(TypeError, Rectangle, "2", 4)
        self.assertRaises(TypeError, Rectangle, 2, "4")

    def test_validate_4(self):
        "Cases 4"
        self.assertRaises(TypeError, Rectangle, "2", 4)
        self.assertRaises(TypeError, Rectangle, 2, "4")

    def test_validate_5(self):
        "Cases 5"
        self.assertRaises(ValueError, Rectangle, -2, 4)
        self.assertRaises(ValueError, Rectangle, 2, 0)

    def test_validate_6(self):
        "Cases 6"
        self.assertRaises(ValueError, Rectangle, 2, 4, -1, 2)
        self.assertRaises(ValueError, Rectangle, 2, 1, 2, -1)

    def test_validate_7(self):
        "Cases 7"
        self.assertRaises(TypeError, Rectangle, 3, 4, "b", 5)
        self.assertRaises(TypeError, Rectangle, 2, 3, 4, "c")

    def test_validate_8(self):
        "Cases 8"
        self.assertRaises(TypeError, Rectangle, [2], 4)
        self.assertRaises(TypeError, Rectangle, 2, [3])

    def test_validate_9(self):
        "Cases 9"
        self.assertRaises(TypeError, Rectangle, (2, 4), 4)
        self.assertRaises(TypeError, Rectangle, 2, (2, 4))

    def test_validate_10(self):
        "Cases 10"
        self.assertRaises(TypeError, Rectangle, {'width': 5}, 4)
        self.assertRaises(TypeError, Rectangle, 2, {'height': 5})

    def test_validate_11(self):
        "Cases 11"
        self.assertRaises(TypeError, Rectangle, 5.6, 4)
        self.assertRaises(TypeError, Rectangle, 2, 4.5)

    def test_validate_12(self):
        "Cases 12"
        self.assertRaises(TypeError, Rectangle, 6, 5, [2], 4)
        self.assertRaises(TypeError, Rectangle, 4, 2, 2, [3])

    def test_validate_13(self):
        "Cases 13"
        self.assertRaises(TypeError, Rectangle, 6, 5, (2, 4), 4)
        self.assertRaises(TypeError, Rectangle, 6, 5, 2, (2, 4))

    def test_validate_14(self):
        "Cases 14"
        self.assertRaises(TypeError, Rectangle, 6, 5, {'width': 5}, 4)
        self.assertRaises(TypeError, Rectangle, 6, 5, 2, {'height': 5})

    def test_validate_15(self):
        "Cases 15"
        self.assertRaises(TypeError, Rectangle, 6, 5, 5.6, 4)
        self.assertRaises(TypeError, Rectangle, 6, 5, 2, 4.5)

    def test_Rectangle16(self):
        "Cases 16"
        r = Rectangle(24, 98)
        self.assertEqual(r.width, 24)
        self.assertEqual(r.height, 98)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_validate_17(self):
        "Case 17"
        with self.assertRaises(TypeError) as e:
            r = Rectangle(None)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

    def test_validate_18(self):
        """Case 18"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(2)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

    def test_validate_19(self):
        """Case 19"""
        rect = Rectangle(2, 3)
        self.assertEqual(rect.area(), 6)

    def test_validate_20(self):
        """Case 20"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 10/10 - 10/10")
        r.update(67, 2)
        self.assertEqual(r.__str__(), "[Rectangle] (67) 10/10 - 2/10")
        r.update(68, 3, 4)
        self.assertEqual(r.__str__(), "[Rectangle] (68) 10/10 - 3/4")
        r.update(98, 12, 9, 8)
        self.assertEqual(r.__str__(), "[Rectangle] (98) 8/10 - 12/9")
        r.update(14, 22, 13, 11, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (14) 11/12 - 22/13")
        r = Rectangle(1, 1)
        r.update(76, 2, 3, 4, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (76) 4/5 - 2/3")

    def test_validate_21(self):
        """Case 21"""
        r = Rectangle(10, 10, 10, 10, 1)
        r.update(height=12)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 10/10 - 10/12")
        r.update(width=12, x=2)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 2/10 - 12/12")
        r.update(y=1, width=2, x=3, id=2)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 3/1 - 2/12")

    def test_validate_22(self):
        """Case 22"""
        r = Rectangle(1, 2, 3, 4, 12)
        r.update()
        self.assertEqual(r.__str__(), "[Rectangle] (12) 3/4 - 1/2")

    def test_validate_23(self):
        """Case 23"""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = {'x': 1, 'width': 10, 'id': 9, 'height': 2, 'y': 9}
        r3 = r1.to_dictionary()
        self.assertEqual(r2, r3)
    
    def test_rectangle24(self):
        """Case 24"""
        r5 = Rectangle(2, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r5.display()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(output, '##\n##\n')

    def test_rectangle25(self):
        """Case 25"""
        r6 = Rectangle(2, 3, 2, 2)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r6.display()
        output = captured_output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertEqual(output, '\n' * 2 + (' ' * 2 + '#' * 2 + '\n') * 3)
