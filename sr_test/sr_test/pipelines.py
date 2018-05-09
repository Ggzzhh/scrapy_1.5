# -*- coding: utf-8 -*-
from pymongo import MongoClient
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SrTestPipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient()
        self.db = self.client.zhihu

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if item.get('url_token'):
            self.db.users.update({'url_token': item['url_token']},
                                 {'$set': dict(item)}, True)
            return '人物{}的资料 + 1'.format(item.get('url_token'))
