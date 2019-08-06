import requests


def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").text


def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))


def get_html(url):
    retry_count = 5
    while retry_count > 0:
        proxy = get_proxy()
        print(f'proxy {proxy} crawl {url} {5 - retry_count} times')
        try:
            return requests.get(url, proxies={"http": "http://{}".format(proxy)}, verify=False, timeout=10)
        except Exception:
            retry_count -= 1
    return None

# if __name__ == '__main__':
#     response = get_html('http://www.jinnianduoda.com/adgroup/')
#     if response is None:
#         print('fail')
#     else:
#         print(response.text)
