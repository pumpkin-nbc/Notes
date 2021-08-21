# -*- coding: utf-8 -*-
# @Author  : Pumpkin
# @Time    : 2021/8/21 18:00
# @Software: PyCharm
# @File    : demo_1.py
# @Mail    : a760329881@qq.com
import random

import THS_Tools.THS_HK_General_Tools.General_Tools as Tgs

# https://dushu.baidu.com/api/pc/getCatalog
# data: {"book_id":"4306063500"}
# https://dushu.baidu.com/api/pc/getChapterContent
# data: {"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}

import requests
import json

proxy, headers = Tgs.proxy_ths()
url = 'https://dushu.baidu.com/api/pc/getCatalog'
params = {"data": '{"book_id":"4306063500"}'}

a = requests.get(url=url, params=params,
                 headers={"User-Agent": random.choice(headers)},
                 proxies={'http': random.choice(proxy)})
a.close()
a = a.json()['data']['novel']['items']
for i in a:
    title = i['title']
    cid = i['cid']
    print(title)
    print(cid)
# print(json.dumps(a, indent=4, ensure_ascii=False))
# url = 'https://dushu.baidu.com/api/pc/getChapterContent'
# params = {"data": '{"book_id":"4306063500","cid":"4306063500|11348571","need_bookinfo":1}'}
# a = requests.get(url=url, params=params, headers={"User-Agent": random.choice(headers)},
#                  proxies={'http': random.choice(proxy)})
# a.close()
# a.encoding = 'UTF-8'
# b = a.json()['data']['novel']['content']
# print(b.replace('\n',''))
