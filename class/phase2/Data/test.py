class Node:
    def __init__(self,value,next = None):
        self.value = value
        self.next = next

class LinkList:
    def __init__(self):
        self.head = Node(None)

    def init_list(self,date):
        p = self.head
        for item in date:
            p.next = Node(item)
            p = p.next

    def show(self):
        p = self.head.next
        while p:
            print(p.value,end = ' ')
            p = p.next

    def get_length(self):
        count = 0
        p = self.head.next
        while p:
            count += 1
            p = p.next
        return count

    def is_emety(self):
        return self.get_length() == 0

    def clear(self):
        self.head = Node(None)

    def append(self,item):
        p = self.head
        while p.next:
            p = p.next
        p.next = Node(item)

    def delete(self,target):
        p = self.head
        while not p.next.value == target:
            p = p.next
        p.next = p.next.next

    def insert_for_index(self,index,target):
        if index < 0 or index > self.get_length():
            raise IndexError("list index out of range")
        count = 0
        p = self.head
        while not count == index:
            count += 1
            p = p.next
        tmp = p.next
        p.next = Node(target,tmp)

    def get_item(self,index):
        if index < 0 or index > self.get_length() - 1:
            raise IndexError("list index out of range")
        count = 0
        p = self.head.next
        while not count == index:
            count += 1
            p = p.next
        return p.value

if __name__ == "__main__":
    link = LinkList()
    L = [1,2,3,4,5,6]
    print(link.is_emety())
    link.init_list(L)
    link.append(7)
    print(link.get_length())
    link.delete(2)
    link.insert_for_index(6,2)
    print(link.get_item(6))
    link.show()