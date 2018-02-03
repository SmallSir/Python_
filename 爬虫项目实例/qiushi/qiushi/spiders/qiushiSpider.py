# -*- coding: utf-8 -*-
import scrapy


class QiushispiderSpider(scrapy.Spider):
    name = 'qiushiSpider'
    allowed_domains = ['https://www.qiushibaike.com/']
    start_urls = ['https://www.qiushibaike.com//']
    def parse(self, response):
        pass
