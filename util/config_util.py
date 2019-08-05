# coding=utf-8

config_dict = {
    "qunfenxiang": {
        "start_url": "http://www.qunfenxiang.net/group/",
        "next_page": {
            "selector_type": "css",
            "selector_val": "a.pageNext",
            "val": "href",
            "val_prefix": "http://www.qunfenxiang.net"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.boldBorder",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/group/(\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_prefix": "http://www.qunfenxiang.net"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "title"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "div.f12.c888",
                    "val": "stripped-0"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.code_info>h1",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "时间：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "industry",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "行业：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "location",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "地区：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "tag",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "标签：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "div.page_con > div:nth-child(4) > p.pt20",
                    "val": "text"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.code_pic > span:nth-child(2) > div > p > img",
                    "val": "src"
                },
                {
                    "name": "qr_master",
                    "selector_type": "css",
                    "selector_val": "div.code_pic > span:nth-child(3) > div > p > img",
                    "val": "src"
                },
                {
                    "name": "account_master",
                    "selector_type": "css",
                    "selector_val": "div.green_bg>p",
                    "val": "stripped-1"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/qunfenxiang",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "weixinqun": {
        "start_url": "https://weixinqun.com/group",
        "next_page": {
            "selector_type": "css",
            "selector_val": "a.pageNext",
            "val": "href",
            "val_prefix": "https://weixinqun.com"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.border5",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/group\\?id=(\\d+)",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_prefix": "https://weixinqun.com"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "p.goods_name>a",
                    "val": "title"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "p.wxNum",
                    "val": "stripped-[0,1,None]"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "span.des_info_text>b",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "css",
                    "selector_val": "ul.other-info>li:nth-child(3)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "industry",
                    "selector_type": "css",
                    "selector_val": "ul.other-info>li:nth-child(1)",
                    "val": "stripped-1"
                },
                {
                    "name": "location",
                    "selector_type": "css",
                    "selector_val": "ul.other-info>li:nth-child(2)",
                    "val": "stripped-1"
                },
                {
                    "name": "tag",
                    "selector_type": "css",
                    "selector_val": "ul.other-info>li:nth-child(4)",
                    "val": "stripped-1"
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "div.des_info > div.clearfix > ul > li:nth-child(3) > span",
                    "val": "text"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "span.shiftcode:nth-child(2)>img",
                    "val": "src"
                },
                {
                    "name": "qr_master",
                    "selector_type": "css",
                    "selector_val": "span.shiftcode:nth-child(3)>img",
                    "val": "src"
                },
                {
                    "name": "account_master",
                    "selector_type": "css",
                    "selector_val": "span.des_info_text2:nth-child(2)",
                    "val": "text"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/weixinqun",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "qianwanqun": {
        "start_url": "http://www.qianwanqun.com/weixinqun/",
        "next_page": {
            "selector_type": "find",
            "selector_val": "a",
            "selector_text": "下一页",
            "parent": False,
            "val": "href",
            "val_prefix": "http://www.qianwanqun.com/weixinqun/"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.p_list_wxq>ul>a",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/weixinqun/show-(\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "",
                    "val": "href",
                    "val_prefix": "http://www.qianwanqun.com"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "li>div.l2",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "li>div.l3",
                    "val": "stripped-0"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.r1",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "css",
                    "selector_val": "div.r2 > li:nth-child(6)",
                    "val": "stripped-1"
                },
                {
                    "name": "industry",
                    "selector_type": "css",
                    "selector_val": "div.r2 > li:nth-child(4)",
                    "val": "stripped-1"
                },
                {
                    "name": "location",
                    "selector_type": "css",
                    "selector_val": "div.r2 > li:nth-child(5)",
                    "val": "stripped-1"
                },
                {
                    "name": "tag",
                    "selector_type": "css",
                    "selector_val": "div.r2 > li:nth-child(4)",
                    "val": "stripped-1"
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "div.ql > div:nth-child(4)",
                    "val": "text"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.cl",
                    "val": "style",
                    "val_process": {
                        "method": "regex",
                        "regex": "url\\(([0-9a-zA-Z/_.]+)\\)",
                        "index": 0
                    },
                    "val_prefix": "http://www.qianwanqun.com"
                },
                {
                    "name": "qr_master",
                    "selector_type": "",
                    "selector_val": ""
                },
                {
                    "name": "account_master",
                    "selector_type": "find",
                    "selector_val": "b",
                    "selector_text": "群主微信：",
                    "parent": True,
                    "val": "stripped-1"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/qianwanqun",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "weixin28_qun": {
        "start_url": "http://www.weixin28.com/qun/",
        "next_page": {
            "selector_type": "find",
            "selector_val": "a",
            "selector_text": "下一页",
            "parent": False,
            "val": "href",
            "val_prefix": "http://www.weixin28.com"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.hover-border",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/qun/[a-zA-Z]*/(\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_prefix": "http://www.weixin28.com"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "p.title>a",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "span.fr",
                    "val": "text"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "h1.title",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "css",
                    "selector_val": "div.intro-box > ul > li:nth-child(4)",
                    "val": "stripped-2"
                },
                {
                    "name": "industry",
                    "selector_type": "css",
                    "selector_val": "div.intro-box > ul > li:nth-child(2)",
                    "val": "stripped-2"
                },
                {
                    "name": "location",
                    "selector_type": "css",
                    "selector_val": "div.intro-box > ul > li:nth-child(7)>span.lx",
                    "val": "text"
                },
                {
                    "name": "tag",
                    "selector_type": "css",
                    "selector_val": "span.tags>a",
                    "val": "text"
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "div.detail-box",
                    "val": "text"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.img>img:nth-child(1)",
                    "val": "src"
                },
                {
                    "name": "qr_master",
                    "selector_type": "css",
                    "selector_val": "div.img>img:nth-child(2)",
                    "val": "src"
                },
                {
                    "name": "account_master",
                    "selector_type": "css",
                    "selector_val": "span.f20",
                    "val": "text"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/weixin28_qun",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "weixin28_hong": {
        "start_url": "http://www.weixin28.com/hong/",
        "next_page": {
            "selector_type": "find",
            "selector_val": "a",
            "selector_text": "下一页",
            "parent": False,
            "val": "href",
            "val_prefix": "http://www.weixin28.com"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.hover-border",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/hong/[a-zA-Z]*/(\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_prefix": "http://www.weixin28.com"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "p.title>a",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "span.fr",
                    "val": "text"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "h1.title",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "css",
                    "selector_val": "div.intro-box > ul > li:nth-child(4)",
                    "val": "stripped-2"
                },
                {
                    "name": "industry",
                    "selector_type": "css",
                    "selector_val": "div.intro-box > ul > li:nth-child(2)",
                    "val": "stripped-2"
                },
                {
                    "name": "location",
                    "selector_type": "css",
                    "selector_val": "div.intro-box > ul > li:nth-child(7)>span.lx",
                    "val": "text"
                },
                {
                    "name": "tag",
                    "selector_type": "css",
                    "selector_val": "span.tags>a",
                    "val": "text"
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "div.detail-box",
                    "val": "text"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.img>img:nth-child(1)",
                    "val": "src"
                },
                {
                    "name": "qr_master",
                    "selector_type": "css",
                    "selector_val": "div.img>img:nth-child(2)",
                    "val": "src"
                },
                {
                    "name": "account_master",
                    "selector_type": "css",
                    "selector_val": "span.f20",
                    "val": "text"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/weixin28_hong",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "weixinfabu": {
        "start_url": "https://www.weixinfabu.com/group/",
        "next_page": {
            "selector_type": "find",
            "selector_val": "a",
            "find_type": "title",
            "selector_text": "下一页",
            "parent": False,
            "val": "href",
            "val_prefix": "https://www.weixinfabu.com"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.border5",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "group_show/(\\d+)/",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "p.goods_name>a",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "span.caaa",
                    "val": "text"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "span.des_info_text>b",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "css",
                    "selector_val": "ul.other-info > li:nth-child(2)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "industry",
                    "selector_type": "css",
                    "selector_val": "ul.other-info > li:nth-child(1)>a",
                    "val": "text"
                },
                {
                    "name": "location",
                    "selector_type": "css",
                    "selector_val": "ul.other-info > li:nth-child(3)>a",
                    "val": "text"
                },
                {
                    "name": "tag",
                    "selector_type": "css",
                    "selector_val": "li.tag>a",
                    "val": "text"
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "span.des_info_text2>pre",
                    "val": "text"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.iframe > span:nth-child(2)>img",
                    "val": "src",
                    "val_prefix": "https://www.weixinfabu.com"
                },
                {
                    "name": "qr_master",
                    "selector_type": "css",
                    "selector_val": "div.iframe > span:nth-child(3)>img",
                    "val": "src",
                    "val_prefix": "https://www.weixinfabu.com"
                },
                {
                    "name": "account_master",
                    "selector_type": "css",
                    "selector_val": "ul.other-info > li:nth-child(6)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                }
            ]
        },
        "storage": {
            "base_dir": "./data/weixinfabu",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "jam9": {
        "start_url": "https://www.jam9.cc/weixinqun/index.html",
        "next_page": {
            "selector_type": "find",
            "selector_val": "a",
            "selector_text": "下一页",
            "parent": False,
            "val": "href",
            "val_prefix": "https://www.jam9.cc"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.uk-container>ul.uk-grid>li",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/weixinqun/[a-zA-Z]*/(\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_prefix": "https://www.jam9.cc"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.uk-text-meta.mp10",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "div.uk-width-1-2.uk-text-meta",
                    "val": "text"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "h1.hbt",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "css",
                    "selector_val": "ul.uk-list > li:nth-child(4)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "industry",
                    "selector_type": "css",
                    "selector_val": "ul.uk-list > li:nth-child(2)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "location",
                    "selector_type": "css",
                    "selector_val": "ul.uk-list > li:nth-child(3)>div>code",
                    "val": "text"
                },
                {
                    "name": "tag",
                    "selector_type": "css",
                    "selector_val": "ul.uk-list > li:nth-child(2)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "#text",
                    "val": "stripped-0"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.jam-imgp>img",
                    "val": "src"
                },
                {
                    "name": "qr_master",
                    "selector_type": "",
                    "selector_val": ""
                },
                {
                    "name": "account_master",
                    "selector_type": "css",
                    "selector_val": "ul.uk-list > li:nth-child(1)>span>code",
                    "val": "text"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/jam9",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "souweixin": {
        "start_url": "https://www.souweixin.com/group",
        "next_page": {
            "selector_type": "find",
            "selector_val": "a",
            "find_type": "title",
            "selector_text": "下一页",
            "parent": False,
            "val": "href",
            "val_prefix": "https://www.souweixin.com"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.boldBorder",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/group\\?id=(\\d+)",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_prefix": "https://www.souweixin.com"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.lg_txt",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "div.f12.c888",
                    "val": "stripped-[0,1,None]"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.code_info>h1",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "时间：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "industry",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "行业：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "location",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "地区：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "tag",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "标签：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "brief",
                    "selector_type": "",
                    "selector_val": ""
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.code_pic>div.p1>p>img",
                    "val": "src"
                },
                {
                    "name": "qr_master",
                    "selector_type": "",
                    "selector_val": ""
                },
                {
                    "name": "account_master",
                    "selector_type": "css",
                    "selector_val": "div.green_bg>p:nth-child(1)>span",
                    "val": "text"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/souweixin",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "haoweixin": {
        "start_url": "http://www.haoweixin.net/group/",
        "next_page": {
            "selector_type": "css",
            "selector_val": "a.pageNext",
            "val": "href",
            "val_prefix": "http://www.haoweixin.net"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.boldBorder",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/group/(\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_prefix": "http://www.haoweixin.net"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.lg_intro",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "div.f12.c888",
                    "val": "stripped-[0,1,None]"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.code_info>h1",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "时间：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "industry",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "行业：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "location",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "地区：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "tag",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "标签：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "div.code_info>p.f18",
                    "val": "text"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.code_pic > span:nth-child(2) > div > p:nth-child(1) > img",
                    "val": "src",
                    "val_prefix": "http://www.haoweixin.net"
                },
                {
                    "name": "qr_master",
                    "selector_type": "css",
                    "selector_val": "div.code_pic > span:nth-child(3) > div > p:nth-child(1) > img",
                    "val": "src",
                    "val_prefix": "http://www.haoweixin.net"
                },
                {
                    "name": "account_master",
                    "selector_type": "css",
                    "selector_val": "div.green_bg>p:nth-child(1)>span",
                    "val": "text"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/haoweixin",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "vhujia": {
        "start_url": "https://www.vhujia.com/weixin/index/p/1.html",
        "next_page": {
            "selector_type": "find",
            "selector_val": "a",
            "selector_text": "下一页",
            "parent": False,
            "val": "href",
            "val_prefix": "https://www.vhujia.com"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "li>dl",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "dt>a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/weixin/show/id/(\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "dt>a",
                    "val": "href",
                    "val_prefix": "https://www.vhujia.com"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "dd.tit>a>b",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "",
                    "selector_val": ""
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.viewm>h1",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "发布时间：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "industry",
                    "selector_type": "css",
                    "selector_val": "div.viewm > div > ul > li:nth-child(6) > span",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "location",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "所属地区：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "tag",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "标签：",
                    "parent": True,
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "div.content>p",
                    "val": "text"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.viewm>div>div>img",
                    "val": "src",
                    "val_prefix": "https://www.vhujia.com"
                },
                {
                    "name": "qr_master",
                    "selector_type": "",
                    "selector_val": ""
                },
                {
                    "name": "account_master",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "微信号：",
                    "parent": True,
                    "val": "stripped-1"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/vhujia",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "wekui": {
        "start_url": "https://www.wekui.com/html/41/",
        "encoding": "gbk",
        "next_page": {
            "selector_type": "find",
            "selector_val": "a",
            "selector_text": "下一页",
            "parent": False,
            "val": "href"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.border5",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "https://www.wekui.com/html/.*/(\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "p.goods_name>a",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "span.caaa",
                    "val": "text"
                }
            ]
        },
        "detail": {
            "skip": [
                "https://www.wekui.com/html/52-34/34468.html"
            ],
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "span.des_info_text>b",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "css",
                    "selector_val": "ul.other-info>li:nth-child(2)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "industry",
                    "selector_type": "css",
                    "selector_val": "ul.other-info>li:nth-child(1)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "location",
                    "selector_type": "css",
                    "selector_val": "ul.other-info>li:nth-child(3)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "tag",
                    "selector_type": "css",
                    "selector_val": "ul.other-info>li:nth-child(4)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "span.des_info_text2:nth-child(1)",
                    "val": "text"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "span.shiftcode:nth-child(4) > img",
                    "val": "src"
                },
                {
                    "name": "qr_master",
                    "selector_type": "css",
                    "selector_val": "span.shiftcode:nth-child(3) > img",
                    "val": "src"
                },
                {
                    "name": "account_master",
                    "selector_type": "css",
                    "selector_val": "span.des_info_text2:nth-child(2)",
                    "val": "text"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/wekui",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "qun68": {
        "start_url": "http://qun68.com/group/",
        "next_page": {
            "selector_type": "find",
            "selector_val": "a",
            "find_type": "title",
            "selector_text": "下一页",
            "parent": False,
            "val": "href",
            "val_prefix": "http://qun68.com"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.border5",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/group/(\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_prefix": "http://qun68.com"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "title"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "p.wxNum",
                    "val": "stripped-[0,1,None]"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "span.des_info_text>b",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "css",
                    "selector_val": "ul.other-info>li:nth-child(2)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "industry",
                    "selector_type": "css",
                    "selector_val": "ul.other-info>li:nth-child(1)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "location",
                    "selector_type": "css",
                    "selector_val": "ul.other-info>li:nth-child(3)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "tag",
                    "selector_type": "css",
                    "selector_val": "ul.other-info>li:nth-child(4)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "span.des_info_text2:nth-child(1)",
                    "val": "text"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "span.shiftcode:nth-child(2) > img",
                    "val": "src",
                    "val_prefix": "http://qun68.com"
                },
                {
                    "name": "qr_master",
                    "selector_type": "css",
                    "selector_val": "span.shiftcode:nth-child(3) > img",
                    "val": "src",
                    "val_prefix": "http://qun68.com"
                },
                {
                    "name": "account_master",
                    "selector_type": "css",
                    "selector_val": "span.des_info_text2:nth-child(2)",
                    "val": "text"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/qun68",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "nihaoweixin": {
        "start_url": "https://www.nihaoweixin.com/group/",
        "next_page": {
            "selector_type": "css",
            "selector_val": "a.pageNext",
            "val": "href",
            "val_prefix": "https://www.nihaoweixin.com"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.boldBorder",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/group/(\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_prefix": "https://www.nihaoweixin.com"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.lg_intro",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "div.f12.c888",
                    "val": "stripped-[0,1,None]"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.code_info>h1",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "时间：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "industry",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "行业：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "location",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "地区：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "tag",
                    "selector_type": "find",
                    "selector_val": "span",
                    "selector_text": "标签：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "div.code_info>p.f18",
                    "val": "text"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.code_pic > span:nth-child(2) > div > p:nth-child(1) > img",
                    "val": "src",
                    "val_prefix": "http://www.nihaoweixin.com"
                },
                {
                    "name": "qr_master",
                    "selector_type": "css",
                    "selector_val": "div.code_pic > span:nth-child(3) > div > p:nth-child(1) > img",
                    "val": "src",
                    "val_prefix": "http://www.nihaoweixin.com"
                },
                {
                    "name": "account_master",
                    "selector_type": "css",
                    "selector_val": "div.green_bg>p:nth-child(1)>span",
                    "val": "text"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/nihaoweixin",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "wxqun": {
        "start_url": "http://www.wxqun.com/wxq",
        "next_page": {
            "selector_type": "css",
            "selector_val": "li.next>a",
            "val": "href",
            "val_prefix": "http://www.wxqun.com"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.show>ul>li>div",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "http://www.wxqun.com/wxq/(\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "href"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "a",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "div.show > ul > li > div > p:nth-child(2) > span:nth-child(1)",
                    "val": "text"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.con_info>h1",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "css",
                    "selector_val": "div.con_info>ul>li:nth-child(2)",
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "industry",
                    "selector_type": "css",
                    "selector_val": "div.con_info>ul>li:nth-child(1)>a",
                    "val": "text"
                },
                {
                    "name": "location",
                    "selector_type": "css",
                    "selector_val": "div.con_info>ul>li:nth-child(3)>a",
                    "val": "text"
                },
                {
                    "name": "tag",
                    "selector_type": "css",
                    "selector_val": "div.con_info>ul>li:nth-child(4)>span",
                    "val": "text"
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "div.con_info > p:nth-child(3) > span:nth-child(2)",
                    "val": "text"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.con_img > p > span:nth-child(1) > img",
                    "val": "src"
                },
                {
                    "name": "qr_master",
                    "selector_type": "css",
                    "selector_val": "div.con_img > p > span:nth-child(2) > img",
                    "val": "src"
                },
                {
                    "name": "account_master",
                    "selector_type": "css",
                    "selector_val": "div.con_info > p:nth-child(5)>span",
                    "val": "text"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/wxqun",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "gpwxq": {
        "start_url": "http://www.gpwxq.com/weixin-index-id-44.html",
        "next_page": {
            "selector_type": "find",
            "selector_val": "a",
            "selector_text": "下一页",
            "val": "href",
            "val_prefix": "http://www.gpwxq.com"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.qun-content>ul>li",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "div.dt>a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/weixin-show-id-(\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "div.dt>a",
                    "val": "href",
                    "val_prefix": "http://www.gpwxq.com"

                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.db>p.p1>a",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "div.db>p.p2>span.fLeft>font.fs",
                    "val": "text"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.box1>h4",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "find",
                    "selector_val": "strong",
                    "selector_text": "发布时间：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "industry",
                    "selector_type": "css",
                    "selector_val": "span.b_nav>a:nth-child(3)",
                    "val": "text"
                },
                {
                    "name": "location",
                    "selector_type": "find",
                    "selector_val": "strong",
                    "selector_text": "地区：",
                    "parent": True,
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "tag",
                    "selector_type": "css",
                    "selector_val": "span.b_nav>a:nth-child(3)",
                    "val": "text"
                },
                {
                    "name": "brief",
                    "selector_type": "find",
                    "selector_val": "strong",
                    "selector_text": "简介：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.fLeft.b1 > p:nth-child(1) > img",
                    "val": "src",
                    "val_prefix": "http://www.gpwxq.com"
                },
                {
                    "name": "qr_master",
                    "selector_type": ""
                },
                {
                    "name": "account_master",
                    "selector_type": "find",
                    "selector_val": "strong",
                    "selector_text": "微信号：",
                    "parent": True,
                    "val": "stripped-1"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/gpwxq",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "weixinqn": {
        "start_url": "http://www.weixinqn.com/weixin-index-id-44.html",
        "next_page": {
            "selector_type": "find",
            "selector_val": "a",
            "selector_text": "下一页",
            "val": "href",
            "val_prefix": "http://www.weixinqn.com"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "ul.w1000>li",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "div.dt>a",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/weixin-show-id-(\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "div.dt>a",
                    "val": "href",
                    "val_prefix": "http://www.weixinqn.com"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.db>p.p1>a",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "div.db>p.p2>span.fLeft>font.fs",
                    "val": "text"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.box1>h1",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "find",
                    "selector_val": "strong",
                    "selector_text": "发布时间：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "industry",
                    "selector_type": "css",
                    "selector_val": "span.b_nav>a:nth-child(2)",
                    "val": "text"
                },
                {
                    "name": "location",
                    "selector_type": "find",
                    "selector_val": "strong",
                    "selector_text": "地区：",
                    "parent": True,
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    }
                },
                {
                    "name": "tag",
                    "selector_type": "css",
                    "selector_val": "span.b_nav>a:nth-child(2)",
                    "val": "text"
                },
                {
                    "name": "brief",
                    "selector_type": "find",
                    "selector_val": "strong",
                    "selector_text": "简介：",
                    "parent": True,
                    "val": "stripped-1"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.fLeft.b1 > p:nth-child(1) > img",
                    "val": "src",
                    "val_prefix": "http://www.weixinqn.com/"
                },
                {
                    "name": "qr_master",
                    "selector_type": ""
                },
                {
                    "name": "account_master",
                    "selector_type": "find",
                    "selector_val": "strong",
                    "selector_text": "微信号：",
                    "parent": True,
                    "val": "stripped-1"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/weixinqn",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "sm168": {
        "start_url": "http://sm168.com/list-9-1.html",
        "next_page": {
            "selector_type": "find",
            "selector_val": "a",
            "selector_text": "下一页",
            "val": "href",
            "val_prefix": "http://sm168.com/"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.tools_contentgz > ul > li",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "a.items",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "http://sm168.com/show-(\\d+-\\d+-\\d+).html",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "a.items",
                    "val": "href"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.gz_title>h4",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "span",
                    "val": "text"
                }
            ]
        },
        "detail": {
            "skip": [
                "http://sm168.com/show-69-140407-1.html"
            ],
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.content_r>h1",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "find",
                    "selector_val": "b",
                    "selector_text": "发布时间",
                    "parent": True,
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    },
                    "backup": {
                        "selector_type": "find",
                        "selector_val": "span",
                        "selector_text": "发布时间",
                        "parent": True,
                        "val": "text",
                        "val_process": {
                            "method": "split",
                            "split": "：",
                            "index": 1
                        }
                    }
                },
                {
                    "name": "industry",
                    "selector_type": "find",
                    "selector_val": "b",
                    "selector_text": "所属行业",
                    "parent": True,
                    "val": "stripped-2",
                    "backup": {
                        "selector_type": "find",
                        "selector_val": "span",
                        "selector_text": "所属行业",
                        "parent": True,
                        "val": "stripped-2",
                    }
                },
                {
                    "name": "location",
                    "selector_type": "find",
                    "selector_val": "b",
                    "selector_text": "地区",
                    "parent": True,
                    "val": "stripped-2",
                    "backup": {
                        "selector_type": "find",
                        "selector_val": "span",
                        "selector_text": "地区",
                        "parent": True,
                        "val": "stripped-2",
                    }
                },
                {
                    "name": "tag",
                    "selector_type": ""
                },
                {
                    "name": "brief",
                    "selector_type": "find",
                    "selector_val": "b",
                    "selector_text": "简介",
                    "parent": True,
                    "val": "text",
                    "val_process": {
                        "method": "split",
                        "split": "：",
                        "index": 1
                    },
                    "backup": {
                        "selector_type": "find",
                        "selector_val": "span",
                        "selector_text": "简介",
                        "parent": True,
                        "val": "text",
                        "val_process": {
                            "method": "split",
                            "split": "：",
                            "index": 1
                        }
                    }
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.content_l>img",
                    "val": "src",
                    "val_prefix": "http://sm168.com",
                    "backup": {
                        "selector_type": "css",
                        "selector_val": "div.content_l > p > img",
                        "val": "src",
                        "val_prefix": "http://sm168.com"
                    }
                },
                {
                    "name": "qr_master",
                    "selector_type": ""
                },
                {
                    "name": "account_master",
                    "selector_type": "find",
                    "selector_val": "b",
                    "selector_text": "群主微信号",
                    "parent": True,
                    "val": "stripped-2",
                    "backup": {
                        "selector_type": "find",
                        "selector_val": "span",
                        "selector_text": "群主微信号",
                        "parent": True,
                        "val": "stripped-2",
                    }
                }
            ]
        },
        "storage": {
            "base_dir": "./data/sm168",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    },
    "9877788": {
        "start_url": "https://www.9877788.com/qun",
        "next_page": {
            "selector_type": "css",
            "selector_val": "a.page_next",
            "val": "href",
            "val_prefix": "https://www.9877788.com"
        },
        "items": {
            "selector_type": "css",
            "selector_val": "div.content>a",
            "list": True,
            "attrs": [
                {
                    "name": "id",
                    "selector_type": "css",
                    "selector_val": "",
                    "val": "href",
                    "val_process": {
                        "method": "regex",
                        "regex": "/wx/(\\d+)",
                        "index": 0
                    }
                },
                {
                    "name": "url",
                    "selector_type": "css",
                    "selector_val": "",
                    "val": "href",
                    "val_prefix": "https://www.9877788.com"
                },
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.data>p.ellipsis",
                    "val": "text"
                },
                {
                    "name": "last_update",
                    "selector_type": "css",
                    "selector_val": "div.data>div.position>span.fl",
                    "val": "text"
                }
            ]
        },
        "detail": {
            "attrs": [
                {
                    "name": "title",
                    "selector_type": "css",
                    "selector_val": "div.detail_content>p",
                    "val": "text"
                },
                {
                    "name": "time",
                    "selector_type": "css",
                    "selector_val": "div.cards>span>img",
                    "val": "src",
                    "val_process": {
                        "method": "regex",
                        "regex": "https://img.9877788.com/Uploads/(\\d{4}-\\d{2}-\\d{2})/.*",
                        "index": 0
                    }
                },
                {
                    "name": "industry",
                    "selector_type": "css",
                    "selector_val": "div.information > span:nth-child(2)",
                    "val": "text"
                },
                {
                    "name": "location",
                    "selector_type": "css",
                    "selector_val": "div.information > span:nth-child(1)",
                    "val": "text"
                },
                {
                    "name": "tag",
                    "selector_type": ""
                },
                {
                    "name": "brief",
                    "selector_type": "css",
                    "selector_val": "div.text_detail.first>div.texts",
                    "val": "text"
                },
                {
                    "name": "qr_group",
                    "selector_type": "css",
                    "selector_val": "div.cards>span>img",
                    "val": "src"
                },
                {
                    "name": "qr_master",
                    "selector_type": ""
                },
                {
                    "name": "account_master",
                    "selector_type": "css",
                    "selector_val": "div.text_detail.special>div.texts",
                    "val": "text"
                }
            ]
        },
        "storage": {
            "base_dir": "./data/9877788",
            "data_name": "data.csv",
            "img_dir": "imgs"
        }
    }
}


# 加载配置文件
# path - 默认使用config/super-config.json文件
# name - 指定配置文件中某项，否则返回所有
def load_config(path='config/super-config.json', name=None):
    # json_obj = read_json_obj(path)
    # if name is None:
    #     return json_obj
    # if name not in json_obj:
    #     return None
    # return json_obj[name]
    if name is None:
        return config_dict
    if name not in config_dict:
        return None
    return config_dict[name]
