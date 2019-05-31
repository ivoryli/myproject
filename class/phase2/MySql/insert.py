'''
插入练习
'''
import pymysql

#创建连接
db = pymysql.connect(host='localhost',user='root',passwd='123456',database='stu',charset='utf8')

# 创建游标
cur = db.cursor()

while True:
    name = input("Name:")
    age = int(input("Age:"))
    gender = input("m or w:")
    score = float(input("Score:"))
    # sql = "insert into myclass(name,age,gender,score) values(%s,%s,%s,%s);"  #方法2
    sql = "insert into myclass(name,age,gender,score) values('%s',%s,'%s',%f);"%(name,age,gender,score)   #方法1
    try:
        #列表中元素全是字符串，执行语句，自动识别类型
        # cur.execute(sql,[name,age,gender,score])  #方法2
        cur.execute(sql)   #方法1
        db.commit()
    except Exception as e:
        db.rollback()   #失败回滚到操作之前的状态
        print("Faild:",e)

cur.close()
db.close()
