import re
import requests
import chardet

# 1.请求url
url = 'http://news.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}

free_proxy = {'http': '122.234.207.140:9000'}

# response = requests.get(url=url, headers=headers, proxies=free_proxy)
response = requests.get(url=url, headers=headers)
data = response.content.decode("utf-8")

patten = re.compile('<a href="(\S*)" .*>(.*)</a>')
result = patten.findall(data)
url = result[7][0]
print(url)
response = requests.get(url=url,headers=headers)
data = response.content.decode("GB2312",'ignore')
# data = response.content
# data = chardet.detect(data)
# print(data)

with open("proxy.html","w",encoding='GB2312') as f:
    f.write(data)