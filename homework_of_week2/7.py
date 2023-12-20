"""
本题做法和 5 6 题相似，都是用迭代法求解
仅需更改初始迭代函数即可
"""


def sort_two(c):
    diff = 1e-6
    while True:
        f = c ** 3 - 2
        f_der = 3 * (c ** 2)
        c_delta = -f/f_der
        c += c_delta
        if abs(c_delta) < diff:
            break
    print(c)


sort_two(10)
