# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time


class Meiju100Pipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        fileName = today + 'meiju.txt'
        with open(fileName,'a') as fp:
            fp.write("%s \t" %item['storyName'])
            #fp.write("%s \t" %item['storyState'])
            fp.write("%s \t" %item['storyLX'])
            if len(item['tvStation']) == 0:
                fp.write("unknow \n")
            else:
                fp.write("%s \n" % item['tvStation'])
            #fp.write("%s \n" % item['updateTime'])
        return item
