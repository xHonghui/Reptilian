# encoding:utf-8
# 使用 urllib2 抓取智联招聘网站信息
import re
import urllib2


def get_web_data(url):
    webdata = urllib2.urlopen(url).read()
    return webdata


def get_data(keyword, address):
    for i in range(len(address)):
        for j in range(len(keyword)):
            url = "https://sou.zhaopin.com/jobs/searchresult.ashx?jl=" + bytes(address[i]) + "&kw=" + keyword[
                j] + "&sm=0&p=1"
            webstr = get_web_data(url)
            restr = "<em>(\\d+)</em>"
            regex = re.compile(restr, re.IGNORECASE)
            data_list = regex.findall(webstr)
            if len(data_list) > 0:
                print address[i], keyword[j], data_list[0]
        print "============================================================="


keyword = ["java", "android", "python", "h5"]
address = ["北京", "深圳", "广州", "上海"]
get_data(keyword, address)
