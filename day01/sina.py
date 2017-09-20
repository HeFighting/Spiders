#coding=utf-8

import requests

url = 'http://www.baidu.com/s?'

headers = {
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

params = {'wd': '汇率'}

response = requests.get(url, params=params, headers=headers)

print(response.url)

# print(response.content.decode())

with open('baidu2.html', 'wb') as f:
    f.write(response.content)
