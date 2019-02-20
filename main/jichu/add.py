#/Users/sun/Desktop/Pythontest/venv/bin/python
#coding=utf-8
def add_method(x,y):
#有try可以重新赋值，在其他引用的时候
    try:
        return x/y
    except Exception as e:
         print(e)
#有print输出值就不可以重新赋值
   #print(x+y)

add_method(10,6)




print(add_method(23,9))

