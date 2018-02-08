# -*- coding: utf-8 -*-



from meiju100.middlewares.resource import PROXIES
import random
class RandomProxy(object):
    def process_request(self,request,spider):
        proxy = random.choice(PROXIES)
        url = 'http://' + proxy
        print(url)
        request.meta['proxy'] = url