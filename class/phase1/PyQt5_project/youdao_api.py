import json

import requests

def api(key):
    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 UBrowser/6.2.4098.3 Safari/537.36 X-Requested-With:XMLHttpRequest"}
    data = {"i":key,
    "from":"AUTO",
    "to":"AUTO",
    "smartresult":"dict",
    "client":"fanyideskweb",
    "salt":"15561928032574",
    "sign":"793b360f281f99e4e71e926d5a760481",
    "ts":"1556192803257",
    "bv":"5b00dec16aaca6420a32f369eb955b1f",
    "doctype":"json",
    "version":"2.1",
    "keyfrom":"fanyi.web",
    "action":"FY_BY_REALTlME"}

    response = requests.post(url,data,headers)
    response_data = response.text
    #{'elapsedTime': 1, 'type': 'ZH_CN2EN', 'translateResult': [[{'src': '哦哇', 'tgt': 'Oh wow!'}]], 'errorCode': 0} <class 'dict'>
    result = json.loads(response_data)
    print(result,type(result))
    tgt = result["translateResult"][0][0]['tgt']
    return tgt
# print(tgt)