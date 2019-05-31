'''
逆波兰表达式   myself bug: 1 2 3 + p == 6
'''

from phase2.Data.day02.lstack import *

st1 = input("请输入逆波兰表达式:")
st = LStack()
L = st1.split(" ")   #split return list()
# print(L)

def reverse_polish(L):
    total_num = 0
    for item in L:
        if ord(item[-1]) in tuple(range(48,58)):
            item = int(item)
            st.push(item)
        elif item == '+':
            while not st.is_empty():
                total_num += st.pop()
        elif item == '-':
            while not st.is_empty():
                total_num -= st.pop()
                if not st.is_empty():
                    total_num += st.pop()
        elif item == 'p':
            return total_num

print(reverse_polish(L))