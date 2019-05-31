import requests

# 请求数据url
member_url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=python'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
#  cookies 的字符串
cookies = 'JSESSIONID=593C0A3E1C6C74F528935FC8A506AB45; UM_distinctid=16aafaf07ab8b5-06f023eeb65a2e-2b6f686a-1fa400-16aafaf07ac5d9; CNZZDATA1000212028=593322813-1557723260-https%253A%252F%252Fcr.scutde.net%252F%7C1559046802'

# 需要的是 字典类型
cook_dict = {}
cookies_list = cookies.split('; ')
for cookie in cookies_list:
    cook_dict[cookie.split('=')[0]] = cookie.split('=')[1]


# 字典推导式
cook_dict = {cookie.split('=')[0]:cookie.split('=')[1] for cookie in cookies.split('; ')}

response = requests.get(member_url, headers=headers, cookies=cook_dict)

data = response.content.decode()

with open('05-cookie.html','w') as f:
    f.write(data)