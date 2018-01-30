# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class ZzweatherSpider(scrapy.Spider):
    name = 'zzweather'
    start_urls = []
    citys =['zhengzhou','qinzhou','chengdu']
    for city in citys:
        start_urls.append('https://www.tianqi.com/'+ city+ '/')


    def parse(self, response):
        subSelector = response.css('.weatherbox')
        items = []
        for i in range(7):
            city = subSelector.css('.name h2::text').extract()[0]
            item = WeatherItem()
            data = subSelector.css('.week li b::text').extract()[i]
            item['cityDate'] = city + data
            item['week'] = subSelector.css('.week span::text').extract()[i]
            temps = ''
            temps = subSelector.css('.zxt_shuju span::text').extract()[i]
            item['temperature'] = temps + '~' + subSelector.css('.zxt_shuju b::text').extract()[i]
            item['weather'] = subSelector.xpath('.//ul[@class="txt txt2"]/li/text()').extract()[i]
            item['wind'] = subSelector.xpath('.//ul[@class="txt"]/li/text()').extract()[i]
            items.append(item)
        return items