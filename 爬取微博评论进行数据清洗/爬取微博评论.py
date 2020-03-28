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
import jieba
from wordcloud import WordCloud
import  numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt
# 要爬取热评的起始url
url = 'https://m.weibo.cn/comments/hotflow?id=4455529256335361&mid=4455529256335361&max_id='
headers = {
    'Cookie': '',#你的coolie
    'Referer': 'https://m.weibo.cn/detail/4455529256335361',
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
path = os.getcwd() + "./Data/微博评论数据.csv"#
csvfile = open(path, 'w',newline='',encoding = 'utf-8')
writer = csv.writer(csvfile)
maxpage =17 #爬取的数量
m_id = 0
id_type = 0
for page in range(0, maxpage):
    print(page)
    jsondata = get_page(m_id, id_type)
    write_csv(jsondata)
    results = parse_page(jsondata)
    time.sleep(2)
    m_id = results['max_id']
    id_type = results['max_id_type']

