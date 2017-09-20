#coding=utf-8

import requests

import re

# 登录后的url地址
url = "http://renren.com/923768535"

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

# 通过手动登录之后获取,cookie,即身份认证　
temp = "anonymid=j7afizlgrrdodg; depovince=BJ; jebecookies=a18f1577-1d46-498b-8ea1-c3d583646ce8|||||; _r01_=1; ick_login=acd83d6e-77ca-4f8d-afe0-6914027d2fe4; _de=4F1FF60C280AA48B2CD1201DB4C6DF4A; p=9323a4cef78e11e6a3924f35a17ad8d15; first_login_flag=1; ln_uact=17173805860; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=7d5c090364d57afe2c8859a53c23c01e5; societyguester=7d5c090364d57afe2c8859a53c23c01e5; id=923768535; xnsid=a3aefda2; loginfrom=syshome; JSESSIONID=abcpr10tb2zx5aW1quC5v; ch_id=10016; jebe_key=cfe20cff-bebd-4393-943d-149979137f58%7Ceda913e449d4d8cd6ac80727da63a1fe%7C1504787377045%7C1%7C1504787377094"

# 构建cookies字典, 字典也有类似的字典推导式子
temp_dict = {data.split('=')[0]: data.split('=')[1] for data in temp.split('; ')}

# for data in temp.split('; '):
#     temp_dict[data.split('=')[0]] = data.split('=')[1]

# 发送请求
response = requests.get(url, headers=headers, cookies=temp_dict)

print(re.findall(r'迷途', response.content.decode()))


















