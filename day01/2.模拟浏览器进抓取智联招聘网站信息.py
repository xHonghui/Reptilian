# encoding:utf-8
# 2.模拟浏览器进抓取智联招聘网站信息
import re
import selenium  # 测试框架
import selenium.webdriver  # 模拟浏览器


def get_web_data(url):
    driver = selenium.webdriver.Firefox()  # 调用火狐浏览器
    driver.get(url)  # 设置 url
    web_data = driver.page_source  # 获取源代码数据
    restr = "<em>(\\d+)</em>"
    regex = re.compile(restr, re.IGNORECASE)
    target_list = regex.findall(web_data)
    driver.close()
    if len(target_list) > 0:
        return target_list[0]
    else:
        return None


def get_data(keyword, address):
    for i in range(len(address)):
        for j in range(len(keyword)):
            url = "https://sou.zhaopin.com/jobs/searchresult.ashx?jl=" + bytes(address[i]) + "&kw=" + keyword[
                j] + "&sm=0&p=1"
            target_num = get_web_data(url)
            if target_num is not None:  # 非空判断
                print address[i], keyword[j], target_num


keyword = ["java", "android", "python", "h5"]
address = ["北京", "深圳", "广州", "上海"]
get_data(keyword, address)
