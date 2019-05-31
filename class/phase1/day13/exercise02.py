'''
   输入年月日,返回星期
'''
import time

def get_weekday():
    weeks = ("星期一","星期二","星期三","星期四","星期五","星期六","星期天")
    year = int(input("请输入年份:"))
    month = int(input("请输入月份:"))
    day = int(input("请输入第几天:"))
    #time.strtime根据字符串返回时间元组,字符串格式与后取得元组格式一致,如("%s %s %s"%(x,x,x),%Y %m %d) s与s之间是空格,Y与m之间也要空格
    time_tuple = time.strptime("%d/%d/%d"%(year,month,day),"%Y/%m/%d")
    #时间元组第7个元素是星期
    print(weeks[time_tuple[6]])

get_weekday()