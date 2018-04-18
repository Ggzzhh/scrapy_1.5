# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
from ..items import FullwebsiteItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class HapdsSpider(CrawlSpider):
    name = 'hapds'
    allowed_domains = ['hapds.lss.gov.cn']
    start_urls = ['http://hapds.lss.gov.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'hapds\.lss\.gov\.cn'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.logger.info('目前的url是：{}'.format(response.url))
        item = FullwebsiteItem()
        soup = BeautifulSoup(response.body, 'lxml')
        if not soup.find('div', {'class': 'cent'}):
            return None
        item['title'] = soup.find('div', {'class': 'c-tittle'}).text
        time_text = soup.find('div', {'class': 'time'}).text
        res = re.search(r'[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}', time_text)
        if res:
            item['time'] = res.group()
        item['url'] = response.url
        item['content'] = soup.find('div', {'class': 'nr'}).text
        return item
