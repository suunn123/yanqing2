# /Users/sun/Desktop/Pythontest/venv/bin/python
# coding=utf-8

for a in range(1, 10):

    for b in range(1, a + 1):
        print('{}x{}={}\t'.format(b, a, a * b), end='')
    print()

for n in range(1, 10):
    for m in range(1, n + 1):
        print('{}*{}={}\t'.format(m, n, n * m), end='')
    print()

print('{我}吃饭{好吃}'.format(我='青儿', 好吃='好吃啊'))

ai = 1
while ai <= 10:
    bi = 1
    while bi <= ai:
        print("*", end='')
        bi += 1
    print("\n")
    ai += 1

age = 0

while age < 7:
    if age > 2:
        print("我要上学")
        break
    print("我还是小孩子", age, "我不上学")
    age = age + 1

age = 6
while age < 9:
    age = age + 1
    if age - 1 < 2:
        print("我要抱抱")
        continue
    print("我要上学了")


def chufa(x, y):
    try:
        result = x / y
    #except ZeroDivisionError:
    #   print("除数不能为0")
    except Exception as e:
        print(e)
    else:
        print(result)
    finally:
        print("任何情况下有我的存在")


chufa(10, 5)
