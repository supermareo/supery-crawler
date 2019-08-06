# coding=utf-8
import base64
import os
import requests
import qrcode
from io import BytesIO

from util.file_util import write_bytes
from util.time_util import today_date_str
from util.proxy_util import get_html


# 下载图片
# url - 图片地址
# path - 存储路径
# 返回文件名称
# 如果下载出错，返回空字符串
def download_img(url, path, proxy):
    if len(url) == 0:
        return ''
    if url.startswith('qrtext-'):
        url = url.replace('qrtext-', '')
        return generate_qr_code(url, path)
    # base64的图片
    if url.startswith('data:image/png;base64,'):
        url = url.replace('data:image/png;base64,', '')
        return base64_img(url, path)
    try:
        response = get(url, proxy)
        print(response.text)
        write_bytes(path, response.content)
        return path.split('/')[-1]
    except:
        print(f'download image {url} error')
        return ''


def base64_img(base64str, path):
    try:
        base64str = base64str.replace('data:image/png;base64,', '')
        data = base64.b64decode(base64str)
        write_bytes(path, data)
        return path.split('/')[-1]
    except:
        print(f'download image {base64str} error')
        return ''


# 生成二维码，返回base64字符串
def generate_qr_code(text, path):
    img = qrcode.make(text)
    output_buffer = BytesIO()
    img.save(output_buffer, format='png')
    byte_data = output_buffer.getvalue()
    write_bytes(path, byte_data)
    return path.split('/')[-1]


# 获取下一个文件名
# type - group表示群,master表示群主
def next_img_name(img_path, type='group'):
    # 呼气
    date_str = today_date_str()
    files = os.listdir(img_path)
    if type == 'group':
        count = len(list(filter(lambda x: (date_str + 'A' not in x and date_str in x), files)))
        return f'{date_str}{count + 1}.png'
    else:
        count = len(list(filter(lambda x: (date_str + 'A') in x, files)))
        return f'{date_str}A{count + 1}.png'


def get(url, use_proxy):
    if not use_proxy:
        return requests.get(url, verify=False)
    return get_html(url)


# if __name__ == '__main__':
#     download_img('http://www.jinnianduoda.com/d/file/2018-08-10/ac8968b69ce04d2564ddc8faf01ab857.jpg','abc.jpg')


# if __name__ == '__main__':
#     print(generate_qr_code('http://www.baidu.com'))

if __name__ == '__main__':
    download_img('http://www.jinnianduoda.com/d/file/2019-08-04/ab7ca17caf63240683a3fd36bbd95060.jpeg', 'test.jpeg',
                 True)
