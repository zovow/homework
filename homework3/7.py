x = int(input())
y = int(input())

if x < y:
    x, y = y, x

result = 1

if x % y == 0:
    result = int(x / y)


while x % y != 0:
    r = x % y
    x, y = y, r
    result = y

print(result)
