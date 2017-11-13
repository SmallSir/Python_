from urllib.request import urlopen
from bs4 import BeautifulSoup
import  re

#http://www.pythonscraping.com/pages/warandpeace.html
#http://www.pythonscraping.com/pages/page3.hetml
'''查找标签
web = "http://www.pythonscraping.com/pages/warandpeace.html"
html = urlopen(web)
bsobj = BeautifulSoup(html)ii
nameList = bsobj.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())
'''
'''
查找子标签或者兄弟标签
web = "http://www.pythonscraping.com/pages/page3.hetml"
html = urlopen(web)
bsobj = BeautifulSoup(html)
寻找兄弟标签
for sibling in bsobj.find("table",{"id":"gitList"}).tr.next_siblings:
    print(sibling)
寻找子标签
for child in bsobj.find("table",{"id":"giftList"}).children:
    print(child)
'''
'''
查找父亲标签
html = urlopen(web)
bsobj = BeautifulSoup(html)
print(bsobj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
'''
'''
import requests

def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


if __name__ == "__name__":
    url = "http://www.baidu.com"
    print(getHTMLText(url))
'''
