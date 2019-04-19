# print absolute value of an integer:
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# 字符串和编码
a = 100
if a >= 0:
    print(a)
else:
    print(-a)
print(ord('a'))
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')
x = b'ABC'
print(x)
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print('ABC'.encode('ascii').decode('ascii'))
print('中文'.encode('utf-8').decode('utf-8'))
print(b'\xe4\xb8\xad\xff'.decode('utf-8', errors='ignore'))
print(len('abc'))
print(len('中文'))
print(u'中文显示正常')
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# 使用list和tuple
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
# 最后一个字符 可以用-1 以此类推，可以获取倒数第2个、倒数第3个
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
classmates.append('Adam')
print(classmates)
classmates.insert(1, 'Jack')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(1)
print(classmates)
classmates[1] = 'Sarah'
print(classmates)
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
print(s[2][1])
# tuple
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
a = ()
b = (1)
c = [2]
d = (3,)
e = (4, 5, 6)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# 条件判断
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('your age is', age)
    print('teenager')
else:
    print('your age is', age)
    print('kid')
# birth = int(input('birth: '))
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
height = 1.75
weight = 80.5
bmi = weight / pow(height, 2)
if bmi < 18.5:
    print('过轻')
elif bmi >= 18.5 and bmi < 25:
    print('正常')
elif bmi >= 25 and bmi < 28:
    print('过重')
elif bmi >= 28 and bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')

# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum += x
print(sum)

sum = 0
for x in list(range(101)):
    sum += x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello,', x, '!')

n = 1
while n <= 100:
    if n > 10:  # 当n = 11时，条件满足，执行break语句
        break  # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

# dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
d['Adam'] = 67
print(d, d['Adam'])
d['Jack'] = 90
print(d, d['Jack'])
# 判断key是否存在
print('Thomas' in d)
print(d.get('Thomas'))
# 指定值
print(d.get('Thomas', 100))
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(d.pop('Bob'))
print(d)
# set
s = set([1, 2, 3])
print(s)
s.add(4)
print(s)
# 通过remove(key)方法可以删除元素：
s.remove(4)
print(s)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

# 函数 https://docs.python.org/3/library/functions.html#func-dict 官方文档
# abs 求绝对值
print('绝对值：', abs(100))
print('绝对值：', abs(-20))
print('绝对值：', abs(13.54))
print('最大值：', max(2, 3, 1, -5))
# 数据类型转换
print(type(int('123')))
print(int(12.33))
print(type(str(1.23)))
print(type(float('12.34')))
print(bool(0), bool(1), bool(''))
a = abs  # 变量a指向abs函数
print('绝对值：', a(-1))  # 所以也可以通过a调用abs函数


# 定义函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


print('绝对值：', my_abs(-99))


# 空函数
def nop():
    pass


if age >= 18:
    pass
# print(my_abs('A'))
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)


# 定义函数时，需要确定函数名和参数个数；
#
# 如果有必要，可以先对参数的数据类型做检查；
#
# 函数体内部可以用return随时返回函数结果；
#
# 函数执行完毕也没有return语句时，自动return None。
#
# 函数可以同时返回多个值，但其实就是一个tuple。
def quadratic(a, b, c):
    L = [a, b, c]
    for x in L:
        if not isinstance(x, (int, float)):
            raise TypeError("数据类型有误：", "参数类型必须为整形或浮点型!")
    delta = b * b - 4 * a * c
    if delta < 0:
        print('无解')
        return
    else:
        x1 = (0 - b + math.sqrt(delta)) / (2 * a)
        x2 = (0 - b - math.sqrt(delta)) / (2 * a)
        return x1, x2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')


def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))
print(power(15, 2))


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('ChenPeng', 'F')
enroll('iZhu', 'B', city='ChangSha')


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 把函数的参数改为可变参数 *
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))
print(calc(1, 3, 5, 7))

# 在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
print(calc(*nums))


# 关键字参数可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)


person('Michael', 30)
person('Michael', 30, city="BeiJing")
person('Michael', 30, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Michael', 30, city=extra["city"], job=extra["job"])
# 简化
person('Jack', 24, **extra)


# 命名关键字参数
# 检查是否有city和job参数：
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
# 比如定义一个函数，包含上述若干种参数：
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


# 在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
# 传tuple和dict
print("传tuple和dict")
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)


# 计算两个数的乘积，请稍加改造，变成可接收一个或多个数并计算乘积：
def product(*args):
    sum = 1
    if not args:
        raise TypeError('不可为空')
    for x in args:
        if not isinstance(x, (int, float)):
            raise TypeError("参数类型错误")
        sum = sum * x
    return sum


# 测试
print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')

# 递归函数
print("递归函数")
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)
print(fact(5))
print(fact(64))
# 如果我们计算fact(5)，可以根据函数定义看到计算过程如下：
#
# ===> fact(5)
# ===> 5 * fact(4)
# ===> 5 * (4 * fact(3))
# ===> 5 * (4 * (3 * fact(2)))
# ===> 5 * (4 * (3 * (2 * fact(1))))
# ===> 5 * (4 * (3 * (2 * 1)))
# ===> 5 * (4 * (3 * 2))
# ===> 5 * (4 * 6)
# ===> 5 * 24
# ===> 120
# 递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
#
# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加
# 一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(100))

#汉诺塔的移动
def hanoi(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        hanoi(n - 1, a, c, b)
        print(a, '-->', c)
        hanoi(n - 1, b, a, c)
# 调用
hanoi(4, 'A', 'B', 'C')