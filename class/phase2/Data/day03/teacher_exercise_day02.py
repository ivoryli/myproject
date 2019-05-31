'''
逆波兰表达式
'''

from phase2.Data.day02.lstack import *

st = LStack()

while True:
    exp = input("dc:")
    tmp = exp.split(" ")
    st.clear()
    for i in tmp:
        if i == 'p':
            break
        if i not in ['+','-']:
            st.push(float(i))

        elif i == '+':
            y = st.pop()
            x = st.pop()
            st.push(x + y)

        elif i == '-':
            y = st.pop()
            x = st.pop()
            st.push(x - y)
    print("结果:",st.pop())