import requests
from bs4 import BeautifulSoup

import config_util
from image_util import download_img
from img_name_util import next_img_name

config = config_util.load_config(name='qunfenxiang')

url_array = []


def start():
    url_array.append(config['start_url'])
    while len(url_array) > 0:
        url = url_array.pop(0)
        craw_list(url)


def craw_list(url):
    print(f'start crawl {url}')
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')

    # 提取下一页地址并添加到列表待处理
    process_next_page_url(soup)
    # 提取页面要处理列表元素
    page_items = process_page_items(soup)
    # 提取详情
    for page_item in page_items:
        detail = craw_detail(page_item)
        restore_data(detail)
    # item_config = config['s_items']
    # items = soup.select(item_config['selector'])
    # item_data_list = []
    # for item in items:
    #     item_data = {}
    #     for k, v in item_config.items():
    #         if k == 'selector':
    #             continue
    #         css, attr = config_util.parse_selector(v)
    #         if css == '':
    #             one = item
    #         else:
    #             one = item.select_one(css)
    #         if attr == 'text':
    #             item_data[k] = one.text.strip()
    #         elif attr.startswith('stripped'):
    #             rules = attr.split('-')[1]
    #             strings = list(one.stripped_strings)
    #             if rules.startswith('[') and rules.endswith(']'):
    #                 rule_split = rules[1:-1].split(',')
    #                 str_list = []
    #                 for i in rule_split[0:-1]:
    #                     str_list.append(strings[int(i)])
    #                 item_data[k] = ''.join(str_list) if rule_split[-1] == 'None' else rule_split[-1].join(str_list)
    #             else:
    #                 item_data[k] = strings[int(rules)]
    #         else:
    #             item_data[k] = one.attrs[attr]
    #     item_data_list.append(item_data)
    #
    # for data in item_data_list:
    #     # craw_detail(data)
    #     pass


# 爬取详情页
def craw_detail(page_item):
    url = page_item['url']
    print(f'star crawl detail {url}')
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    attrs_cfg = config['detail']['attrs']
    item = {'id': url}
    for attr_cfg in attrs_cfg:
        item[attr_cfg['name']] = extract(soup, attr_cfg)
    return item


#     "next_page": {
#       "selector_type": "css",
#       "selector_val": "a.pageNext",
#       "val": "href",
#       "val_prefix": "http://www.qunfenxiang.net/group"
#     }
# 提取下一页地址
def process_next_page_url(soup):
    cfg = config['next_page']
    next_page_url = extract(soup, cfg)
    if next_page_url is not None:
        url_array.append(next_page_url)
    # if 's_selector_next_page' in config:
    #     css, attr = config_util.parse_selector(config['s_selector_next_page'])
    #     next_page = soup.select_one(css)
    #     if next_page is not None:
    #         next_page_url = next_page.attrs[attr]
    # else:
    #     pattern = re.compile(config['s_regex_next_page'])
    #     groups = pattern.findall(html)
    #     print(groups)
    #     next_page_url = groups[0]
    #
    # if next_page_url is not None:
    #     base_url = config['s_base_url']
    #     real_url = base_url + next_page_url
    #     url_array.append(real_url)
    #


# 提取页面待处理列表元素，返回一个列表
#     "items": {
#       "selector_type": "css",
#       "selector_val": "div.boldBorder",
#       "attrs": [
#         {
#           "name": "url",
#           "selector_type": "css",
#           "selector_val": "a",
#           "val": "href"
#         },
#         {
#           "name": "title",
#           "selector_type": "css",
#           "selector_val": "i.c_title",
#           "val": "text"
#         },
#         {
#           "name": "last_update",
#           "selector_type": "css",
#           "selector_val": "div.f12.c888",
#           "val": "stripped-1"
#         }
#       ]
#     }
def process_page_items(soup):
    cfg = config['items']
    attrs = cfg['attrs']
    docs = extract(soup, cfg)
    items = []
    for doc in docs:
        item = {}
        for attr in attrs:
            val = extract(doc, attr)
            item[attr['name']] = val
        items.append(item)
    # print(items)
    return items


