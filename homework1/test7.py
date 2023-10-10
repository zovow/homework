list = [1, 2, 3, 4, 5]
new_list1 = []
new_list2 = []

length = len(list)
for x in list:
    new_list1.append(list[length-1])
    length -= 1
print(new_list1)

length = len(list)
x = length -1
while x >= 0:
    new_list2.append(list[x])
    x -= 1
print(new_list2)