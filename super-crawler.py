import requests, re
from bs4 import BeautifulSoup

from util import config_util, history_util
from util import time_util, file_util
from util.image_util import download_img, next_img_name

config = None
history = None
data_path = None
img_dir = None
crawler_name = None
url_array = []


def start(name):
    global config, history, data_path, img_dir, crawler_name, url_array

    crawler_name = name
    config = config_util.load_config(name=crawler_name)
    history = history_util.load(name=crawler_name)
    if config is None:
        print(f'no config for {crawler_name}, program exit')
        return
    if history is None:
        history = {}

    storage = config['storage']
    base_dir = storage['base_dir']
    time_str = time_util.today_date_str()
    base_dir = f'{base_dir}/{time_str}'
    data_name = storage['data_name']
    data_path = f'{base_dir}/{data_name}'
    img_dir = storage['img_dir']
    img_dir = f'{base_dir}/{img_dir}/'

    file_util.create_dirs_if_not_exists(base_dir)
    file_util.create_dirs_if_not_exists(img_dir)
    file_util.remove_file(data_path)

    url_array = [config['start_url']]

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
    item_detail_list = []
    for page_item in page_items:
        last_update = time_util.parse_time_str(page_item['last_update'], time_util.now_time_stamp())
        id = page_item['id']
        if not id in history:
            history[id] = {}
            detail = craw_detail(id, page_item)
        elif history[id]['last_crawler_time'] > last_update:
            detail = craw_detail(id, page_item)
        else:
            detail = history[id]['data']

        item_detail_list.append(detail)
        # 更新时间
        history[id]['last_crawler_time'] = time_util.now_time_stamp()
        # 更新数据
        history[id]['data'] = detail
    for item_detail in item_detail_list:
        restore_data(item_detail)
    history_util.update(crawler_name, history)


# 爬取详情页
def craw_detail(id, page_item):
    url = page_item['url']
    print(f'star crawl detail {url}')
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'lxml')
    # print(soup)
    attrs_cfg = config['detail']['attrs']
    item = {'id': id}
    for attr_cfg in attrs_cfg:
        item[attr_cfg['name']] = extract(soup, attr_cfg)
    return item


# 提取下一页地址
def process_next_page_url(soup):
    cfg = config['next_page']
    next_page_url = extract(soup, cfg)
    if next_page_url is not None and next_page_url != '':
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

    doc = None
    if selector_type == 'css':
        if 'list' in cfg:
            doc = soup.select(selector_val)
        else:
            doc = soup.select_one(selector_val)
    elif selector_type == 'find':
        selector_text = cfg['selector_text']
        if 'list' in cfg:
            doc = soup.find_all(selector_val, text=selector_text)
        else:
            doc = soup.find(selector_val, text=selector_text)
        parent = cfg['parent']
        if parent:
            doc = doc.parent

    if doc is None:
        return None

    if not 'val' in cfg:
        return doc

    result = ''
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

    result = result.replace('\n', '').replace('\r', '')

    if 'val_process' in cfg:
        val_process_cfg = cfg['val_process']
        method = val_process_cfg['method']
        if 'regex' == method:
            regex = val_process_cfg['regex']
            groups = re.findall(regex, result)
            index = val_process_cfg['index']
            if len(groups) > index:
                result = groups[index]
        elif 'split' == method:
            split_char = val_process_cfg['split']
            splits = result.split(split_char)
            index = val_process_cfg['index']
            if len(splits) > index:
                result = splits[index]

    result = result.strip()
    if 'val_prefix' in cfg:
        val_prefix = cfg['val_prefix']
        return val_prefix + result

    return result


def restore_data(data):
    print(f'restore {data}')
    # 下载图片
    qr_group_name = download_img(data["qr_group"], img_dir + next_img_name(img_dir))
    qr_master_name = download_img(data["qr_master"], img_dir + next_img_name(img_dir, type='master'))
    real_data = {}
    # 把值里面所有','换成中文'，',防止影响csv格式，并去除换行
    for k, v in data.items():
        real_data[k] = v.replace(',', '，').replace('\n', '').replace('\r', '')

    # 生成要存入csv的字符串
    # 编号,群标题,发布时间,行业,地区,标签,群简介,群二维码图片,群主微信号,群主二维码
    line = f'{real_data["id"]},{real_data["title"]},{real_data["time"]},' \
        f'{real_data["industry"]},{real_data["location"]},{real_data["tag"]},{real_data["brief"]},' \
        f'{qr_group_name},{real_data["account_master"]},{qr_master_name}'

    # 写文件
    file_util.append_line(data_path, line)


if __name__ == '__main__':
    # start(name='qunfenxiang')
    start(name='weixinqun')
