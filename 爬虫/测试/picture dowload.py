import requests
import os
url = "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
root = "D://python项目//爬虫//测试"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)#检查是否有root这个文件路径，如果没有就添加
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件保存失败")
except:
    print("爬取失败")
