'''
二进制文件存储
'''

import pymysql

#创建连接
db = pymysql.connect(host='localhost',user='root',passwd='123456',database='stu',charset='utf8')

# 创建游标
cur = db.cursor()

#文件存储

# with open('tree.jpg','rb') as fd:
#     data = fd.read()
#
# try:
#     sql = "insert into Image value(1,'tree.jpg',%s);"
#     cur.execute(sql,[data])
#     db.commit()
# except Exception as e:
#     db.rollback()
#     print(e)


#获取文件
sql = "select * from Image where filename = 'tree.jpg'"

cur.execute(sql)
# image = cur.fetchall()
# with open(image[0][1],"wb") as fd:
#     fd.write(image[0][2])
image = cur.fetchone()
with open(image[1],"wb") as fd:
    fd.write(image[2])

cur.close()
db.close()