# L = []
# for x in range(65,90):
#     L.append(chr(x))
#     L.append(chr(x + 32))
#
# str1 = "".join(L)
# print(str1)

# d = {'春季':(1,2,3),'夏季':(4,5,6),'秋季':(7,8,9),'冬季':(10,11,12)}
# season = input("请输入季节:")
# print(d[season])

seasons = {
           1:"有1,2,3月",
           2:"有4,5,6月",
           3:"有7,8,9月",
           4:"有10,11,12月",
           }

season = int(input("请输入季节:"))
if season not in seasons:
    print("输入有误")
else:
    value = seasons[season]
    print(value)