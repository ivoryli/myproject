from urllib import request
from urllib import parse

#获取网页对象
# resp = request.urlopen('http://www.baidu.com')
# print(resp.read().decode())

#下载网页
# request.urlretrieve('http://ww.baidu.com/','baidu.html')

url = 'http://www.baidu.com/s'
params = {'wd':'刘德华'}
qs = parse.urlencode(params)
print(qs)
# url = url + '?' + qs
# print(url)
# resp = request.urlopen(url)
# print(resp.read().decode())

# params = {'name':'张三','age':10,'greet':'hello world'}
# qs = parse.urlencode(params)
# # print(qs)
# result = parse.parse_qs(qs)
# print(result)
