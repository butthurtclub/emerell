__author__ = 'emerell'

import unittest
from math import hypot

__all__ = (
    'Point',
)


class Point:
    def _validate(self, value):
        return float(value)

    def __init__(self, x=0.0, y=0.0):
        self._x = self._validate(x)
        self._y = self._validate(y)

    def __str__(self):
        return f'({self._x}, {self._y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def distance(self, other):
        return hypot(other.x - self.x, other.y - self.y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, x):
        self._x = self._validate(x)

    @y.setter
    def y(self, y):
        self._y = self._validate(y)


class TestPoint(unittest.TestCase):
    def test_validation(self):
        x = Point(10, 5)
        y = Point(10.7, 2.42)

        self.assertEqual(x._validate(10), 10.0)
        self.assertEqual(y._validate(10.7), 10.7)

    def test_init(self):
        p = Point(6, 7)
        self.assertEqual(p.x, 6.0)
        self.assertEqual(p.y, 7.0)

    def test_operators(self):
        a = Point(3, 4)
        b = Point(7, 6)
        c = Point(3.0, 4.0)

        self.assertTrue(a != b)
        self.assertFalse(a == b)
        self.assertTrue(a == c)
        self.assertFalse(a != c)

        b.x = 3
        b.y = 4

        self.assertTrue(a == b)
        self.assertFalse(a != b)

    def test_distance(self):
        a = Point(0, 3)
        b = Point(4, 0)
        c = Point(0.0, -3.0)
        d = Point(-4.0, 0.0)

        self.assertEqual(a.distance(b), 5)
        self.assertEqual(b.distance(a), 5)
        self.assertEqual(c.distance(d), 5.0)
        self.assertEqual(d.distance(c), 5.0)

    def test_presentation(self):
        a = Point(5, 5)
        b = Point(6.0, 10.0)
        c = Point(7, 8.2)

        self.assertEqual(str(a), '(5.0, 5.0)')
        self.assertEqual(str(b), '(6.0, 10.0)')
        self.assertEqual(str(c), '(7.0, 8.2)')


if __name__ == '__main__':
    unittest.main()