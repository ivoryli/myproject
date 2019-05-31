import pymysql

db = pymysql.connect(host='localhost',user='root',passwd='123456',database='dict')

fd = open('dict.txt')


cur = db.cursor()

while True:
    data = fd.readline()
    if not data:
        break
    word_explain = data.split()
    word = word_explain[0]
    explain = " ".join(word_explain[1:])
    # print(word,explain)
    sql = "insert into word_book(word,explan) value(%s,%s)"
    try:
        cur.execute(sql,[word,explain])
        db.commit()
    except Exception as e:
        db.rollback()
        print("Faild:",e)

fd.close()
cur.close()
db.close()



