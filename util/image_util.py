# coding=utf-8
import os

import requests

from util.file_util import write_bytes
from util.time_util import today_date_str


# 下载图片
# url - 图片地址
# path - 存储路径
# 返回文件名称
# 如果下载出错，返回空字符串
def download_img(url, path):
    try:
        response = requests.get(url, verify=False)
        write_bytes(path, response.content)
        return path.split('/')[-1]
    except:
        print(f'download image {url} error')
        return ''


# 获取下一个文件名
# type - group表示群,master表示群主
def next_img_name(img_path, type='group'):
    # 呼气
    date_str = today_date_str()
    files = os.listdir(img_path)
    if type == 'group':
        count = len(list(filter(lambda x: (date_str + 'A' not in x and date_str in x), files)))
        return f'{date_str}{count + 1}.png'
    else:
        count = len(list(filter(lambda x: (date_str + 'A') in x, files)))
        return f'{date_str}A{count + 1}.png'
