# coding=utf-8
import requests


# 下载图片
def download_img(url, path):
    try:
        response = requests.get(url)
        with open(path, 'wb') as f:
            f.write(response.content)
        return path.split('/')[-1]
    except:
        print(f'download image {url} error')
        return ''
