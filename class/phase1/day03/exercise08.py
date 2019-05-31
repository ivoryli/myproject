'''
输入一个数,判断是否是素数:只能被1和自身整除称为素数
'''

n = int(input("输入一个数"))

if n < 2:
    print("不是素数")
else:
    for i in range(2,n):
        if n % i == 0:
            print("能被%d整除"%i)
            print("不是素数")
            break
    else:
        print("是素数")