# coding=utf-8

import re

import requests
from bs4 import BeautifulSoup

import config_util

config = config_util.load_config(name='qunfenxiang')

url_array = []


def start():
    while len(url_array) > 0:
        url = url_array.pop(0)
        craw_list(url)


def craw_list(url):
    print(f'start crawl {url}')
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    next_page_url = None
    if 's_selector_next_page' in config:
        css, attr = config_util.parse_selector(config['s_selector_next_page'])
        next_page = soup.select_one(css)
        if next_page is not None:
            next_page_url = next_page.attrs[attr]
    else:
        pattern = re.compile(config['s_regex_next_page'])
        groups = pattern.findall(html)
        print(groups)
        next_page_url = groups[0]

    if next_page_url is not None:
        base_url = config['s_base_url']
        real_url = base_url + next_page_url
        url_array.append(real_url)

    item_config = config['s_items']
    items = soup.select(item_config['selector'])
    item_data_list = []
    for item in items:
        item_data = {}
        for k, v in item_config.items():
            if k == 'selector':
                continue
            css, attr = config_util.parse_selector(v)
            if css == '':
                one = item
            else:
                one = item.select_one(css)
            if attr == 'text':
                item_data[k] = one.text.strip()
            elif attr.startswith('stripped'):
                rules = attr.split('-')[1]
                strings = list(one.stripped_strings)
                if rules.startswith('[') and rules.endswith(']'):
                    rule_split = rules[1:-1].split(',')
                    str_list = []
                    for i in rule_split[0:-1]:
                        str_list.append(strings[int(i)])
                    item_data[k] = ''.join(str_list) if rule_split[-1] == 'None' else rule_split[-1].join(str_list)
                else:
                    item_data[k] = strings[int(rules)]
            else:
                item_data[k] = one.attrs[attr]
        item_data_list.append(item_data)

    for data in item_data_list:
        craw_detail(data)


def craw_detail(item_data):
    print(f'start crawl detail {item_data}')
    url = config['s_base_url'] + item_data['selector_url']
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    item_detail_config = config['s_item_detail']
    detail = {}
    for k, v in item_detail_config.items():
        css, attr = config_util.parse_selector(v)
        if css == '':
            one = soup
        else:
            one = soup.select_one(css)
        if attr == 'text':
            detail[k] = one.text.strip()
        elif attr.startswith('stripped'):
            rules = attr.split('-')[1]
            strings = list(one.stripped_strings)
            if rules.startswith('[') and rules.endswith(']'):
                rule_split = rules[1:-1].split(',')
                str_list = []
                for i in rule_split[0:-1]:
                    str_list.append(strings[int(i)])
                detail[k] = ''.join(str_list) if rule_split[-1] == 'None' else rule_split[-1].join(str_list)
            else:
                detail[k] = strings[int(rules)]
        else:
            detail[k] = one.attrs[attr]
    print(detail)


if __name__ == '__main__':
    start_url = config['s_start_url']
    url_array.append(start_url)
    start()
