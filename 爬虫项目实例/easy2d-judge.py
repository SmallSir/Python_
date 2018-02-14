#-*- coding: utf-8 -*-


from selenium import webdriver
import random
import time

judge=['能摸你的J8吗','PHP是世界上最好的语言','刘海波我要给你生猴子','python是世界上最好的语言啦啦啦啦我不管','这个游戏引擎吧，太垃圾拉基辣鸡','引擎好不好，跟开发者颜值有关，于是我觉得这个不行','开发者好厉害刘海波最丑']

for i in range(20):
    driver = webdriver.Chrome()
    url = u'https://www.easy2d.cn/'
    driver.get(url)
    driver.implicitly_wait(10)
    clickElement = driver.find_element_by_id('qadvice')
    clickElement.click()
    writeElement = driver.find_element_by_id('txadvice')
    writeElement.clear()
    writeElement.send_keys(random.choice(judge))
    time.sleep(2)
    sumbitElement = driver.find_element_by_id('submit')
    sumbitElement.click()
    time.sleep(1)
    driver.close()
