# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WangyimusictestItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    singer = scrapy.Field()#歌手
    music = scrapy.Field()#歌曲
    cd = scrapy.Field()
    comments = scrapy.Field()