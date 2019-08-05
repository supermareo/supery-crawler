import re

import requests
from bs4 import BeautifulSoup

from util import config_util, history_util
from util import time_util, file_util
from util.image_util import download_img, next_img_name

# 忽略warning日志
requests.packages.urllib3.disable_warnings()

config = None
history = None
data_path = None
img_dir = None
crawler_name = None
url_array = []
# 默认编码是utf-8，有的网站是gbk
encoding = 'utf-8'
# 跳过部分网页
detail_skip = []

callback = None

progress_page = 0
progress_details = 0
progress_detail_save = 0


def call_callback(callback_method, arg):
    if callback_method is not None:
        callback_method(arg)


def start(name, callback_method):
    global config, history, data_path, img_dir, crawler_name, url_array, encoding, detail_skip, callback, progress_page, progress_details, progress_detail_save
    progress_page = 1
    progress_details = 1
    progress_detail_save = 1
    callback = callback_method

    crawler_name = name
    config = config_util.load_config(name=crawler_name)
    history = history_util.load(name=crawler_name)
    if config is None:
        call_callback(callback, f'找不到{crawler_name}对应的配置信息，无法继续')
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
    if 'encoding' in config:
        encoding = config['encoding']
    if 'skip' in config['detail']:
        detail_skip = config['detail']['skip']

    file_util.create_dirs_if_not_exists(base_dir)
    file_util.create_dirs_if_not_exists(img_dir)
    file_util.remove_file(data_path)
    file_util.append_line(data_path, '编号,群标题,发布时间,行业,地区,标签,群简介,群二维码图片,群主微信号,群主二维码')

    url_array = [config['start_url']]

    while len(url_array) > 0:
        url = url_array.pop(0)
        craw_list(url)


def crawler_list_page(url):
    response = requests.get(url, verify=False)
    response.encoding = encoding
    html = response.text
    soup = BeautifulSoup(html, 'lxml')

    # 提取下一页的url
    cfg = config['next_page']
    next_page_url = extract(soup, cfg)
    next_page_url = None if next_page_url is '' else next_page_url
    # 提取本页列表每一项
    page_items = process_page_items(soup)

    # 返回下一页url与本页列表每一项数据
    return next_page_url, page_items


def craw_list(url):
    print(f'start crawl {url}')
    global progress_page, progress_details, progress_detail_save

    call_callback(callback, f'正在采集第{progress_page}页数据')
    next_page_url, page_items = crawler_list_page(url)
    call_callback(callback, f'完成采集第{progress_page}页数据')
    if next_page_url is not None:
        url_array.append(next_page_url)

    # 提取详情
    item_detail_list = []
    for page_item in page_items:
        call_callback(callback, f'正在采集第{progress_page}页，第{progress_details}项数据')
        # 忽略部分特殊的页面
        url = page_item['url']
        if url in detail_skip:
            continue

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
        call_callback(callback, f'完成采集第{progress_page}页，第{progress_details}项数据')
        progress_details += 1

    for item_detail in item_detail_list:
        call_callback(callback, f'正在存储第{progress_page}页，第{progress_detail_save}项数据')
        restore_data(item_detail)
        call_callback(callback, f'完成存储第{progress_page}页，第{progress_detail_save}项数据')
        progress_detail_save += 1

    history_util.update(crawler_name, history)
    progress_page += 1


# 爬取详情页
def craw_detail(id, page_item):
    url = page_item['url']
    print(f'start crawl detail {url}')
    # call_callback(callback, f'start crawl detail {url}')
    response = requests.get(url, verify=False)
    response.encoding = encoding
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
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
    if selector_type == '':
        return ''

    selector_val = cfg['selector_val']

    doc = None
    if selector_type == 'css':
        if '' == selector_val:
            doc = soup
        else:
            if 'list' in cfg:
                doc = soup.select(selector_val)
            else:
                doc = soup.select_one(selector_val)
        if doc is None:
            if 'backup' in cfg:
                return extract(soup, cfg['backup'])

    elif selector_type == 'find':
        if 'find_type' in cfg:
            find_type = cfg['find_type']
        else:
            find_type = 'text'

        selector_text = cfg['selector_text']
        if 'list' in cfg:
            if find_type == 'text':
                doc = soup.find_all(selector_val, text=selector_text)
            else:
                doc = soup.find_all(selector_val, attrs={find_type: selector_text})
        else:
            if find_type == 'text':
                doc = soup.find(selector_val, text=selector_text)
            else:
                doc = soup.find(selector_val, attrs={find_type: selector_text})

        if doc is None:
            if 'backup' in cfg:
                return extract(soup, cfg['backup'])
            return ''

        if 'parent' not in cfg:
            parent = False
        else:
            parent = cfg['parent']

        if parent:
            doc = doc.parent

    if doc is None:
        return ''

    if 'val' not in cfg:
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
        if not result.startswith(val_prefix):
            return val_prefix + result

    return result


def restore_data(data):
    print(f'restore {data}')
    # call_callback(callback, f'restore {data}')
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

# if __name__ == '__main__':
#     # start(name='qunfenxiang')
#     # start(name='weixinqun')
#     # start(name='qianwanqun')
#     # start(name='weixin28_qun')
#     # start(name='weixin28_hong')
#     # start(name='weixinfabu')
#     # start(name='jam9')
#     # start(name='souweixin')
#     # start(name='haoweixin')
#     # start(name='vhujia')
#     start(name='wekui')
