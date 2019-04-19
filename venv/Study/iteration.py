# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key, d[key])

# 默认情况下，dict迭代的是key。如果要迭代value，
# 可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。
for item in d.items():
    print(item)

# 由于字符串也是可迭代对象，因此，也可以作用于for循环：
for ch in 'ABC':
    print(ch)

# 所以，当我们使用for循环时，只要作用于一个可迭代对象，
# for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
# from collections import Iterable
# print(isinstance('abc',Iterable))   #str是否可迭代
# print(isinstance([1,2,3],Iterable))   #list是否可迭代
# print(isinstance(int,Iterable))   #int是否可迭代

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


# 查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if not L:
        return (None, None)
    min = L[0]
    max = L[0]
    for val in L:
        if val < min:
            min = val
        if val > max:
            max = val
    return (min, max)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
