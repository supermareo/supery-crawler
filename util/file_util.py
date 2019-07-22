# coding=utf-8
# 文件操作工具类
import json
import os


# 按行读取
def read_lines(path):
    if os.path.isfile(path):
        with open(path, 'r', encoding='utf-8') as f:
            return f.readlines()
    return None


# 读取json文件，返回json转的python对象
def read_json_obj(path):
    lines = read_lines(path)
    if lines is None:
        return None
    return json.loads(''.join(list(map(lambda x: x.replace('\n', ''), lines))))


# 读取json文件，返回json字符串
def read_json_str(path):
    json_obj = read_json_obj(path)
    return json.dumps(json_obj)


# 追加一行
def append_line(path, line, end='\n'):
    dir_path = ''.join(path.split('/')[:-1])
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    with open(path, 'a', encoding='utf-8') as f:
        f.write(line + end)


# 追加多行
def append_lines(path, lines, end='\n'):
    dir_path = ''.join(path.split('/')[:-1])
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    with open(path, 'a', encoding='utf-8') as f:
        for line in lines:
            f.write(line + end)


# bytes写文件
def write_bytes(path, content):
    dir_path = ''.join(path.split('/')[:-1])
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    with open(path, 'wb') as f:
        f.write(content)


# 覆盖写文件
def write_line(path, content):
    dir_path = ''.join(path.split('/')[:-1])
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
