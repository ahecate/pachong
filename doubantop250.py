import json
import re
from lxml import etree
import pymongo
import time
import requests
import ssl
context = ssl._create_unverified_context()
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['douban']
table = db['douban-250']

url = ['https://movie.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}

def download_urls(url):
    response = requests.get(url,headers=header,verify=False)
    selector = etree.HTML(response.text)
    url_list = selector.xpath('//a[@class=""]/@href')
    return url_list

def get_content(url):
    #print(url)
    response = requests.get(url,headers=header,verify=False)
    selector = etree.HTML(response.text)
    name = selector.xpath('//span[@property="v:itemreviewed"]/text()')[0]
    director = selector.xpath('//a[@rel="v:directedBy"]/text()')[0]
    #主演只取前三个
    actor = selector.xpath('//a[@rel="v:starring"]/text()')[:3]
    actor = r';'.join(actor)
    type = selector.xpath('//span[@property="v:genre"]/text()')
    type = r';'.join(type)
    runtime = selector.xpath('//span[@property="v:runtime"]/text()')[0]
    #制片国家使用re
    country = re.findall('<span class="pl">制片国家/地区:</span>(.+)<br/>', response.text, re.S)
    level = selector.xpath('//strong[@class="ll rating_num"]/text()')[0]

    info = {
        '电影':name,
        '导演':director,
        '主演':actor,
        '类型':type,
        '国家':country,
        '时长':runtime,
        '评价':level }

    table.insert_one(info)

if __name__=='__main__':
    start = time.time()
    url_lists = []  #全部链接的列表
    for i in url:
        url_lists.extend(download_urls(i))
    for url in url_lists:
    #有几个链接是无效的 ，使用try...except...
        try:
            get_content(url)
        except Exception as e:
            continue

    stop = time.time()
    print('run time:', (stop - start))
