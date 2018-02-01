# -*- coding: utf-8 -*-
import scrapy
from getip.items import GetipItem

class IpdlSpider(scrapy.Spider):
    name = 'ipdl'
    start_urls = []
    for i in range(1,2):
        start_urls.append('http://www.xicidaili.com/nn/'+str(i))
    def parse(self, response):
        subSelector = response.xpath('//tr[@class=""]|//tr[@class="odd"]')
        ii = response.css('.odd')
        items = []
        for sub in subSelector:
            item = GetipItem()
            item['ip'] = sub.css('td::text').extract()[0]
            item['port'] = sub.css('td::text').extract()[1]
            item['protocol'] = sub.css('td::text').extract()[5]
            items.append(item)
        return items