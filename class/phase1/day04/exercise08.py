'''
  3.一注彩票７个球
  　　前6个红色 : 1-33之间,不能重复
      最后一个篮球: 1-16 之间
    (1)  购买彩票
    (2)  随机产生一注彩票
    random.randint(1,100)
'''

import random

'''
L_input = []
L_random = []
count = 1
while True:
    n = int(input("第%d个号码是(1-33之间):"%count))
    if n < 1 or n >33 or (count == 7 and n > 16) or n in L_input:
        continue
    L_input.append(n)
    count += 1
    if count == 8:
        break

for item in range(7):
    print("自选的第%d个号码是:%d"%(item + 1,L_input[item]))

count = 1
while True:
    n = random.randint(1,34)
    if count == 7 and n > 16 or n in L_random:
        continue
    L_random.append(n)
    count += 1
    if count == 8:
        break

for item in range(7):
    print("机选的第%d个号码是:%d"%(item + 1,L_random[item]))
'''

#T版篮球可重复
ticket = []
#前6个红球
while len(ticket) < 6:
    number = int(input("请输入第%d个红球号码:"%(len(ticket) + 1)))
    if number < 1 or number > 33:
        print("不在范围内")
    elif number in ticket:
        print("该号码已经存在")
    else:
        ticket.append(number)

#篮球
while True:
    number = int(input("请输入蓝球号码:" ))
    if 1 <= number <= 16:
        ticket.append(number)
        break
    else:
        print("不在范围内")

for item in ticket:
    print(item)


#机选
ticket_random = []
while len(ticket_random) < 6:
    number = random.randint(1,33)
    if number not in ticket_random:
        ticket_random.append(number)

# ticket_random.sort()

ticket_random.append(random.randint(1,16))

# 列表范围排序
temp = ticket_random[:6]
temp.sort()
ticket_random[:6] = temp

print(ticket_random)