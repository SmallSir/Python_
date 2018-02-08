# -*- coding: utf-8 -*-
import scrapy
from meiju100.items import Meiju100Item

class Meiju100spiderSpider(scrapy.Spider):
    name = 'meiju100Spider'
    start_urls = ['http://www.meijutt.com/new100.html']

    def parse(self, response):
        subSelector = response.xpath('//ul[@class="top-list  fn-clear"]/li')
        items = []
        for sub in subSelector:
            item = Meiju100Item()
            item['storyName'] = sub.xpath('./h5/a/text()').extract()[0]
#            item['storyState'] = sub.xpath('./span[@class="state1 new100state1"]/text()').extract()[0]
            item['tvStation'] = sub.xpath('./span[@class="mjtv"]/text()').extract()[0]
           # item['updateTime'] = sub.xpath('./div[@class="lasted-time new100time fn-right"]/font/text()').extract()[0]
            item['storyLX'] = sub.xpath('./span[@class="mjjq"]/text()').extract()[0]
            print("----------------------------------")
            items.append(item)
        return items
