n = int(input())
A = []
B = []
i = 0
while i < n:
    x = int(input())
    A.append(x)
    i += 1

i = 0
while i < n:
    j = 0
    data = 1
    while j < n:
        if j != i:
            data *= A[j]
        j += 1
    B.append(data)
    i += 1

print(B)
