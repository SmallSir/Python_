# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import os.path

class WeatherPipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d',time.localtime())
        filename = today + '.txt'
        with open(filename,'a') as fp:
            fp.write(item['cityDate'] + '\t')
            fp.write(item['week'] + '\t')
            fp.write(item['temperature'] + '\t')
            fp.write(item['weather'] + '\t')
            fp.write(item['wind'] + '\t')
            fp.write('\n')
            time.sleep(1)
        return item
