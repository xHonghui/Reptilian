# encoding:utf-8
# python 正则表达式回顾
import re

mystr = """<span class=\"search_yx_tj\">
        共<em>5830</em>个职位满足条件
    </span>"""

restr = "<em>(\\d+)</em>"  # 带括号表示只提取括号内的数据，不带括号则提取正则表达式匹配到的字符串
regex = re.compile(restr, re.IGNORECASE)
mylist = regex.findall(mystr)
print mylist
