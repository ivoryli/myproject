'''
   练习：使用装饰器实现：
   　　　为两个已有功能（进入后台，删除订单）,增加新功能（验证权限）
'''

def verify_permission(func):
    def wrapper(*args,**kwargs):
        print("进行权限验证")
        return func(*args,**kwargs)
    return wrapper

@verify_permission
def enter_background(login_id,pwd):
    print(login_id,pwd)
    print("进入后台系统....")

@verify_permission
def delete_order(order_id):
    print("删除%d订单..."%order_id)

enter_background("zs",123)
delete_order(12)
