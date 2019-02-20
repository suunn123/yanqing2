#!/Users/sun/Desktop/bin/python

age=int(input("请输入年龄："))
if age >=18:
    print("我年轻力壮")
elif age >=6:
    print("我还是个孩子")
elif age >=0:
    print("我是个儿童")
else:
    print("我不是人")

age=18
sex="f"
if sex == "f":
    print("我是女孩子")
    if age >= 18:
        print ("二八年华")
    elif age >=9:
        print ("我是儿童")
    elif age >=0:
        print ("我是婴儿")
elif sex == "g":
    print ("我是男生")
else :
    print ("我是大猩猩")





