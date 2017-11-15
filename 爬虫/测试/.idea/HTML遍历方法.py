import requests
from  bs4 import BeautifulSoup
r = requests.get("http://python123.io/ws/demo.html")
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
#获得body儿子节点第二个
#print(soup.body.contents[1])
print(soup.title.parent)
'''
上搜
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
'''
