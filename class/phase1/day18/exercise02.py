'''
   装饰器练习
'''

def check_id(func):
    def wrapper(*args,**kwargs):
        print("验证账户")

        return func(*args,**kwargs)
    return wrapper

@check_id
def deposit(money):
    print("存款:",money)

@check_id
def withdraw():
    print("取钱:")
    return 100000

deposit(1000000)
print(withdraw())