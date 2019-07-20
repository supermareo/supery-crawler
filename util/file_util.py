# coding=utf-8
# 文件操作工具类
import json


# 按行读取
def read_lines(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.readlines()


# 读取json文件，返回json转的python对象
def read_json_obj(path):
    lines = read_lines(path)
    return json.loads(''.join(list(map(lambda x: x.replace('\n', ''), lines))))


# 读取json文件，返回json字符串
def read_json_str(path):
    json_obj = read_json_obj(path)
    return json.dumps(json_obj)


# 追加一行
def append_line(path, line, end='\n'):
    with open(path, 'a', encoding='utf-8') as f:
        f.write(line + end)


# 追加多行
def append_lines(path, lines, end='\n'):
    with open(path, 'a', encoding='utf-8') as f:
        for line in lines:
            f.write(line + end)


# bytes写文件
def write_bytes(path, content):
    with open(path, 'wb') as f:
        f.write(content)
