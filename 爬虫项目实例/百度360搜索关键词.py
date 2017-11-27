import requests
#百度360搜索关键词提交
#搜索引擎关键词提交接口
'''
百度的关键词接口
http://www.baidu.com/s?wd=keyword
360的关键词接口
http://www.so.com/s?q=keyword
'''
kv = {'wd':'Python'}
try:
    r = requests.get("http://www.baidu.com/s",params = kv)
    print(len(r.text))
except:
    print("爬取失败")
