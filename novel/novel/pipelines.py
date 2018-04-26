# -*- coding: utf-8 -*-
from pymongo import MongoClient
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NovelPipeline(object):
    def open_spider(self, spider):
        self.client = MongoClient()
        self.db = self.client.Novel

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if item.get('qidian'):
            for name in item['qidian']:
                self.db.qidian.update({"_id": '500'}, {"$addToSet": {
                    'qidian': name}}, upsert=True)
        return item
