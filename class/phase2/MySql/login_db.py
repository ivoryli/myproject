import pymysql

class DBoperation:
    def __init__(self,host,user,passwd,database,charset='utf8'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset

    # 创建连接
    def connect(self):
        self.db = pymysql.connect(host = self.host,
                             user = self.user,
                             passwd = self.passwd,
                             database = self.database,
                             charset = self.charset
                            )
        self.cur = self.db.cursor()

    def select(self,name):
        sql = "select name,password from user where name='%s'"%name
        try:
            self.cur.execute(sql)
        except Exception:
            result = None                   #查询语言出错返回None
            self.db.rollback()
        else:
            result = self.cur.fetchone()    #查询成功,取值
            if result:                      #longin调用,首创时为空
                result = result[1]          #取出password
        return result

    def login(self,name,password):
        if self.select(name):               #判断注册时有没有重名
            return False
        try:
            sql = "insert into user(name,password) value('%s','%s')"%(name,password)
            self.cur.execute(sql)
            self.db.commit()
            return True
        except Exception:
            return False
            self.db.rollback()

    def close(self):
        self.cur.close()
        self.db.close()

user = DBoperation('localhost','root','123456','stu','utf8')
user.connect()
while True:
    print('''
    1.用户注册
    2.用户登录
    ''')
    op = int(input("请选择:"))
    if op == 1:
        name = input("Name:")
        password = input("password:")
        if user.login(name,password):
            print("%s注册成功"%name)
        else:
            print("用户名已存在")
    if op == 2:
        name = input("Name:")
        password = input("password:")
        usr_password = user.select(name)  #返回str类型
        if usr_password == password:
            print("登录成功")
        else:
            print("登录失败")

user.close()