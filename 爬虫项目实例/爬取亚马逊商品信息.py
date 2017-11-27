import requests
## 爬取亚马逊网上信息
url = "https//www.amzon.cn/gp/product/B01M8L5Z3Y"
kv = {'user-agent':'Mozilla/5.0'}
try:
    r = requests.get(url,headers = kv)
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")