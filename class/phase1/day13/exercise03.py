'''
   输入出生日期,计算出生多少天
'''
import time
def get_day(year,month,day):

    #lockaltime 参数:秒   返回:时间元组  time.struct_time(tm_year=2019, tm_mon=4, tm_mday=18, tm_hour=19, tm_min=32, tm_sec=58, tm_wday=3, tm_yday=108, tm_isdst=0)
    # print(time.localtime(time.time()))

    #UTC只是比北京时间提前了8个小时 time.mktime((1970, 1, 1, 8, 0, 0, 1, 1, 0) = 0
    # print(time.mktime((1970, 1, 1, 8, 0, 0, 1, 1, 0)))
    # mktime参数:元组  返回:utc秒数
    #获取生日当天秒数
    briday_second = time.mktime(time.strptime("%d %d %d"%(year,month,day),"%Y %m %d"))

    # print(second)
    total_second = time.time() - briday_second
    # total_day = total_second / 60 / 60 // 24
    # total_year = total_day // 365
    print(total_second)

get_day(1970,1,1)