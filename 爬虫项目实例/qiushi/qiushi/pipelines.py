# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import urllib
import os

class QiushiPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        fileName = today + 'qiubai.txt'
        imgDir = 'IMG'
        if os.path.isdir(imgDir):
            pass
        else:
            os.mkdir(imgDir)
        with open(fileName,'a') as fp:
            fp.write('-'*50+'\n' + '*'*50 + '\n')
            fp.write("author:\t %s\n" %(item['author']))
            fp.write("content:\t %s\n"%(item['content']))
            try:
                imgURL = item['img'][1]
            except IndexError:
                pass
            else:
                imgName = os.path.basename(imgURL)
                fp.write("img:\t %s\n" %(imgName))
                imgPathName = imgDir + os.sep + imgName
                with open(imgPathName,'wb') as fpi:
                    responese = urllib.urlopen(imgURL)
                    fpi.write(responese.read())
            fp.write("fun: %s\t talk: %s\n" % (item['funNum'],item['talkNum']))
            fp.write('-' * 50 + '\n' + '*' * 50 + '\n'*10)
        return item
