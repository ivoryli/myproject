'''
随机数学加
'''

import random
score = 0
for x in range(10):
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    # print(n1,n2)
    n3 = int(input("%d + %d = ?\n"%(n1,n2)))
    if n3 == n1 + n2:
        score += 10
        print("回答正确！ +10分")
    else:
        score -= 5
        print("回答错误！ -5分")

print(score)