import random
import time

def pupple_sort(pop_list):
    count = len(pop_list)
    for i in range(count-1):
        for j in range(count-i-1):
            if pop_list[j] > pop_list[j+1]:
                pop_list[j],pop_list[j+1]=pop_list[j+1],pop_list[j]
    # print(pop_list)

def selection_sort(array):
    for i in range(len(array)-1):
        min_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
    # print(array)

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    return merge(merge_sort(left), merge_sort(right))

def merge(left,right):
    result = []
    i = j = 0
    while i < len(left) and j < len(left):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


list = []
n = int(input())
x = random.randint(1 * n, 2 * n)
i = 1
while i < x:
    list.append(random.randint(1, 99999))
    i += 1

# print(list)
# 注释内容均为测试使用
start_1 = time.time()
selection_sort(list)
end_1 = time.time()
print(end_1 - start_1)

start_2 = time.time()
selection_sort(list)
end_2 = time.time()
print(end_2 - start_2)

start_3 = time.time()
merge_sort(list)
end_3 = time.time()
print(end_3 - start_3)

# 经过测试，归并排序在10，100，1000等数量级的数据规模上
# 其速度遥遥领先选择排序和冒泡排序，而后两者的速度接近，相差不大
