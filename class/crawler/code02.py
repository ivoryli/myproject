from urllib import request
from urllib import parse

# url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
#
# resp = request.urlopen(url)
# print(resp.read().decode())

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    # 'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
}

# req = request.Request(url,headers=headers)
# resp = request.urlopen(req)
# print(resp.read().decode())


# url = 'https://www.so.com/s?q=%E5%86%85%E6%B6%B5%E6%AE%B5%E5%AD%90&src=srp&fr=se_favorite&psid=eae8861435fbfa0a1bb7a3d4378331f2'
url = "https://blog.csdn.net/m0_37499059/article/details/79003731"

data ={
    'first':'true',
    'pn':1,
    'kd':'python'
}

req = request.Request(url,headers=headers,data = parse.urlencode(data).encode('utf-8'),method='GET')
print(req)
resp = request.urlopen(req)
print(resp.read().decode())
