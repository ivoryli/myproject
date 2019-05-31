import urllib.request

def create_proxy_handler():
    proxy = {
        "http":"http://176.122.17.158:8000"
    }
    url = "https://new.qq.com/ch/ent/"
    # url = 'https://blog.csdn.net/m0_37499059/article/details/79003731'     #decode()错误
    # urllib.request.urlopen()

    handler = urllib.request.ProxyHandler(proxy)

    opener = urllib.request.build_opener(handler)

    response = opener.open(url)

    data = response.read()
    data = data.decode()
    print(data)

create_proxy_handler()

# url = "https://www.so.com/s?q=%E5%86%85%E6%B6%B5%E6%AE%B5%E5%AD%90&src=srp&fr=se_favorite&psid=eae8861435fbfa0a1bb7a3d4378331f2"
#
# response = urllib.request.urlopen(url)
# data = response.read().decode()
# print(data)