import pymysql

class Login:
    def __init__(self,
                 database = 'stu',
                 host='localhost',
                 user = 'root',
                 passwd='123456',
                 port = 3306,
                 charset='utf8',
                 table = 'user'):
        self.database = database
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port
        self.charset = charset
        self.table = table
        self.connect_db() #　连接数据库

    def connect_db(self):
        self.db = pymysql.connect(host=self.host,
                                  user=self.user,
                                  port = self.port,
                                  database=self.database,
                                  passwd = self.passwd,
                                  charset = self.charset)
        self.cur = self.db.cursor()

    def close(self):
        self.cur.close()
        self.db.close()

    def login(self,name,passwd):
        sql = "select * from %s where name = '%s' and password='%s'"%(self.table,name,passwd)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return True
        else:
            return False


    def register(self,name,passwd):
        sql = "select * from %s \
              where name = '%s';" % \
              (self.table, name)
        self.cur.execute(sql)
        if self.cur.fetchone():
            return False

        sql = "insert into %s (name,password) \
              values ('%s','%s');"%(self.table,name,passwd)

        try:
            self.cur.execute(sql)
            self.db.commit()
        except Exception:
            self.db.rollback()
            return False
        return True


if __name__ == "__main__":
    user = Login()

