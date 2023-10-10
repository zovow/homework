
import math
import numpy as np

def add_all(a, b):
    i = 1
    sum = 0
    while i < 10000:
        i += 1
        x = np.random.uniform(2, 3)
        sum += x**2 + 4*x*math.sin(x)
    return sum / 10000

result = add_all(2, 3)

print(result)

