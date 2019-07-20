# coding=utf-8
from util.file_util import read_json_obj


# 加载配置文件
# path - 默认使用config/super-config.json文件
# name - 指定配置文件中某项，否则返回所有
def load_config(path='config/super-config.json', name=None):
    json_obj = read_json_obj(path)
    if name is None:
        return json_obj
    if name not in json_obj:
        return None
    return json_obj[name]
