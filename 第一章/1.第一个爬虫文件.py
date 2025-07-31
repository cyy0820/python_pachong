#爬虫：通过编写程序来获取互联网上的资源
#百度
#需求：用程序模拟浏览器，输入网址，获取网页源代码
#python 搞定以上需求，特别简单
from urllib.request import urlopen

url="http://www.baidu.com"
html=urlopen(url)
# print(html.read())
# print(html.read().decode('utf-8'))  #baidu.con源代码
with open("mybaidu.html",mode='w', encoding='utf-8')as f:
    f.write(html.read().decode('utf-8')) #将获取到的源代码写入文件
print('over!')
