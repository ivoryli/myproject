# n = int(input("输入学生人数"))
# stu = []
# for i in range(n):
#     scroe =int(input("第%d个学生成绩是: "%(i + 1)))
#     stu.append(scroe)
#
# for i in range(n):
#     print("第%d个学生成绩是: %d"%(i + 1,stu[i]))
#
# print("学生总成绩是:%d"%sum(stu))
# print("学生最高成绩是:%d"%max(stu))
# print("学生最低成绩是:%d"%min(stu))


#------------------------------------------------------------------------------------------
L = []
while True:
    name = input("请输入第%d学生名字:"%(len(L)+1))
    if name == 'esc':
        break
    if name not in L:
        L.append(name)

for n in L:
    print(n)
