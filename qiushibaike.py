import requests
from bs4 import BeautifulSoup
import ssl
context = ssl._create_unverified_context()


num = 0
baseurl='https://www.qiushibaike.com/8hr/page/'
for pagenum in range(1,5):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    url=baseurl+str(pagenum)+'/'
    r=requests.get(url,headers=headers,verify=False)
    content=r.text

    soup = BeautifulSoup(content,'lxml')
    div1=soup.find_all(class_='article block untagged mb15 typs_hot')
    div2=soup.find_all(class_='article block untagged mb15 typs_long')
    div3=soup.find_all(class_='article block untagged mb15 typs_recent')
    div4=soup.find_all(class_='article block untagged mb15 typs_old')
    divs=[div1,div2,div3,div4]
    # print(div1)
    for d in divs:
        for div in d:
            joke = div.span.get_text()
            name= div.h2.get_text()
            if div.find_all(class_='thumb'):
                # image= div.find_all('img')
                # print(image)
                continue
            print(joke)
            # print(name)
            num+=1
            print('------------')
        print("===++++++****************+++++++=====")

    print("===+++page+++*****page",pagenum,"*******page****+++++page++=====")

print(num)