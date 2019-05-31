'''
按一斤16两,输入两,输出几斤几两
'''

n = int(input("输入两数："))
chopper = n //16
liang = n % 16
print(str(chopper) + "斤" + str(liang) + "两")