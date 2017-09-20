#coding=utf-8

from selenium import webdriver

# 创建一个浏览器对象
driver = webdriver.Chrome()

# 跳转到登陆页面
driver.get('https://qzone.qq.com/')

# 获取框架节点,进入到框架当中
el_frame = driver.find_element_by_xpath('//*[@id="login_frame"]')
driver.switch_to_frame(el_frame)

# 获取点击密码登陆的元素
el = driver.find_element_by_xpath('//*[@id="switcher_plogin"]')

# 模拟点击
el.click()

# 输入账号密码
driver.find_element_by_xpath('//*[@id="u"]').send_keys('1191820896')
driver.find_element_by_xpath('//*[@id="p"]').send_keys('qwas12')

# 登录
el_su = driver.find_element_by_xpath('//*[@id="login_button"]').click()













