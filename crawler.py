# coding=utf-8
import requests
from bs4 import BeautifulSoup

import config_util

config = config_util.load_config(name='qunfenxiang')
print(config)
start_url = config['s_start_url']
print(start_url)
html = requests.get(start_url).text
soup = BeautifulSoup(html, 'html.parser')

css, attr = config_util.parse_selector(config['s_selector_next_page'])
next_page_url = soup.select_one(css).attrs[attr]
print(next_page_url)

item_config = config['s_items']
items = soup.select(item_config['selector'])
item_datas = []
for item in items:
    item_data = {}
    for k, v in item_config.items():
        if k == 'selector':
            continue
        css, attr = config_util.parse_selector(v)
        one = item.select_one(css)
        if attr == 'text':
            item_data[k] = one.text
        elif attr.startswith('stripped'):
            splits = attr.split('-')
            item_data[k] = list(one.stripped_strings)[int(splits[1])]
        else:
            item_data[k] = one.attrs[attr]
    item_datas.append(item_data)

for data in item_datas:
    print(data)
