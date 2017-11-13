from urllib.request import urlopen
from bs4 import BeautifulSoup

#建立可靠的网络连接

def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError) as e:
        print(e)
    try:
        obj = BeautifulSoup(html.read())
        title = obj.h1
    except AttributeError as e:
        print(e)
    return title
tt = getTitle("http://www.pythonscraping.com/pages/page1.html")
if tt == None:
    print("Title could not be found")
else:
    print(tt)

