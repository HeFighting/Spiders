#coding=utf-8

import re
import requests

# action中提交的url地址
url = "http://www.renren.com/PLogin.do"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

# 构建账号密码的表单
post_data = {
    'email': '17173805860',
    'password': '1qaz@WSX3edc'
}

# 发送请求返回响应
session = requests.session()
session.post(url, data=post_data, headers=headers)

response = session.get("http://renren.com/923768535")

# 验证是否成功
print(re.findall(r'迷途', response.content.decode()))
print(response.url)























