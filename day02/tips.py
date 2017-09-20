#coding=utf-8

import requests

# url = 'http://www.baidu.com'
#
# response = requests.get(url)
#
# print(response.cookies)
# print(type(response.cookies))
#
#
# dict_cookie = requests.utils.dict_from_cookiejar(response.cookies)
# print(dict_cookie)
#
# print(type(requests.utils.cookiejar_from_dict(dict_cookie)))
#
#
# ==================================================
url = 'https://www.12306.cn/mormhweb/'
# 设置超时，认证
response = requests.get(url, timeout=3, verify=False)













