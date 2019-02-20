#/Users/sun/Desktop/Pythontest/venv/bin/python
#coding=utf-8
import unittest

def add(x,y):
    return x+y

class Demo(unittest.TestCase):
    def setUp(self):
        print("I am set up")
    def test_demo(self):
        print("my first test demo")
        self.assertEqual(add(10,9),11,"比较是否等于")

    def test_demo2(self):
        self.assertEqual(add(32,3),35,"第二个比较")
        print("my secend test demo")
    def tearDown(self):
        print("I am tear dowm")

