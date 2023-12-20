def cube_root(x, threshold=0.0001):
    left = 0
    right = x

    while right - left > threshold:
        mid = (left + right) / 2
        cube = mid ** 3

        if cube > x:
            right = mid
        else:
            left = mid

    return left

x = int(input())
print(cube_root(x))