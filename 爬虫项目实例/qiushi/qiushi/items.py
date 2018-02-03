# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QiushiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()#作者信息
    content = scrapy.Field()#笑话内容
    img = scrapy.Field()#笑话图片
    funNum = scrapy.Field()#单击好笑次数
    talkNum = scrapy.Field()#评论数量

