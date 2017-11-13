import requests
url = "http://www.ip138.com/ips138.asp?ip="
try:
    r = requests.get(url + '171.212.89.35')
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")
