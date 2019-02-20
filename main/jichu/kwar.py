# /Users/sun/Desktop/Pythontest/venv/bin/python
# coding=utf-8
from typing import Tuple


def add(x, **kwargs):
    print(x)
    print(kwargs)


add(1, name1="world", age1="sun", )


def fun(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


fun(1, 2, 3, 4, name="hello", age=20)


def add(x, **kwargs):
    total = x
    for arg, value in kwargs.items():
        print("输出" + arg)
        total += value
    return total


print(add(12, y=7, v=8))

print(("*") * 55)


def add(x, kwargs):
    total = x
    for arg, value in kwargs.items():
        print("输出" + arg)
        total += value
    return total


input_dic = {"y": 11, "t": 12, "u": 23, "h": 5}
print(add(10, input_dic))




def sqr(x):
    return x**2
z= (4, 5, 8)
#map前面加list
print(list(map(sqr,z)))




def add(o,l):
    return o+l
x1=(2,3,4)
y1=(4,5,6)
#map前面加list
print(list(map(add,x1,y1)))
