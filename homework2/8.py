"""
第一种方法：傅里叶级数的拓展
Π²/8 = Σ1/(2k-1)²
"""
import math
import time

i = 1
my_pai1 = 0
start_1 = time.time()
while i < 10000:
    my_pai1 += 1 / ((2 * i - 1) ** 2)
    i += 1
end_1 = time.time()

result1 = math.sqrt(8 * my_pai1)

print('{:.10f}'.format(result1))
print(end_1 - start_1)

"""
第二种方法：
Π = 4(Σ(-1)**(i+1) * (1/2*i-1))
"""

i = 1
my_pai2 = 0
start_2 = time.time()
while i < 10000:
    my_pai2 += (-1) ** (i+1) * (1/(2 * i-1))
    i += 1
end_2 = time.time()

result2 = 4 * my_pai2
print('{:.10f}'.format(result2))
print(end_2 - start_2)

"""
第三种方法：连乘
Π/2 = ∏(2*i/(2*i-1) * 2*i/(2*i+1))
"""

i = 1
my_pai3 = 1
start_3 = time.time()
while i < 10000:
    my_pai3 *= 4*(i**2)/(4*(i**2) - 1)
    i += 1
end_3 = time.time()

result3 = my_pai3 * 2
print('{:.10f}'.format(result3))
print(end_3 - start_3)

"""
我们可以看到，在三种算法都考虑10000个级数的情况下
算法一明显更接近圆周率的真实值
而算法二和算法三的差值不大，性能接近
在运行时间方面，算法一的运行时间也是最短的
算法二和算法三的运行时间接近
综上算法一的效率和性能最好，算法二和算法三接近
"""