import math
a = int(input())
count = 0
i = 2
while i < math.sqrt(a):
    if a % i == 0:
        count += 1
    i += 1
if count == 0:
    print("a是质数")
else:
    print("a不是质数")
