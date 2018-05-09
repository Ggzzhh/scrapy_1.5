# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import ZhihuItem
from scrapy_redis.spiders import RedisSpider


class ZhihuSpider(RedisSpider):
    name = 'zhihu'

    def parse(self, response):
        item = ZhihuItem()
        res = json.loads(response.text)
        for field in item.fields:
            if res.get(field):
                item[field] = res.get(field)
        return item
