#coding=utf-8

import requests

# 1.url
url = 'http://www.baidu.com'

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

response = requests.get(url, headers)

print(response.content.decode())

