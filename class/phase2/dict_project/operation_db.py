'''
dict项目用于处理数据   Bob 123456
'''

import pymysql
import hashlib
import time
#编写功能类 提供给服务端使用
class Database:
    def __init__(self,host = 'localhost',
                      port = 3306,
                      user = 'root',
                      passwd = '123456',
                      database = 'dict'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.connect_db()

    def connect_db(self):
        self.db = pymysql.connect(host = self.host,
                                  port = self.port,
                                  user = self.user,
                                  passwd = self.passwd,
                                  database = self.database)

    def create_cursor(self):         #每个子进程开不同的游标
        self.cur = self.db.cursor()

    # 处理注册
    def register(self,name,passwd):
        sql = 'select * from user where name = "%s"'%name
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if r:
            return False

        #加密处理
        hash = hashlib.md5((name + "ivory").encode())
        hash.update(passwd.encode())

        sql = "insert into user(name,passwd) value(%s,%s)"
        try:
            self.cur.execute(sql,[name,hash.hexdigest()])
            self.db.commit()
            return True
        except Exception:
            self.db.rollback()
            return False

    # 处理登录   myself bug:同名情况不确定
    def login(self,name,passwd):
        sql = 'select * from user where name = "%s"' % name
        self.cur.execute(sql)
        r = self.cur.fetchone()
        if not r:
            return False

        hash = hashlib.md5((name + "ivory").encode())
        hash.update(passwd.encode())

        if hash.hexdigest() != r[2]:
            return False
        else:
            return True

    #插入历史记录
    def insert_history(self,name,word):
        tm = time.ctime()
        sql = "insert into history(name,word,time) value(%s,%s,%s)"
        try:
            self.cur.execute(sql,[name,word,tm])
            self.db.commit()
        except Exception:
            self.db.rollback()

    #单词查询
    def query(self,word):
        sql = "select explan from word_book where word = '%s'"%word
        self.cur.execute(sql)
        explan = self.cur.fetchone()
        if explan:
            return explan[0]
        else:
            return None

    #查询历史记录
    def query_history(self,name):
        #order by 取最新的
        sql = "select name,word,time from history where name = '%s' order by id desc limit 10"%name
        self.cur.execute(sql)
        # history = self.cur.fetchall()
        # if history:
        #     return history
        # else:
        #     return None
        return self.cur.fetchall()

    #关闭数据库
    def close(self):
        self.cur.close()      #每个子进程都有自己的空间
        self.db.close()

if __name__ == '__main__':
    user = Database()
    # user.create_cursor()
    # user.close()