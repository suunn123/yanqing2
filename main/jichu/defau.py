# /Users/sun/Desktop/Pythontest/venv/bin/python
# coding=utf-8
import value as value

from Forfor import age


def student(name: object, sex: object, age: object = 7) -> object:
    return name + "," + sex + "," + str(age) + "岁"


print(student("青儿", "女", 18))
print(student(sex="男", name="sun"))


def student1(profile, *mytuple):
    out_put = ""
    for parameter in mytuple:
        if not out_put:
            out_put = out_put + parameter
    return profile + ";" + out_put


print(u"学生", u"大鹏", u"男性", u"7岁")


def student2(profile, mytuple):
    out_put = ""
    for parameter in mytuple:
        if not out_put:
            out_put = out_put + parameter
    return profile + ";" + out_put


print(u"学生", u"大鹏", u"男性", u"7岁")

