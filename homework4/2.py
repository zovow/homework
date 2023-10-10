import time
import numpy as np

begin = time.time()

# 程序开始，下面以冒泡排序为例

pop_list = np.random.randint(100000, size=1000)
# print("排序之前", pop_list)


def pupple_sort(pop_list):
    count = len(pop_list)
    for i in range(count-1):
        for j in range(count-i-1):
            if pop_list[j] > pop_list[j+1]:
                pop_list[j], pop_list[j+1]=pop_list[j+1], pop_list[j]

pupple_sort(pop_list)
# print("排序之后", pop_list)

end = time.time()

time_of_program = end - begin
print(time_of_program)
