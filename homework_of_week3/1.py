m = float(input())

result = ''
while m - int(m) != 0:
    m *= 2
    if m >= 1:
        result += str(1)
    else:
        result += str(0)
    m -= int(m)
print("0.", end='')
print(result)

