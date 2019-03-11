from bs4 import BeautifulSoup
import requests
import urllib.request
import os


def page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    r = requests.get(url, headers)
    context = r.text

    soup = BeautifulSoup(context, 'lxml')
    links = soup.find_all(class_='col-xs-6 col-md-2')

    for i in links:
        imgs = i.find_all(class_='img-responsive lazy image_dtb')
        for img in imgs:
            img_url = img['data-original']
            img_name = i.p.get_text()

        suffix = img_url.split('.')[-1]
        filename = img_name + '.' + suffix
        dir = 'images_keywords'

        if not os.path.exists(dir):
            os.mkdir(dir)
            print("mkdir dir")

        try:
            urllib.request.urlretrieve(img_url, dir + '/' + filename)
        except FileNotFoundError:
            print("emm…大概是文件名有/暂时不处理嘻嘻")
        else:
            print("下载成功----" + filename)


def main():
    keywords = '爸爸'
    for num in range(1,2):
        url = f'https://www.doutula.com/search?keyword={keywords}&page={num}'
        print(url)

    page(url)


if __name__ == '__main__':
    main()
