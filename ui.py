# coding=utf-8


import threading
import tkinter as tk
from tkinter import ttk

import supercrawler

website_zh_en_map = {
    '群分享': 'qunfenxiang',
    '微信群创业者': 'weixinqun',
    '千万群': 'qianwanqun',
    '微信28-群': 'weixin28_qun',
    '微信28-红福群': 'weixin28_hong',
    '微信群发布平台': 'weixinfabu',
    'jam9微信群': 'jam9',
    '搜微': 'souweixin',
    '好微信': 'haoweixin',
    '微互加': 'vhujia',
    '微魁网': 'wekui'
}
website_zh_list = list(website_zh_en_map.keys())

win = tk.Tk()
win.title("微信群采集")  # 添加标题
ttk.Label(win, width=16, text="选择要采集的站点：").grid(column=0, row=0)  # 添加一个标签，并将其列设置为1，行设置为0


def click_me():
    action.config(state=tk.DISABLED)
    print(f'开始爬取 - {website_chosen.get()}-{selected_website}')
    t = threading.Thread(target=supercrawler.start, args=(selected_website, callback), name='thread-crawling')
    t.setDaemon(True)
    t.start()


def callback(line):
    log.set(line)


action = ttk.Button(win, width=10, text="开始采集", command=click_me)
action.grid(column=2, row=0)


def combobox_selected(event):
    global selected_website
    selected_website = website_zh_en_map[website_chosen.get()]


# 创建一个下拉列表
website_chosen = ttk.Combobox(win, width=18, state='readonly', values=website_zh_list)
website_chosen.grid(column=1, row=0)
website_chosen.current(0)
selected_website = website_zh_en_map[website_zh_list[0]]

# 绑定时间
website_chosen.bind('<<ComboboxSelected>>', combobox_selected)

log = tk.StringVar()
ttk.Label(win, width=50, textvariable=log).grid(column=0, row=1, columnspan=3)

win.mainloop()  # 当调用mainloop()时,窗口才会显示出来
