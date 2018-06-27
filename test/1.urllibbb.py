# encoding:utf-8  # python2 不能使用中文，在文件的第一行加上这句注释就可以了
import urllib2


# 方式一
def download1(url):
    return urllib2.urlopen(url).read()


# print download1("http://wwww.baidu.com")

# 方式二
def download2(url):
    data_list = urllib2.urlopen(url).readlines()
    for line in data_list:
        if len(line.strip()) == 0:  # 全部为空格的行，不输出
            continue
        print line


# download2("http://wwww.baidu.com")


# 方式三
def download3(url):
    bai_du_file = urllib2.urlopen(url);
    while True:
        line = bai_du_file.readline()
        if not line:   # 没有数据了，则跳出循环
            break
        if len(line.strip()) == 0:  # 全部为空格的行，不输出
            continue
        print line


download3("http://wwww.baidu.com")
