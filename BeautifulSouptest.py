from bs4 import BeautifulSoup
import re

# BeautifulSoup
# https://cuiqingcai.com/1319.html
html='''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie<!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
'''

# print(type(html))

soup=BeautifulSoup(html,'lxml')
# print(soup.prettify())
#
# print(soup.title)
#
# print(soup.a)
# print(type(soup.a))
# print(soup.name)
# print(soup.a.name)
# print(soup.p)
# print(soup.p.attrs)
# print(soup.p['class'])
# print(soup.p.get('class'))
#
# soup.p['class']='newClass'
# print(soup.p)
# print(soup.p['class'])
#
# del soup.p['class']
# print(soup.p)
#
# print(soup.p.string)
# print(type(soup.p.string))
#
# print(soup.name)
# print(type(soup.name))
# print(soup.attrs)

# print(soup.a)
# print(soup.a.string)
# print(type(soup.a.string))

# if type(soup.a.string)== 'bs4.element.Comment' :
#     print(soup.a.string)

# print(soup.p.contents)
# print(soup.p)
# print(soup.p.string)

# print(soup.head.contents)
# print(soup.head.contents[0])
# print(soup.body.children)

# for ch in soup.body.children:
#     print(ch)

# for ch in soup.descendants:
#     print(ch)

# print(soup.head.string)
# print(soup.head)
# print(soup.head.contents)
# print(soup.title.string)
# print(soup.title)

# for str in soup.stripped_strings:
#     print(repr(str))


# p=soup.p
# print(p.parent.name)

# content = soup.head.title.string
# print(content.parent.name)
# # print(content.parents)
# for parent in content.parents:
#     print(parent.name)
#
#
# print(soup.p.next_sibling)
# print(soup.p.prev_sibling)
# print(soup.p.next_sibling.next_sibling)
#
# for sibling in soup.a.next_siblings:
#     print(repr(sibling))

# print(soup.head.next_element)
# print(soup.title.previous_element)

# for element in soup.a.next_elements:
#     print(repr(element))

# for i in soup.find_all("a"):
#     print(i.get("href"))

# print(soup.find_all('a'))
#
# for i in soup.find_all('a'):
#     print(i.get_text())

# for tag in soup.find_all(re.compile('t')):
#     print(tag.name)

# for i in soup.find_all(['a','b']):
#     print(i.name)
#
# for i in soup.find_all(True):
#     print(i.name)
# //传方法 不太懂//
# def has_class_but_no_id(tag):
#     if tag.has_attr('class') and (not tag.has_attr('id')):
#         return True
#     else:
#         return False
#
# print(soup.find_all(has_class_but_no_id))

# print(soup.find_all(id='link2'))

# print(soup.find_all(href=re.compile("els")))

# print(soup.find_all(id=re.compile('link')))

# print(soup.find_all(href=re.compile('els'),id='link1'))

# print(soup.find_all(class_='sister'))

# data_soup = BeautifulSoup('<div data-foo="value">foo!</div>','lxml')
# print(data_soup.find_all(attrs={"data-foo":"value"}))

# print(soup.find_all(text='Elsie'))
# print(soup.find_all(text=["Tillie", "Elsie", "Lacie"]))

# print(soup.find_all(text=re.compile("Dormouse")))

# print(soup.find_all("a",limit=2))

# print(soup.html.find_all("title"))
# print(soup.html.find_all("title", recursive=False))
# print(soup.find_all("title"))

# print(soup.find('a'))
#
# print(soup.find_all('a'))

# print(soup.select('title'))
# print(soup.select('a'))
# print(soup.select('.sister'))
# print(soup.select('#link1'))
# print(soup.find_all(id='link1'))

# print(soup.select('p #link1'))
# print(soup.select("head > title"))

# print(soup.select('a[class="sister"]'))

# print(soup.select('p a[href="http://example.com/elsie"]'))

print(type(soup.select('a')))

print(soup.select('a'))

# for title in soup.select('a'):
#     print(title.get_text())



