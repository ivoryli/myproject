'''
学数据库练习
增删改
'''

import pymysql

#创建连接
db = pymysql.connect(host='localhost',user='root',passwd='123456',database='stu',charset='utf8')

# 创建游标
cur = db.cursor()

try:
    #插入操作
    sql = "insert into interest value(7,'Bob','draw,sing','B',6852,'凑合吧');"
    cur.execute(sql)

    # 修改操作
    sql = "update interest set price=6666 where name = 'Bob';"
    cur.execute(sql)

    # 删除操作
    sql = "delete from myclass where score = 0;"
    cur.execute(sql)

    db.commit()

except Exception as e:
    db.rollback()
    print("Faild:",e)

cur.close()
db.close()