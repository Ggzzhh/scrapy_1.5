# -*- coding: utf-8 -*-
import scrapy
import re
import hashlib
from datetime import datetime
from ..items import NovelItem, ChapterItem
from urllib.parse import quote, urlparse
from pymongo import MongoClient
from bs4 import BeautifulSoup

class BiqugeSpider(scrapy.Spider):
    name = 'biquge'

    def start_requests(self):
        """生成起点中月点击最多的500本小说在笔趣阁的搜索地址"""
        search_url = 'http://www.biquge.com.tw/modules/article/soshu.php?searchkey=+{}'
        client = MongoClient()
        find = client.Novel.qidian.find_one({'_id': '500'})
        names = find['qidian']
        if len(names) != 500:
            raise ValueError('数据错误，请重新运行名字为qidian的爬虫!')
        for name in names[:1]:
            name = quote("纣临", encoding='gbk')
            yield scrapy.Request(search_url.format(name), callback=self.parse,
                                 encoding='gbk', meta={'v_name': name})

    def parse(self, response):
        """解析查找页面"""
        url = urlparse(response.url)
        soup = BeautifulSoup(response.body, 'lxml')
        # 如果有query属性 说明查找到了多个结果
        if url.query:
            print('hh')
            tr = soup.find(id='nr')
            if tr:
                url = tr.find('td').a.get('href')
                yield scrapy.Request(url, callback=self.parse_novel,
                                         encoding='gbk')
        else:
            print('else')
            yield scrapy.Request(response.url, callback=self.parse_novel
                                 , encoding='gbk', dont_filter=True)

    def parse_novel(self, response):
        """解析小说目录页面"""
        item = NovelItem()
        url = urlparse(response.url)
        soup = BeautifulSoup(response.text, 'lxml')
        if re.match(r'/\d+_\d+/', url.path):
            info = soup.find(id='info')
            if info:
                info_p = info.find_all('p')
                name = info.h1.text
                item['novel_name'] = name
                item['novel_author'] = info_p[0].text[7:]
                item['novel_abstract'] = soup.find(id='intro').text
                time = datetime.strptime(info_p[2].text[5:], '%Y-%m-%d')
                item['last_update'] = time
                item['last_chapter'] = info_p[-1].a.text
                dds = soup.find_all('dd')
                item['chapter_count'] = len(dds)
                item['chapter_id'] = hashlib.md5(
                    name.encode('utf-8')).hexdigest()
                item['status'] = '1'
                item['chapters'] = {}
                # 调试 只截取一章
                for dd in dds[:1]:
                    url = dd.a.get('href')
                    id = re.search(r'/(\d+)\.', url).groups()[0]
                    item['chapters'][dd.a.text] = id
                    url = 'http://www.biquge.com.tw' + url
                    yield scrapy.Request(url, callback=self.parse_chapter,
                                         meta={'item': item})

    def parse_chapter(self, response):
        """解析小说章节页面"""
        c_item = ChapterItem()
        item = response.meta.get('item')
        soup = BeautifulSoup(response.text, 'lxml')
        if item:
            c_item['chapter_id'] = item['chapter_id']
            c_item['chapter_cent'] = soup.find(id='content').text
        return {'item': item, 'c_item': c_item}