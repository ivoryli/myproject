from urllib import parse

url = 'https://www.bilibili.com/video/av37581145/s;adf?p=6'  #虚拟url

result = parse.urlparse(url)
# result = parse.urlsplit(url)  #少了个 params 属性 就是;到？之间的   adf
print('scheme',result)
print('scheme',result.scheme)