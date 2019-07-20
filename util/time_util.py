# coding=utf-8

import time


# 获取今天日期字符串：20190720
def today_date_str():
    return time.strftime("%Y%m%d", time.localtime(time.time()))
