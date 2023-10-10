# 以下实现一个链表的增删查改

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class my_list:
    def __init__(self):
        self.head = None

    def print(self):
        now = self.head
        while now:
            print(now.value, end=',')
            now = now.next
        print()
    def add(self, value):
        newnode = Node(value)
        if self.head == None:
            self.head = newnode
        else:
            now = self.head
            while now.next:
                now = now.next
            now.next = newnode

    def move(self, value):
        if self.head == None:
            print("error")
            return
        elif self.head.value == value:
            self.head = self.head.next
        else:
            now = self.head
            while now.next.value != value:
                now = now.next
            now.next = now.next.next

    def change(self, value, target):
        if self.head == None:
            print("error")
            return
        elif self.head.value == value:
            self.head.value = target
        else:
            now = self.head
            while now:
                if now.value == value:
                    now.value = target
                    return
                now = now.next

    def find(self,value):
        now = self.head
        while now:
            if now.value == value:
                return True
            return False



new_list = my_list()

new_list.add(6)
new_list.add(10)
new_list.add(2)
new_list.print()
new_list.move(2)
new_list.change(10, 20)
new_list.print()

# 上述代码均为测试，保证该程序可正常运行
