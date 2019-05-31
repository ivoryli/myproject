'''
在控制台中获取一个商品单价
　　　　　再获取一个商品数量
　　　　　再获取一个金额
　　　计算应该找回多少钱

'''

price = float(input("请输入单价:"))
num = int(input("请输入数量:"))
m = int(input("请输入金额:"))

total_mon = float(price * num)

if total_mon >= 100:
    total_mon *= 0.8

residue = m - total_mon

if residue < 0:
    residue = abs(residue)
    print("还缺",residue,"块钱")
else:
    print("找零:",residue,"块钱")

