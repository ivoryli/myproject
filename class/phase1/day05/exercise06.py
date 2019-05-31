L =[]
while True:
    name = input("请输入姓名:")
    if not name:
        break
    age = int(input("请输入年龄:"))
    score = int(input("请输入成绩:"))
    d = {}
    d['name'] = name
    d['age'] = age
    d['score'] = score
    L.append(d)

for dict_stu in L:
    for key,value in dict_stu.items():
        # print("%s同学年龄是%d,成绩:%d"%())
        print('%s---->%s'%(key,value))