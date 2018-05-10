# -*- coding: utf-8 -*-
import scrapy


class DoubanReadSpider(scrapy.Spider):
    name = 'douban_read'
    allowed_domains = ['read.douban.com']
    base_url = 'https://read.douban.com/kind/1'
    num = 46260

    start_urls = [
        base_url + '?start={num}&sort=hot&promotion_only=False&'
        'min_price=None&max_price=None&works_type=None'
    ]

    def parse(self, response):
        item = {'urls': []}
        for i in range(1, 21):
            xpath = '/html/body/div/div/article/div[2]/div[1]/ul/li[{i}]/' \
                    'div[2]/div[2]/a/@href'
            url = response.xpath(xpath.format(i=i), num=self.num)
            if url:
                url = url.extract()[0]
                if url:
                    item['urls'].append("https://read.douban.com" + url)
        yield item
        next_url = response.xpath("//a[contains(text(), '后页')]/@href")
        if next_url:
            next_url = next_url.extract()[0]
            yield scrapy.Request(url=self.base_url + next_url,
                                 callback=self.parse)
