'''
 ord()字变数
 chr()数变字
'''

n = input("输入字符串")

for code in n:
    print(ord(code))

while True:
    n = int(input("输入数字: "))
    if n < 0:
        break
    print(chr(n))