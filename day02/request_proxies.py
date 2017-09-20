#coding:utf-8

import requests

url = 'http://www.baidu.com/'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'
}

# 构建代理
proxies = {
    "http": "http://182.139.184.239:81",
    "https": "https://182.139.184.239:81"
}

# 发起请求
response = requests.get(url, headers=headers, proxies=proxies)
print(response.content.decode())


