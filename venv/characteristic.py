# 高级特性
# 输出1-100奇数
print(list(range(1, 101, 2)))
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前3个元素
print("取前3个元素：")
print([L[0], L[1], L[2]])
# 取前N个元素，也就是索引为0-(N-1)的元素，可以用循环：笨方法
r = []
n = 3
for i in range(n):
    r.append(L[i])
print("r：", r)
# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，
# Python提供了切片（Slice）操作符，能大大简化这种操作。
# 对应上面的问题，取前3个元素，用一行代码就可以完成切片：
print("切片（Slice）：", L[0:3])
# L[0:3]表示，从索引0开始取，直到索引3为止，
# 但不包括索引3。即索引0，1，2，正好是3个元素。
# 如果第一个索引是0，还可以省略：
print("切片2（Slice）：", L[:3])
# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print("倒数切片（Slice）：", L[-2:])
print("倒数切片2（Slice）：", L[-2:-1])  # 记住倒数第一个元素的索引是-1。

L = list(range(100))
# 前10个数
print(L[:10])
# 后10个数
print(L[-10:])
# 前11-20个数：
print(L[10:20])
# 前10个数，每两个取一个
print(L[:10:2])
# 所有数，每5个取一个：
print(L[::5])
# 甚至什么都不写，只写[:]就可以原样复制一个list：
print(L[:])

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
print("\n tuple：")
print((0, 1, 2, 3, 4, 5)[1:-1])
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print("字符串：", "ABCDEFGH"[:3])
print("字符串：", "ABCDEFGH"[::2])


# trim()函数，去除字符串首尾的空格
def trim(s):
    if not isinstance(s, (str)):
        raise TypeError("bad operand type")
    else:
        return trim_str(s)


def trim_str(s):
    if len(s) == 0:
        return s
    if s[0] == ' ':
        return trim_str(s[1:])
    if s[-1] == ' ':
        return trim_str(s[:-1])
    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
