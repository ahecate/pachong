import requests
from bs4 import BeautifulSoup
import ssl
context = ssl._create_unverified_context()


headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
url ='https://www.zhihu.com/question/60787862'
r=requests.get(url=url,headers=headers,verify=False)
print(r.status_code)
# print(r.content)

soup=BeautifulSoup(r.content,'lxml')
# divs=soup.find_all(class_='RichContent RichContent--unescapable')
divs=soup.find_all(class_='RichContent-inner')
i=1
for div in divs:
    print(i)
    print(div.get_text())
    i+=1
    print('----')