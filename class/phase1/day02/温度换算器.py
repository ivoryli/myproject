'''
温度换算器(华氏度,摄氏度,开氏度)
摄氏度 = (华氏度 - 32) / 1.8
华氏度 = 摄氏度 * 1.8 + 32
开氏度 = 摄氏度 + 273.15

获取华,得摄氏度
获取摄氏度,得华氏度
获取摄氏度,得开氏度

华氏度 fahrenheit
摄氏度 centigrade
'''

fahrenheit = float(input("华氏度"))
print("摄氏度:",(fahrenheit -32)/1.8)


centigrade = float(input("摄氏度"))
print("华氏度:",centigrade * 1.8 +32)


centigrade = float(input("摄氏度"))
print("开氏度:",centigrade + 273.15)

