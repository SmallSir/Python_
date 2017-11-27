import requests
import re
import time


def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)#设定超时时间
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return print("解析网页失败")
def parsePage(li, html):
    try:
        counts = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)#正则获取价格
        names = re.findall(r'\"raw_title\"\:\".*?\"',html)#正则获取名字
        for i in range(len(counts)):
            price = eval(counts[i].split(':')[1])#以:分割，获取价格，同时删除引号等符号
            title = eval(names[i].split(':')[1])
            li.append([price, title])
    except:
        print("爬取失败")


def printGoodList(lis):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","产品信息"))
    num = 1
    for g in lis:
        num = num + 1
        print(tplt.format(num, g[0], g[1]))

if __name__ == '__main__':
    goods = "口红"
    depth = 3
    start_url = 'http://s.taobao.com/search?q=' + goods
    list = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(list,html)
        except:
            continue
    printGoodList(list)
