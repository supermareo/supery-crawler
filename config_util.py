# coding=utf-8
import json


def load_config(path='starter_config.json', name=None):
    with open(path, 'r', encoding='utf-8') as f:
        json_str = ''.join(list(map(lambda x: x.replace('\n', ''), f.readlines())))
    json_obj = json.loads(json_str)
    if name is None:
        return json_obj
    for item in json_obj:
        if item['name'] == name:
            return item


def parse_selector(selector):
    splits = selector.split('::')
    return splits[0], splits[1]
