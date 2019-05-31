'''
链式队列
重点代码
'''

#队列异常
class QueueError(Exception):
    pass

#创建结点类
class Node(object):
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
    def __repr__(self):
        return "Node(%s,%s)"%(self.value,self.next)

class LQueue:
    def __init__(self):
        self.front = self.rear = Node(None)

    def is_empty(self):
        # return self.front is self.rear
        return self.front == self.rear

    #入队
    def enqueue(self,elem):
        self.rear.next = Node(elem)
        self.rear = self.rear.next

    #出队
    def dequeue(self):
        if self.is_empty():
            raise QueueError("Queue is empty")
        self.front = self.front.next
        return self.front.value

    def clear(self):
        self.front = self.rear

if __name__ == "__main__":
    lq = LQueue()
    print(lq.is_empty())
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    while not lq.is_empty():
        print(lq.dequeue())
