import requests
from bs4 import BeautifulSoup
import re
import traceback
import time
import numpy as np


#修改请求头文件，避免封IP
hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]
def getHTMLText(url):#参数为页面
    try:
        r = requests.get(url, timeout = 30,headers=hds[np.random.randint(0,len(hds))])
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
    sum = 0
    for s in lst:#对于sum这一块的代码主要是计算存入多少个，前90个股票存在问题，不考虑
        sum = sum + 1
        if sum < 90:
            continue
        if sum >= 100:
            break
        #time.sleep(np.random.rand() * 2)
        url = stockURL + s + ".html"
        html = getHTMLText(url)
        try:
            if html == "":
                continue
            soup = BeautifulSoup(html, 'html.parser')
            StockDict = {}
            stockInfo = soup.find('div', attrs = {'class':'bets-content'})
            try:
                name = soup.find_all(attrs={'class':'bets-name'})[0].text.split()[0]
            except IndexError:
                continue
            StockDict.update({'股票信息':name})#将获取到的股票名字先存下来
            keyList = stockInfo.find_all('dt')#获得该股票的信息名称
            valueList = stockInfo.find_all('dd')#获得该股票的信息的详细资料
            for i in range(len(keyList)):
                key = keyList[i].text
                value = valueList[i].text
                StockDict[key] = value
            with open(fpath, 'a',encoding='utf-8') as f:#将信息存到文件中
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

