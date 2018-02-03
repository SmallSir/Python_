# -*- coding: utf-8 -*-



from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware


class CustomUserAgent(UserAgentMiddleware):
    #设置了请求头
    def process_request(self, request, spider):
        #ua是请求头
        ua = 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
        request.headers.setdefault('User-Agent',ua)

class CustomProxy(object):
    def proces_request(self,request,spider):
        request.meta['proxy'] = 'http://114.33.202.73:8118'