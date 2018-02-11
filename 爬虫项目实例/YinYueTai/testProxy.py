import requests

try:
    requests.get('http://wenshu.court.gov.cn/', proxies={"http":"http://61.135.217.7:80"})
except:
    print('connect failed')
else:
    print ('success')

