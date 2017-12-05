import requests
from bs4 import BeautifulSoup
import re
import traceback

def getHTMLText(url):#参数为页面
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def getStockList(lst, stockURL):#参数为存取股票代码列表,以及股票信息网站
    html = getHTMLText(stockURL)#解析获取股票代码的网站
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')#找到存储代码的位置
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}",href)[0])#获得代码
        except:
            continue

def getStockInfo(lst, stockURL, fpath):#参数为存取股票列表，股票信息网站，以及股票信息存储位置
    count = 0
    for s in lst:
        url = stockURL + s + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            soup = BeautifulSoup(html, 'html.parser')
            StockDict = {}
            stockInfo = soup.find('div', attrs = {'class':'bets-content'})
            name = stockInfo.find_all(attr={'class':'bets-name'})[0]
            StockDict.update({'股票信息':name.text.split()[0]})
            keyList = stockInfo.find_all('dt')
            valueList = stockInfo.find_all('dd')
            for i in range(len(keyList)):
                key = keyList[i].text
                value = keyList[i].text
                StockDict[key] = value
            with open(fpath, 'a',encoding='utf-8') as f:
                f.write(str(StockDict) + '\n')
                count = count + 1
                print("\r当前进度:{:.2f}%".format(count*100/len(lst)))
        except:
            traceback.print_exc()
            count = count + 1
            print("\r当前进度:{:.2f}%".format(count * 100 / len(lst)))
            continue


if __name__ == '__main__':
    Stock_list_url = 'http://quote.eastmoney.com/stocklist.html'#获取股票代码地址
    Stock_info_url = 'https://gupiao.baidu.com/stock/'#获取股票详细信息地址
    file_save = 'D://python项目//Python_//爬虫项目实例//StockInfo.txt'#存储股票信息位置
    slist = []#存储股票代码
    getStockList(slist, Stock_list_url)
    getStockInfo(slist, Stock_info_url,file_save)

