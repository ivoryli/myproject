'''
累加1-100之间能被3整除的数的和
'''

sum = 0

for i in range(1,101):
    if not i % 3:
        sum += i

print(sum)