# coding=utf-8
# 历史数据相关操作工具类

from util.file_util import read_json_obj, write_line
import json


# 加载历史记录
def load(path='history/', name=None):
    return read_json_obj(path + name + '.json')


# 更新历史记录
def update(name,data, path='history/'):
    json_str = json.dumps(data, indent=2)
    write_line(path + name + '.json', json_str)
