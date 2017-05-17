#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def testMaxTest1(self):
        list1 = [5, 22, 50, 10]
        self.assertEqual(max_integer(list1), 50)

    def testMaxTest2(self):
        list1 = []
        self.assertEqual(max_integer(list1), None)

    def testMaxTest3(self):
        list1 = [5, 22, 50, "string"]
        with self.assertRaises(TypeError):
            max_integer(list1)

    def testMaxTest4(self):
        list1 = [5, True, False]
        self.assertEqual(max_integer(list1), 5)

    def testMaxTest5(self):
        self.assertEqual(max_integer([5.3, 8.4, 2.3]), 8.4)

    def testMaxTest6(self):
        with self.assertRaises(TypeError):
            max_integer([None, None])

    def testMax7(self):
        list1 = [10, 15, 2, 37]
        self.assertEqual(max_integer(list1), 37)


    def testMax8(self):
        list1 = [100, 15, 2, 37]
        self.assertEqual(max_integer(list1), 100)


    def testMax9(self):
        list1 = [10, -15, 2, 37]
        self.assertEqual(max_integer(list1), 37)


    def testMax10(self):
        list1 = [-10, -15, -2, -37]
        self.assertEqual(max_integer(list1), -2)


    def testMax11(self):
        list1 = [10]
        self.assertEqual(max_integer(list1), 10)
if __name__ == '__main__':
    unittest.main()
