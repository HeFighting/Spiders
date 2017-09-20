from selenium import webdriver

# 创建一个浏览器对象
# driver = webdriver.PhantomJS()
# driver = webdriver.Chrome()

# 加载网页
# driver.get('http://www.baidu.com/')

# 保存页面快照
# driver.save_screenshot('百度.jpg')

# 定位和操作
# driver.find_element_by_id('kw').send_keys('美女')
# driver.find_element_by_xpath('//*[@id="kw"]')
# driver.find_element_by_css_selector('#kw')
# driver.find_element_by_link_text('新闻').click()
# driver.find_element_by_id('su').click()

# 获取一组元素$获取数据
driver1 = webdriver.Chrome()
driver1.get('http://news.baidu.com/')
el_list = driver1.find_elements_by_xpath('//*[@id="pane-news"]/div/ul/li')
for el in el_list:
    print(el.get_attribute('class'))
print(driver1.current_url)
print(driver1.get_cookies())
print(driver1.page_source)

driver1.close()













