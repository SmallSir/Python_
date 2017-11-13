import requests

'''
def getHTMLText(url):
    try:
        r = request.get(url,params = {'key1':'value1','key2':'value2'})
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding #编码更改，前一个是推测编码，后一个是确定编码
        return r.text
    except:
        return "产生异常"

if __name__ =="__name__":
    url = "http://python123.io/ws"
    print(getHTMLText(url))
'''

kv = {'key1':'value1','key2':'value2'}
body = '主体内容'
r = requests.request('POST','http://python123.io/ws',json = kv)
r = requests.request('POST','http://python123.io/ws',data = body)
hd = {'user-agent':'Chrome/10'}
r = requests.request('POST','http://python123.io/ws',headers = hd)