'''
顺序队列
重点代码
'''

#队列异常
class QueueError(Exception):
    pass

class SQueue:
    def __init__(self):
        self._elems = []

    def enqueue(self, value):
        self._elems.append(value)

    def dequeue(self):
        if not self._elems:
            raise QueueError()
        return self._elems.pop(0)

    def clear(self):
        self._elems = []

    def is_empty(self):
        return self._elems == []

    def top(self):
        return self._elems[0]

if __name__ =="__main__":
    sq = SQueue()
    print(sq.is_empty())
    sq.enqueue(10)
    sq.enqueue(20)
    while not sq.is_empty():
        print(sq.dequeue())