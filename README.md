# PycharmProjectsDemos
Python函数学习
## Python示例，学习合集

**本文会慢慢更新**

**高阶函数**
```
print("一个最简单的高阶函数：")
def add(x, y, f):
    return f(x)+f(y)
#当我们调用add(-5, 6, abs)时，参数x，y和f分别接收-5，6和abs，根据函数定义，我们可以推导计算过程为：
# x = -5
# y = 6
# f = abs
# f(x) + f(y) ==> abs(-5) + abs(6) ==> 11
# return 11
print(add(-5,6,abs))
```
# 最后更新时间2019年4月19日 12:04:33
