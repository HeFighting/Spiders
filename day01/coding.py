#coding=utf-8

import requests

response = requests.get('http://www.baidu.com')

print(response.url)
print("==========================")
# 修改编码方式，只用于response.text的内容，因为其格式为str
response.encoding = 'utf-8'

# 获取str类型的响应
print(response.text)
print("==========================")
# 获取byte类型的响应
print(response.content.decode())
print("==========================")
# 获取状态码
print(response.status_code)
print("==========================")
# 获取请求头
print(response.request.headers)
print("==========================")
# 获取响应头
print(response.headers)

