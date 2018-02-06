# -*- coding: utf-8 -*-
import scrapy
import re
import time
from qiushi.items import QiushiItem
class QiushispiderSpider(scrapy.Spider):
    name = 'qiushiSpider'
    start_urls = ['https://www.qiushibaike.com//']
    def parse(self, response):
        subSelector = response.xpath('//div[contains(@class, "article block untagged mb15")]')
        for div in subSelector:
            title = div.css('a').extract()
            number = ''
            number =re.findall(r'/article/\d*',title[2])[0]
            URL ='https://www.qiushibaike.com'+number
            yield scrapy.Request(url=URL,callback= self.parse_jobs)
    def parse_jobs(self,response):
        item =  QiushiItem()
        item['author'] = response.xpath('//div[@class="author clearfix"]//h2/text()').extract()[0]
        content = []
        content = response.xpath('//div[@class="content"]//text()|//div[@class="content"]//br//text()').extract()
        item['content'] = ''
        for nr in content:
            item['content'] += nr.replace("\n","")
        try:
            item['img'] = response.xpath('//div[@class="thumb"]/img/@src').extract()
        except IndexError:
            print("无图片")
        item['funNum'] = response.xpath('//i[@class="number"]/text()').extract()[0]
        item['talkNum'] = response.xpath('//i[@class="number"]/text()').extract()[1]
        time.sleep(5)
        yield item
