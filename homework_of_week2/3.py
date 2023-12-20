"""
记人，狼，菜，羊分别为0，1，2，3
而且在这岸记状态为0，在对岸状态为1
为（1， 1， 1， 1）时结束
"""

# 判断是否安全
def pending_safe(now):
    if (now[0] != now[1] and now[1] == now[3]) or (now[0] != now[3] and now[2] == now[3]):
        return False
    return True


# 寻找路径
def find_way(now, my_way, visited):
    # 都在对岸就退出
    if now == (1, 1, 1, 1):
        print("路径为：", my_way)
        return

    for way in ways:
        new = tuple(now[i] + way[i] for i in range(4))  # 移动之后的状态
        if 0 <= new[0] <= 1 and 0 <= new[1] <= 1 and 0 <= new[2] <= 1 and 0 <= new[3] <= 1:  # 不能超出范围
            if pending_safe(new) == True and (new in visited) == False:   # 都安全且该状态未被访问
                visited.add(new)
                find_way(new, my_way + [new], visited)
                visited.remove(new)
                # 访问结束之后就要移除new，为下一次for循环做好铺垫

# 初始化
now = (0, 0, 0, 0)

# 判断是否访问过
visited = set()
visited.add(now)

# 移动路径
ways =[
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (1, 0, 1, 0),
    (1, 0, 0, 1),
    (-1, 0, 0, 0),
    (-1, -1, 0, 0),
    (-1, 0, -1, 0),
    (-1, 0, 0, -1)
]

find_way(now, [now], visited)
