'''
二叉树的构建与遍历
重点代码
'''

from phase2.Data.day03.squeue import *

class TreeNode:
    def __init__(self,data = None,left = None,right = None):
        self.data = data
        self.left =left
        self.right = right

    def __str__(self):
        return "TreeNode(%s(%s,%s))"%(self.data,self.left,self.right)

#二叉树类，进行遍历
class Bitree:
    def __init__(self,root = None):
        self.root = root

    def is_empty(self):
        if not self.root:
            return True
        else:
            return False

    #先根
    def perOrder(self,node):
        if node is None:
            return
        print(node.data,end = " ")
        self.perOrder(node.left)
        self.perOrder(node.right)

    # 中根
    def inOrder(self,node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data,end = ' ')
        self.inOrder(node.right)

    # 后根
    def postOrder(self,node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data,end = ' ')

    # 层次遍历
    def levelOrder(self,node):
        sq = SQueue()
        sq.enqueue(node)
        while not sq.is_empty():
            tmp = sq.dequeue()
            print(tmp.data,end = ' ')
            if tmp.left:
                sq.enqueue(tmp.left)
            if tmp.right:
                sq.enqueue(tmp.right)

if __name__ == "__main__":
    #F:\达内\phase2\吕泽\授课资料\数据结构\bitree1.png
    # 按照后序遍历增加结点
    b = TreeNode('B')
    f = TreeNode('F')
    g = TreeNode('G')
    d = TreeNode('D', f, g)
    i = TreeNode('I')
    h = TreeNode('H')
    e = TreeNode('E', i, h)
    c = TreeNode('C', d, e)
    a = TreeNode("A", b, c)

    bt = Bitree(a)   #初始化树对象，传入根结点
    print("pre order ...")
    bt.perOrder(bt.root)
    print()
    bt.inOrder(bt.root)
    print()
    bt.postOrder(bt.root)
    print()
    bt.levelOrder(bt.root)
