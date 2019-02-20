#/Users/sun/Desktop/Pythontest/venv/bin/python
#coding=utf-8
import unittest

def add(x,y):
    return x+y


class demo(unittest.TestCase):
    def setUp(self):
        print("I am set up")

    def test_demo(self):
        print("my firt test")
        self.assertEqual(add(10,1),11,"assert equal")
    def test_demo2(self):
        print("my test demo2")
        self.assertEqual(add(10,10),21,"asser equal demo2")
    def tearDown(self):
        print("I am tear down")
