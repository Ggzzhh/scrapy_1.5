# -*- coding: utf-8 -*-
from pymongo import MongoClient
from fullWebsite.spiders import proxy_ip
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FullwebsitePipeline(object):

    def open_spider(self, spider):
        self.client = MongoClient()
        # t = proxy_ip.Proxies()
        # t.run()

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        print('运行')
        db = self.client.hapds
        item = dict(item)
        url = item.pop('url', 'None')
        db.contents.update({'_id': url}, {'$set': item}, upsert=True)
        print('heh')
        return item
