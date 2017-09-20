from selenium import webdriver

driver = webdriver.Chrome()

driver.get('http://bj.58.com/')

el = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[1]/div[1]/h2/a')

el.click()

print(driver.current_url)

# 获取所有的窗口列表
url_list = driver.window_handles
print(url_list)

# 切换到选定的窗口
driver.switch_to_window(url_list[1])

print(driver.current_url)

# driver.close()

