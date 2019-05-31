'''
单链表学习程序
重点程序
'''

#创建结点类
class Node(object):
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
    def __repr__(self):
        return "Node(%s,%s)"%(self.value,self.next)

#链表的操作
class LinkList(object):
    def __init__(self):
        # self.head = None
        self.head = Node(None)  # 链表的开头

    def init_list(self,data):
        p = self.head   # 可移动变量ｐ
        for i in data:
            p.next = Node(i)
            # print(p.next)
            p = p.next

    def show(self):
        p = self.head.next
        # print(p)  #Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,None))))))
        while p:
            print(p.value,end = ' ')
            p = p.next
        print()

    #myself usable
    # def append(self,value):
    #     p = self.head.next
    #     while True:
    #         if not p.next:
    #             p.next = Node(value)
    #             break
    #         p = p.next

    #teacher
    def append(self,item):
        p = self.head
        while p.next:
            p = p.next
        p.next = Node(item)

    def insert(self,target,value):
        p = self.head
        while True:
            # print(p.next)
            if p.value == target:
                tmp = p.next
                p.next = Node(value,tmp)
                break
            p = p.next

    #myself unusable
    # def insert_for_index(self,index,value):
        # if self.get_length() < index:
        #     raise IndexError()
        # count = 0
        # p = self.head   #Node(None,1)
        # while p.next:
        #     if index == count:
        #         tmp = p.next
        #         p.next = Node(value,tmp)
        #         break
        #     count += 1
        #     p = p.next

    #teacher
    def insert_for_index(self, index, value):
        if index < 0 or index > self.get_length():
            raise IndexError("list index out of range")
        p = self.head
        count = 0
        while  count < index:
            p = p.next
            count += 1
        node = Node(value)
        node.next = p.next
        p.next = node

    #获取索引对应的值&teacher
    def get_item(self,index):
        p = self.head.next
        count = 0
        # 没有到对应索引号并且遍历索引没有到最后就循环
        while count < index and p:
            count += 1
            p = p.next
        # 如果因为p到最后了则说明越界
        if  not p:
            raise IndexError("list index out of range")
        # i 不小于 index说明找到索引结点了
        else:
            return p.value

    def delete(self,value):
        p = self.head
        while p.next:
            if p.next.value == value:
                p.next = p.next.next
                break
            p = p.next
        else:
            raise ValueError("x not in list")

    #获取节点个数
    def get_length(self):
        count = 0
        p = self.head
        while p.next:
            count += 1
            p = p.next
        return count

    #判断链表是否为空
    def is_empty(self):
        if self.get_length() == 0:
            return True
        else:
            return False

    #清空链表
    def clear(self):
        self.head.next = None

    #myself bug:next = int,无法找到下一个对象，无法靠属性找对象
    # def init_list(self,l):
    #     for item in range(len(l) - 1):
    #         if item == 0:
    #             self.head = Node(None,l[item])
    #             continue
    #         Node(l[item],l[item + 1])
    #         if item == len(l) - 1:
    #             Node(l[item + 1])

if __name__ == "__main__":
    #创建链表对象
    link = LinkList()
    print(link.is_empty())
    # 　初始数据
    l = [1,2,3,4,5,6]
    link.init_list(l)# 将初始数据插入链表
    # print(link.head)  #Node(None,Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,None)))))))
    link.append(7)
    # link.insert(None,0)     #按值的位置插入数据
    link.insert_for_index(6,9)#按索引位置插入数据
    link.show()  # 遍历链表
    # print(link.get_length())   #获取节点个数
    link.delete(3)
    link.show()  # 遍历链表
    # print(link.get_item(6))

