'''
  取４位整数,计算每位相加
'''

n = int(input("请输入数字"))

#从千位到个位
qian = n // 1000
bai  = n % 1000 // 100
shi  = n % 1000 %100  // 10
ge   = n % 1000 %100 % 10

# 不建议
#从个位到千位            例: 1234
# ge = n %10               1234 ----->  123 余 4
# shi = n // 10 % 10       1234 ----->  123 ---->  12 余3
# bai = n // 100 %10       1234 ----->  12  ---->  1  余2
# qian = n // 1000         1234 ----->  地板除　得 1

print(qian,bai,shi,ge)
print("4位数相加=:",qian + bai + shi + ge)