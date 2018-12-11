"""
网易云音乐
豆瓣电影
糗事百科
知乎
==，
"""


# class Student:
#     pass

class Developer(object):
    name = 'ele'
    site = 'http://ele.me'

    __sex = 0

    def __init__(self, name, site, sex):
        self.name = name
        self.site = site
        self.__sex = sex

    def get_sex(self):
        return self.__sex

    def set_sex(self, sex):
        self.__sex = sex


class AndroidCoder(Developer):
    coder_id = 1024

    def __init__(self, name, site, sex, coder_id):
        super(AndroidCoder, self).__init__(name, site, sex)
        self.coder_id = coder_id

    def set_sex(self, sex):
        self.__sex = sex
        print('this is a secret')

    def get_sex(self):
        return self.__sex


if __name__ == '__main__':
    androidCoder1=AndroidCoder('jiaqi','www.abc.me',0,1023)
    androidCoder1.set_sex(1)
    print(androidCoder1.get_sex(),androidCoder1.site)