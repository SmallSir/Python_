from selenium import webdriver


driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
driver.implicitly_wait(10)
textElement = driver.find_element_by_id('kw')
textElement.clear()
textElement.send_keys('Python selenium')
submitElement = driver.find_element_by_id('su')
submitElement.click()
resultElements = driver.find_element_by_class_name('c-tools')
len(resultElements)