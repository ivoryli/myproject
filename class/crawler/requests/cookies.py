import requests

# 请求数据url
member_url = 'https://cr.scutde.net/edu3/edu3/framework/index.html'   #登录后网页

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
}
# session 类 可以自动保存cookies === cookiesJar
session = requests.session()
# 1.代码登录
login_url = 'https://cr.scutde.net:443/edu3/j_spring_security_check'  #提交密码网页
login_form_data = {
    "j_username": "10561181120090153",
    "j_password": "hnlg185411"
}
login_response = session.post(login_url,data=login_form_data,headers=headers)
print(login_response.content.decode())
# 2.登录成功之后 带着 有效的cookies 访问 请求目标数据
data = session.get(member_url,headers=headers).content.decode()

with open('requests-cookie.html','w') as f:
    f.write(data)