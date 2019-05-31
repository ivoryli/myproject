'''
球从100米落下,每次弹回一半,最小弹起高度0.01m,一共多少次,一共多少米
'''

hight = 100
count = 0
sum = 0
#直接用hight代表当前高度
#弹起来的高度是 hight / 2
while hight / 2 >= 0.01:
    sum += hight
    count += 1
    hight /= 2
    sum += hight


print("一共%d次,一共走了%f米"%(count,round(sum,2)))