"""
练习：
    １．创建一个数据表为user
    ２．编写程序完成如下功能
        *注册：从终端输入用户名和密码，将用户名密码存入数据库中，用户名不能重复
        *登录：从终端输入用户名和密码，如果该用户存在则登陆成功，不存在则得到登录失败
    ３．将数据库操作功能封装为类

"""
from login import Login
user=Login()

def do_login():
    name = input("User: ")
    passwd = input("Passwd: ")
    return user.login(name,passwd)

def do_register():
    name = input("User: ")
    passwd = input("Passwd: ")
    return user.register(name,passwd)


while True:
    print("=====================")
    print("**     login     ***")
    print("**    register   ***")
    print("=====================")

    cmd = input("Cmd:")
    if cmd == 'login':
        if do_login():
            print("登录成功")
        else:
            print("登录失败")
        break
    elif cmd == 'register':
        if do_register():
            print("注册成功")
        else:
            print("注册失败")
        break
    else:
        print("重新输入")

user.close()


# import pymysql
# def do_login():
# #链接数据库
#     db=pymysql.connect(host="localhost",
#                    port=3306,user="root",
#                    password="123456",
#                    database="stu",
#                    charset="utf8")
#
# #获取游标
# # while True:
# #     cur=db.cursor()
# #     user_name=input("请输入用户名：")
# #     password=input("请输入密码：")
# #     try:
# #         sql="insert into user(user_name,password) VALUES (%s,%s);"
# #         cur.execute(sql,[user_name,password])
# #         db.commit()
# #     except Exception as e:
# #         db.rollback()
# #         print(e)
# #
# # cur.close()
# # db.close()
#
#
#
#     cur = db.cursor()
#     name = input("请输入用户名：")
#     password=input("请输入密码：")
#     sql="select * from user where user_name=%s and password=%s;"
#     try:
#         cur.execute(sql, [name,password])
#         db.commit()
#         print("登陆成功")
#     except Exception as e:
#         db.rollback()  # 失败回滚到操作之前的状态
#         print("Faild:", e)
#
#
#     cur.close()
#     db.close()
# if __name__=="__main__":
#     do_login()