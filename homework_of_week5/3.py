import numpy as np

insert_list = np.random.randint(100, size=10)


def insert_sort(insert_list):
    count = len(insert_list)
    for i in range(count):
        now = i
        while insert_list[now-1] > insert_list[now] and now - 1 >= 0:
            insert_list[now-1], insert_list[now] = insert_list[now], insert_list[now-1]
            now -= 1


insert_sort(insert_list)

print(insert_list)

