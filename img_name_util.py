# coding=utf-8

import os

from time_util import today_date_str


# 获取下一个文件名
# type - group表示群,master表示群主
def next_img_name(type='group'):
    # 呼气
    date_str = today_date_str()
    files = os.listdir('./data/imgs')
    if type == 'group':
        count = len(list(filter(lambda x: (date_str + 'A' not in x and date_str in x), files)))
        return f'{date_str}{count + 1}.png'
    else:
        count = len(list(filter(lambda x: (date_str + 'A') in x, files)))
        return f'{date_str}A{count + 1}.png'


print(next_img_name())