from phase2.Data.day02.sstack import SStack

#此方法不用栈，用列表就可以!!!!!!

#知道说有括号对应的值
# print("(:",ord("("))
# print("):",ord(")"))
# print("{",ord("{"))
# print("}",ord("}"))
# print("[",ord("["))
# print("]",ord("]"))
#
st = SStack()
#
# s = "a{s(d[fa])s}df"
# for item in s:
#     if ord(item) in (40, 41, 123, 125, 91, 93):
#         if ord(item) == 40:
#             st.push(39)
#         else:
#             st.push(ord(item))
# L = []
# while not st.is_empty():
#     L.append(st.pop())
#
# if len(L) % 2 == 1:
#     print("不对称")
#
# for x in range(len(L)):
#     if L[x] in (39, 123, 91):
#         L[x] += 2
# print(L)
# if L == L[::-1]:
#     print("是")

#--------------------------------------------------------------------------------------------------

s = "a{sd([fa])s}df"
for item in s:
    if ord(item) in (40,123,91):
        if ord(item) == 40:
            st.push(39)
        else:
            st.push(ord(item))

    if ord(item) in (41,125,93):
        tmp = ord(item) - 2
        e = st.pop()
        if e != tmp:
            print("不匹配")
            break
else:
    print("匹配")