def extract(soup, cfg):
    selector_type = cfg['selector_type']
    selector_val = cfg['selector_val']

    result = ''
    if selector_type == 'css':
        if not 'val' in cfg:
            return soup.select(selector_val)
        doc = soup.select_one(selector_val)
        val = cfg['val']
        if val == 'text':
            result = doc.text
        elif val.startswith('stripped'):
            rules = val.split('-')[1]
            strings = list(doc.stripped_strings)
            if rules.startswith('[') and rules.endswith(']'):
                rule_split = rules[1:-1].split(',')
                str_list = []
                for i in rule_split[0:-1]:
                    str_list.append(strings[int(i)])
                result = ''.join(str_list) if rule_split[-1] == 'None' else rule_split[-1].join(str_list)
            else:
                result = strings[int(rules)]
        else:
            result = doc.attrs[val]
    elif selector_type == 'find':
        selector_text = cfg['selector_text']
        doc = soup.find(selector_val, text=selector_text)
        parent = cfg['parent']
        if parent:
            doc = doc.parent
        val = cfg['val']
        if val == 'text':
            result = doc.text
        elif val.startswith('stripped'):
            rules = val.split('-')[1]
            strings = list(doc.stripped_strings)
            if rules.startswith('[') and rules.endswith(']'):
                rule_split = rules[1:-1].split(',')
                str_list = []
                for i in rule_split[0:-1]:
                    str_list.append(strings[int(i)])
                result = ''.join(str_list) if rule_split[-1] == 'None' else rule_split[-1].join(str_list)
            else:
                if len(strings) > int(rules):
                    result = strings[int(rules)]
        else:
            result = doc.attrs[val]

    if 'val_prefix' in cfg:
        val_prefix = cfg['val_prefix']
        return val_prefix + result

    return result


# {
#     "id": "http://www.qunfenxiang.net/group/12779.html",
#     "title": "充100送68 尤果娱乐",
#     "time": "2019-06-19 12:36:41",
#     "industry": "游戏玩乐",
#     "location": "上海市",
#     "tag": "",
#     "brief": "无需下载 微信扫码即可登录      实力尤果娱乐  国内最火微信平台 全网诚招代理微信：785934000 QQ:642392350",
#     "qr_group": "http://www.qunfenxiang.net/d/file/2019-05-16/bd0077e6a5272685190849ecee61dfaa.png",
#     "qr_master": "http://www.qunfenxiang.net/d/file/2019-05-16/bd0077e6a5272685190849ecee61dfaa.png",
#     "account_master": "785934000"
# }
def restore_data(data):
    print(f'restore {data}')
    # 下载图片
    qr_group_name = download_img(data["qr_group"], './data/imgs/' + next_img_name())
    qr_master_name = download_img(data["qr_master"], './data/imgs/' + next_img_name(type='master'))
    real_data = {}
    # 把值里面所有','换成中文'，',防止影响csv格式，并去除换行
    for k, v in data.items():
        real_data[k] = v.replace(',', '，').replace('\n', '').replace('\r', '')

    # 生成要存入csv的字符串
    # 编号,群标题,发布时间,行业,地区,标签,群简介,群二维码图片,群主微信号,群主二维码
    line = f'{real_data["id"].split("/")[-1].split(".")[0]},{real_data["title"]},{real_data["time"]},' \
        f'{real_data["industry"]},{real_data["location"]},{real_data["tag"]},{real_data["brief"]},' \
        f'{qr_group_name},{real_data["account_master"]},{qr_master_name}\n'

    # 写文件
    with open('./data/data.csv', 'a', encoding='utf-8') as f:
        f.write(line)


if __name__ == '__main__':
    start()
    # print(craw_detail({'url': 'http://www.qunfenxiang.net/group/12779.html'}))
