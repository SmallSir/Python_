# -*- coding: utf-8 -*-
import scrapy
import re
import time
from WangYiMusicTest.items import WangyimusictestItem
from WangYiMusicTest.settings import DEFAULT_REQUEST_HEADERS
class MusicspiderSpider(scrapy.Spider):
    name = 'MusicSpider'
    start_urls = ['http://music.163.com/artist/album?id=3684']
    def parse(self, response):
        page = response.xpath('//a[@class="zpgi"]/text()').extract()
        page_number = int(page[len(page)-1])
        url = u'http://music.163.com/artist/album?id=3684&limit=12&offset='
        if page_number == None :
            page_number = int(1)
        for i in  range(page_number):
            page_url = url + str(i*12)
            yield scrapy.Request(url=page_url,callback=self.parse_cds)
    def parse_cds(self,response):
        base_url = u'http://music.163.com'
        cds = response.xpath('//ul[@class="m-cvrlst m-cvrlst-alb4 f-cb"]/li')
        for i in range(len(cds)):
            cd_message = cds.xpath('//li/p[@class="dec dec-1 f-thide2 f-pre"]/a/@href').extract()[i]
            messages = base_url + cd_message
            time.sleep(5)
            yield  scrapy.Request(url=messages,callback=self.parse_cd)
    def parse_cd(self,response):
        base_url = u'http://music.163.com'
        songs = response.xpath('//ul[@class="f-hide"]/li')
        for i in range(len(songs)):
            song_id = songs.xpath('//li/a/@href').extract()[i]
            id = song_id[9:]
            song_url = base_url + song_id
            yield scrapy.Request(url=song_url,meta={'id':id},callback=self.parse_song)
    def parse_song(self,response):
        id = response.meta['id']
        base_url = u'http://music.163.com'
        item = WangyimusictestItem()
        data = {
            'csrf_token': '',
            'params': 'Ak2s0LoP1GRJYqE3XxJUZVYK9uPEXSTttmAS+8uVLnYRoUt/Xgqdrt/13nr6OYhi75QSTlQ9FcZaWElIwE+oz9qXAu87t2DHj6Auu+2yBJDr+arG+irBbjIvKJGfjgBac+kSm2ePwf4rfuHSKVgQu1cYMdqFVnB+ojBsWopHcexbvLylDIMPulPljAWK6MR8',
            'encSecKey': '8c85d1b6f53bfebaf5258d171f3526c06980cbcaf490d759eac82145ee27198297c152dd95e7ea0f08cfb7281588cdab305946e01b9d84f0b49700f9c2eb6eeced8624b16ce378bccd24341b1b5ad3d84ebd707dbbd18a4f01c2a007cd47de32f28ca395c9715afa134ed9ee321caa7f28ec82b94307d75144f6b5b134a9ce1a'
        }
        DEFAULT_REQUEST_HEADERS['Referer'] = base_url + '/playlist?id=' + str(id)
        music_comment = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(id)
        item['comments'] = yield scrapy.FormRequest(music_comment, callback=self.parse_comment, formdata=data)
        item['music'] = response.xpath('//em[@class="f-ff2"]/text()').extract()[0]
        item['singer'] = response.xpath('//p[@class="des s-fc4"]//a[@class="s-fc7"]/text()').extract()[0]
        item['cd'] = response.xpath('//p[@class="des s-fc4"]//a[@class="s-fc7"]/text()').extract()[-1]
        #time.sleep(2)
        yield item
    def parse_comment(self,response):
        result = json.loads(response.text)
        return result['total']

