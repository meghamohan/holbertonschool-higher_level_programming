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
'''
    def testMaxTest4(self):
        list1 = [5, True, False]
        self.assertEqual(max_integer(list1), 5)

    def testMaxTest5(self):
        self.assertEqual(max_integer([5.3, 8.4, 2.3]), 8.4)

    def testMaxTest6(self):
        with self.assertRaises(TypeError):
            max_integer([None, None])
'''
if __name__ == '__main__':
    unittest.main()
