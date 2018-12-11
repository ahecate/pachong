from bs4 import BeautifulSoup
import requests
import urllib.request
import os
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



def page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    r = requests.get(url, headers, verify=False)
    context = r.text

    soup = BeautifulSoup(context, 'lxml')
    links = soup.find_all(class_='img-responsive lazy image_dta')

    for i in links:
        alt = i['alt']
        img_url = i['data-backup'].replace('!dta', '')
        # img_url=..[:-4]
        suffix = img_url.split('.')[-1]
        fileName = alt + '.' + suffix

        dir = 'images'
        if not os.path.exists(dir):
            os.mkdir(dir)
            print("mkdir dir")

        # 下载方式1
        try:
            urllib.request.urlretrieve(img_url, 'images/' + fileName)
        except FileNotFoundError:
            print("emm…大概是文件名有/暂时不处理嘻嘻")
        else:
            print("下载成功----" + fileName)

        # 下载方式2 写入文件
        # img_content = requests.get(img_url).content
        # with open(f'images/{fileName}', 'wb') as fp:
        #     fp.write(img_content)
        #     print("下载成功----" + fileName)


def main():
    for num in range(1, 2):
        url = f'https://www.doutula.com/photo/list/?page={num}'
        print(f"这是第{num}页～")
        page(url)


if __name__ == '__main__':
    main()
