'''
   整数相加
'''

def add(*args):
    total = 0
    for i in args:
        total += i
    return total

print(add(1,2,3,4,5))