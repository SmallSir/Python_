#-*- coding: utf-8 -*-

from mylog import MyLog as mylog
import time
import os
from selenium import webdriver


class GetCartoon(object):
    def __init__(self):
        self.startUrl = u'http://www.1kkk.com/ch1-117459/'
        self.log = mylog()
        self.browser = self.getBrowser()
        self.saveCartoon(self.browser)

    def getBrowser(self):
        brower = webdriver.Chrome()
        try:
            brower.get(self.startUrl)
        except:
            mylog.error('open %s failed'%self.startUrl)
        brower.implicitly_wait(30)
        return brower

    def saveCartoon(self,browser):
        cartoonTitle = browser.title.split('_')[0]
        self.createDir(cartoonTitle)
        os.chdir(cartoonTitle)
        sumPage = int(browser.find_element_by_xpath('//div[@class="chapterpager"]/a[8]').text)
        i = 1
        while i <= sumPage:
            imgName = str(i) + '.png'
            img = browser.find_element_by_id('cp_img')
            browser.get_screenshot_as_file(imgName)
            self.log.info('save img %s'%imgName)
            i += 1
            NextTag = browser.find_elements_by_class_name('block')[2]
            NextTag.click()
            time.sleep(2)
        self.log.info('save img success')
    def createDir(self,dirName):
        if os.path.exists(dirName):
            self.log.error('create directory %s failed, have a same name file or directory' %dirName)
        else:
            try:
                os.makedirs(dirName)
            except:
                self.log.error('create directory %s failed' %dirName)
            else:
                self.log.info('create directory %s success' %dirName)
if __name__ == '__main__':
    GC = GetCartoon()