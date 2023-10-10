"""
my_guess 表示初始猜测值
diff 表示二者之间的差异，初始化为1.0
后续每次操作都是my_guess向根号二靠近的过程
当差异值小于1e-6时，输出结束后的猜测值
"""


my_guess = int(input())
diff = 1.0
while diff > 1e-6:
    my_guess = my_guess + (2 - my_guess ** 2)/2
    diff = abs(2 - my_guess ** 2)

print(my_guess)