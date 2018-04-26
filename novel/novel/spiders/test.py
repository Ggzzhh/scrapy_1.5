# -*- coding: utf-8 -*-
import requests

from urllib import parse
from bs4 import BeautifulSoup

# search_url = 'http://www.biquge.com.tw/modules/article/soshu.php?searchkey=+{}'
# search = parse.quote('大王', encoding='gbk')
# res = requests.get(search_url.format(search))
# res.encoding = 'gbk'
# soup = BeautifulSoup(res.text, 'lxml')
# tr = soup.find(id='nr')
# td = tr.find('td')
# print(td.a.get('href'))

# url = 'http://www.biquge.com.tw/17_17380/'
# res = requests.get(url)
# res.encoding = 'gbk'
# soup = BeautifulSoup(res.text, 'lxml')
# info = soup.find(id='info')
# if info:
#     # info_p = info.find_all('p')
#     # print(info.h1.text)
#     # print(info_p[0].text[7:])
#     # print(info_p[-1].a.text)
#     dds = soup.find_all('dd')
#     for dd in dds:
#         url = 'http://www.biquge.com.tw' + dd.a.get('href')
#         print(dd.a.text + ':' + url)

# url = 'https://qdp.qidian.com/qreport?path=pclog&ltype=A&url=https%3A%2F%2Fbook.qidian.com%2Finfo%2F1010565736%23Catalog&ref=https%3A%2F%2Fwww.qidian.com%2Ffree&sw=1920&sh=1080&x=672&y=169&title=%E3%80%8A%E6%B9%BE%E5%8C%BA%E4%B9%8B%E7%8E%8B%E3%80%8B_%E7%A3%A8%E7%A0%9A%E5%B0%91%E5%B9%B4%E8%91%97_%E4%BD%93%E8%82%B2_%E8%B5%B7%E7%82%B9%E4%B8%AD%E6%96%87%E7%BD%91&pid=qd_P_mulu&eid=&bid=&cid=&tid=&rid=&qd_dd_p1=&qd_game_key=&auid=&blid=&algrid=&kw=&isQD=true&cname=QDpclog&l1=3&e1=%7B%22pid%22%3A%22qd_P_mulu%22%2C%22eid%22%3A%22qd_G15%22%2C%22l1%22%3A3%7D&e2=%7B%22pid%22%3A%22qd_P_mulu%22%2C%22eid%22%3A%22qd_G16%22%2C%22l1%22%3A3%7D'
# print(parse.unquote(url))
# url = 'http://www.biquge.com.tw/17_17380/8880626.html'
# res = requests.get(url)
# res.encoding = 'gbk'
# soup = BeautifulSoup(res.text, 'lxml')
# print(soup.find(id='content').text)