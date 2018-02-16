# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlwt
from openpyxl import   Workbook
class WangyimusictestPipeline(object):
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['歌手','歌曲名字','专辑名','评论数'])
    def process_item(self, item, spider):
        line = [item['singer'],item['music'],item['cd'],item['comments']]
        self.ws.append(line)
        self.wb.save(u'D:/python项目/Python_/爬虫项目实例/WangYiMusicTest/WangYiMusicTest/JJ.xlsx')
        return item
