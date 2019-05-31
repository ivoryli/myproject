'''
 输入多个字符串,按q退出,显示不重复的字符串
'''

# s01 = set()
# while True:
#     n = input("请输入字符串:")
#     if n == 'q':
#         break
#     s01.add(n)
#
# for x in s01:
#     print(x)


'''
   经理:['曹操','刘备','孙权']
   技术员:['曹操','刘备','关羽','张飞']
   是经理也是技术员的有谁
   是经理，但不是技术员的有谁
   是技术员但不是经理的有谁
   张飞是经理吗
   只有一个职位的有谁
   经理和技术员共有多少人
'''

list_manager = ['曹操','刘备','孙权']
list_technician = ['曹操','刘备','关羽','张飞']

#建议用frozenset
sm = frozenset(list_manager)
st = frozenset(list_technician)
print("是经理也是技术员的是:",sm & st)
print("是经理，但不是技术员的有:",sm - st)
print("是技术员但不是经理的有:",st - sm)
print("张飞是经理吗:","张飞" in sm)
print("只有一个职位的有谁",sm ^ st)
print("经理和技术员共有",sm | st)

