#!/ur/bin/nv python3
#*- coding: utf-8 -*-
# 1.对网站翻页链接进行分析，发现链接为：“http://www.doutula.com/article/list/?page=3”，我们只需要对数字“3”进行更改便可以到达想访问的网页界面。
#
# 2.创建一个文件夹，用来存储表情包文件夹。
#
# 3.通过分析获得每个表情包的链接，并将其封装到一个函数中，函数最终返回一个含有单个网页所有表情包链接的列表。
#
# 4.对单个表情包链接进行访问，获得每个图片的链接，并将图片下载，保存到名为网页title的文件夹中，将这段代码封装到一个函数中。
#
# 5.创建一个函数，将3和4创建的函数进行封装。
#
# 6.创建一个继承threading.Thread的子类。
#
# 7.创建线程列表，创建线程，激活线程。
#导入模块
import requests
import os
import threading
from bs4 import BeautifulSoup
import time

#创建函数，用来对单页网页进行获取链接，返回一个包含所有链接的列表。
#继承线程类
class New_thread(threading.Thread):
    def __init__(self,han_name,han_can):
        super().__init__()
        self.han_name = han_name
        self.han_can = han_can
    def run(self):
        self.han_name(*self.han_can)
#获取单页的所有斗图包链接
def dan_url_list(url,num):
    headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
    url_2 = url + str(num)
    html = requests.get(url_2,headers=headers,timeout=30)
    html.encoding = html.apparent_encoding
    soup = BeautifulSoup(html.text,'html.parser')
    url_lists = []
    a= soup.find_all(name='a',attrs={'class':'list-group-item random_list'})
    for x in a:
        url_lists.append(x['href'])
    return url_lists

#获得单页链接后，对单个斗图包的url进行获取每张图片的链接。
def img_url(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'}
    html = requests.get(url,headers=headers,timeout=30)
    html.encoding = html.apparent_encoding
    soup = BeautifulSoup(html.text,'html.parser')
    title = soup.find('title').text.split(' - ')[0]
    print(title)
    try:
        os.mkdir('/home/admin/桌面/斗图/%s' % title)
    except:
        pass
    list_1 = []
    s = soup.find_all(name='div',attrs={'class':"artile_des"})
    for x in s:
        try:
            b = x.find('img')['src']
            list_1.append(b)
        except:
            pass
    for x in range(len(list_1)):
        c = requests.get(list_1[x]).content
        with open('/home/admin/桌面/斗图/%s/%s.jpg' % (title,x),'wb') as www:
            www.write(c)

#处理单页数据,这个函数将获取到的包链接用img_url函数进行处理，将图片下载到制定文件夹中。
def down_all(url,num):
    for x in dan_url_list(url,num):
        img_url(x)
#创建多线程。
def main(page_num):
    print('...........Start：%s...............' % time.ctime())
    thr_list = []
    url = 'http://www.doutula.com/article/list/?page='
    for x in range(1,page_num+1):
        t = New_thread(down_all,(url,x))
        thr_list.append(t)
    #启动线程
    for x in thr_list:
        x.start()
    for x in thr_list:
        x.join()
    print('.........All Done: %s..............' % time.ctime())

if __name__ == '__main__':
    a = input('你想获取多少页表情包？')
    main(int(a))