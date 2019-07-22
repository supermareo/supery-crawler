# coding=utf-8

import datetime
import re
import time


# 获取今天日期字符串：20190720
def today_date_str():
    return time.strftime("%Y%m%d", time.localtime(time.time()))


REG_MINUTE = re.compile('(\d+)(分钟)前更新')
REG_HOUR = re.compile('(\d+)(小时)前更新')
REG_DAY = re.compile('(\d+)(天)前更新')
REG_WEEK = re.compile('(\d+)(周)前更新')
REG_MONTH = re.compile('(\d+)个(月)前更新')
REG_YEAR = re.compile('(\d+)(年)前更新')

REG_LIST = [REG_MINUTE, REG_HOUR, REG_DAY, REG_WEEK, REG_MONTH, REG_YEAR]


# 对网页上的时间格式进行处理，转换为时间戳
# 适配以下
# 1分钟前更新
# 23小时前更新
# 1天前更新
# 1周前更新
# 2个月前更新
# 1年前更新
def parse_time_str(time_str):
    num = -1
    flag = None
    for reg in REG_LIST:
        if reg.fullmatch(time_str):
            all = reg.findall(time_str)
            num, flag = all[0][0], all[0][1]
    if num == -1 or flag == None:
        print(f'no match {time_str}')
    return num, flag


def compare():
    pass


# 当前时间戳
def now_time_stamp():
    return int(round(time.time() * 1000))


# 从当期时间算起，几天前后时间戳
# flag - start 开始时间戳|end 结束时间戳
def days_time_stamp(days, end=True):
    # 今天
    today = datetime.date.today()
    new_day = today + datetime.timedelta(days=days)
    if end:
        acquire = new_day + datetime.timedelta(days=1)
        the_time = int(time.mktime(time.strptime(str(acquire), '%Y-%m-%d'))) - 1
    else:
        the_time = int(time.mktime(time.strptime(str(new_day), '%Y-%m-%d')))
    return int(round(the_time * 1000))


# 从当期时间算起，几分钟前后时间戳
# flag - start 开始时间戳|end 结束时间戳
def minutes_time_stamp(minutes, end=True):
    # 今天
    today = datetime.datetime.now()
    new_day = today + datetime.timedelta(minutes=minutes)
    if end:
        acquire = new_day + datetime.timedelta(minutes=1)
        the_time = int(time.mktime(time.strptime(str(acquire)[0:16], '%Y-%m-%d %H:%M'))) - 1
    else:
        the_time = int(time.mktime(time.strptime(str(new_day)[0:16], '%Y-%m-%d %H:%M')))
    return int(round(the_time * 1000))


# 从当期时间算起，几小时前后时间戳
# flag - start 开始时间戳|end 结束时间戳
def hours_time_stamp(hours, end=True):
    # 今天
    today = datetime.datetime.now()
    new_day = today + datetime.timedelta(hours=hours)
    if end:
        acquire = new_day + datetime.timedelta(hours=1)
        the_time = int(time.mktime(time.strptime(str(acquire)[0:13], '%Y-%m-%d %H'))) - 1
    else:
        the_time = int(time.mktime(time.strptime(str(new_day)[0:13], '%Y-%m-%d %H')))
    return int(round(the_time * 1000))


# 从当期时间算起，几周前后时间戳
# flag - start 开始时间戳|end 结束时间戳
def weeks_time_stamp(weeks, end=True):
    # 今天
    today = datetime.date.today()
    # 今天星期几
    weekday = int(time.strftime("%w"))
    # 本周周末
    new_day = today + datetime.timedelta(days=7 - weekday)
    new_day = new_day + datetime.timedelta(days=7 * weeks)
    if end:
        acquire = new_day + datetime.timedelta(days=1)
        the_time = int(time.mktime(time.strptime(str(acquire), '%Y-%m-%d'))) - 1
    else:
        the_time = int(time.mktime(time.strptime(str(new_day), '%Y-%m-%d')))
    return int(round(the_time * 1000))


# 从当期时间算起，几个月前后时间戳
# flag - start 开始时间戳|end 结束时间戳
def months_time_stamp(months, end=True):
    today = datetime.date.today()
    year = today.year
    month = today.month

    year = year + int(months / 12)
    if months < 0:
        months = -1 * months % 12
        if months >= month:
            year -= 1
            months = 12 - months + month
        else:
            months = month - months
    else:
        months = months % 12
        if months + month > 12:
            year += 1
            months = months + month - 12
        else:
            months = months + month

    if end:
        if months == 12:
            months = 1
            year += 1
        else:
            months += 1
        the_time = int(time.mktime(datetime.date(year, months, 1).timetuple())) - 1
    else:
        the_time = int(time.mktime(datetime.date(year, months, 1).timetuple()))
    return int(round(the_time * 1000))

# if __name__ == '__main__':
#     print(months_time_stamp(-6))
#     print(months_time_stamp(-6, end=False))
#     print(months_time_stamp(-7))
#     print(months_time_stamp(-7, end=False))
#     print(months_time_stamp(-8))
#     print(months_time_stamp(-8, end=False))
#     print(months_time_stamp(4))
#     print(months_time_stamp(4, end=False))
#     print(months_time_stamp(5))
#     print(months_time_stamp(5, end=False))
#     print(months_time_stamp(6))
#     print(months_time_stamp(6, end=False))
