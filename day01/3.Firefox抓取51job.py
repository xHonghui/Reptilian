# encoding:utf-8
import re
import selenium
import selenium.webdriver


def get_web_info(url):
    driver = selenium.webdriver.Firefox()
    driver.get(url)
    web_data = driver.page_source
    if web_data is not None:
        return web_data
    else:
        return None


keyword = ["java", "android", "python", "h5"]


def get_data(keyword):
    for i in range(len(keyword)):
        url = "https://search.51job.com/list/030200,000000,0000,00,9,99," + keyword[
            i] + ",2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99" \
                 "&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=" \
                 "&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        web_str = get_web_info(url)
        restr = """<div class="rt">([\s\S]*?)</div>"""
        regex = re.compile(restr)
        data_list = regex.findall(web_str)
        if len(data_list) > 0:
            web_str = data_list[0]
            restr = "(\\d+)"
            regex = re.compile(restr, re.IGNORECASE)
            data_list = regex.findall(web_str)
            if len(data_list) > 0:
                print keyword[i], data_list[0]
            else:
                print "查找失败"
        else:
            print "查找失败"


keyword = ["java", "android", "python", "h5"]
get_data(keyword)
