'''
栈的链式存储
重点代码
'''

#自定义栈异常
class StackError(Exception):
    pass

#创建结点类
class Node(object):
    def __init__(self,value,next = None):
        self.value = value
        self.next = next
    def __repr__(self):
        return "Node(%s,%s)"%(self.value,self.next)

class LStack:
    def __init__(self):
        # 标记栈顶位置
        self._top = None

    def is_empty(self):
        return self._top is None

    def push(self,elem):
        # node = Node(elem)
        # node.next = self._top
        # self._top = node
        self._top = Node(elem,self._top)

    def pop(self):
        if not self._top:
            raise StackError("stack is empty")
        p = self._top
        self._top = p.next   #头的下个做头
        return p.value

    def top(self):
        if not self._top:
            raise StackError("stack is empty")
        return self._top.value

    def clear(self):
        self._top = None
if __name__ == "__main__":
    st = LStack()
    print(st.is_empty())   #判断是否为空
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())