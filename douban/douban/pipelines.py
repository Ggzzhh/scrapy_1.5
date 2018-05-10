# -*- coding: utf-8 -*-
import redis
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def open_spider(self, spider):
        self.r = redis.StrictRedis()

    def process_item(self, item, spider):
        if item.get('urls'):
            for url in item['urls']:
                self.r.sadd('read.douban.urls', url)
        return item
