# encoding:utf-8
# 使用 urllib2 抓取前程无忧网站信息
import re
import urllib2


def get_web_data(url):
    webdata = urllib2.urlopen(url).read()
    return webdata


def get_data(keyword):
    for j in range(len(keyword)):
        url = "https://search.51job.com/list/030200,000000,0000,00,9,99," + keyword[
            j] + ",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99" \
                 "&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=" \
                 "&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        webstr = get_web_data(url)
        # 源文件出现乱码，正则表达式匹配u、不成功
        restr = """<div class="rt">([\s\S]*?)</div>"""  # <div class="rt">共3461条职位</div>，中间有空格和换行符，需要进行两次匹配拿取目标数据
        regex = re.compile(restr, re.IGNORECASE)
        data_list = regex.findall(webstr)
        if len(data_list) > 0:
            webstr = data_list[0]
            restr = "(\\d+)"  # 获取目标数据
            regex = re.compile(restr, re.IGNORECASE)
            data_list = regex.findall(webstr)
            if len(data_list) > 0:
                print "广州", keyword[j], data_list[0]
        else:
            print "查找失败"


keyword = ["java", "android", "python", "h5"]
get_data(keyword)
