"""
牛顿法求解本质上是一个迭代的过程
转换成求解f(x) = x^2 - 2 的零点的问题
我们只关心最后解出来的零点值是多少即可
"""
# 下述为第五题


def sort_two(c):
    diff = 1e-6
    while True:
        f = c ** 2 - 2
        f_der = 2 * c
        c_delta = -f/f_der
        c += c_delta
        if abs(c_delta) < diff:
            break
    print(c)


c = int(input())
# c为初始值

sort_two(c)

# 对于第六题来说，输入不同的c值，即可实现转换

sort_two(c/2)
sort_two(c/4)


# 对比结果我们可以发现，有影响，但是对整体结果影响不大
