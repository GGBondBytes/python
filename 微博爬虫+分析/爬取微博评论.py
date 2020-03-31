# -*- coding: utf-8 -*-
import requests
import time
import os
import csv
import sys
import json
from bs4 import BeautifulSoup
import importlib
importlib.reload(sys)
url = 'https://m.weibo.cn/comments/hotflow?id=***&mid=***&max_id='#将***替换成你要爬的微博id
headers = {
    'Cookie': '***',#将***替换成你的cookie
    'Referer': 'https://m.weibo.cn/detail/***',#将***替换成你要爬的微博id
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

def get_page(max_id, id_type):
    params = {
        'max_id': max_id,
        'max_id_type': id_type
    }
    try:
        r = requests.get(url, params=params, headers=headers)
        if r.status_code == 200:
            return r.json()
    except requests.ConnectionError as e:
        print('error', e.args)


def parse_page(jsondata):
    if jsondata:
        items = jsondata.get('data')
        item_max_id = {}
        item_max_id['max_id'] = items['max_id']
        item_max_id['max_id_type'] = items['max_id_type']
        return item_max_id

def write_csv(jsondata):
    datas = jsondata.get('data').get('data')
    for data in datas:
        comment = data.get("text")
        comment = BeautifulSoup(comment, 'lxml').get_text()
        writer.writerow([json.dumps(comment,  ensure_ascii=False)])

# 存为csv
csvfile = open('./result/微博爬评论.csv', 'w',newline='',encoding = 'utf-8')
writer = csv.writer(csvfile)
maxpage =100 #爬取的页数
m_id = 0
id_type = 0
for page in range(0, maxpage):
    print(page)
    jsondata = get_page(m_id, id_type)
    write_csv(jsondata)
    results = parse_page(jsondata)
    time.sleep(2) #休眠时间，防止被封号
    m_id = results['max_id']
    id_type = results['max_id_type']
