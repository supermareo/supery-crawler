import requests
from bs4 import BeautifulSoup

from util import config_util
from util.image_util import download_img, next_img_name

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


# 提取下一页地址
def process_next_page_url(soup):
    cfg = config['next_page']
    next_page_url = extract(soup, cfg)
    if next_page_url is not None:
        url_array.append(next_page_url)


# 提取页面待处理列表元素，返回一个列表
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
    return items


# 提取逻辑，这段应该是最复杂的
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


def restore_data(data):
    print(f'restore {data}')
    # 下载图片
    img_path = config['storage']['img_path']
    qr_group_name = download_img(data["qr_group"], img_path + next_img_name(img_path))
    qr_master_name = download_img(data["qr_master"], img_path + next_img_name(img_path, type='master'))
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
    data_path = config['storage']['data_path']
    with open(data_path, 'a', encoding='utf-8') as f:
        f.write(line)


if __name__ == '__main__':
    start()
