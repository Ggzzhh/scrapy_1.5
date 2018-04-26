# -*- coding: utf-8 -*-
import scrapy


class QidianSpider(scrapy.Spider):
    name = 'qidian'

    def start_requests(self):
        base_url = 'https://www.qidian.com/rank/click?style=1&dateType=2&page={}'
        for i in range(1, 26):
            request = scrapy.Request(base_url.format(i), callback=self.parse)
            request.meta['PhantomJS'] = True
            yield request

    def parse(self, response):
        L = response.xpath('//div[@class="book-mid-info"]//h4//a/text('
                           ')').extract()
        return {'qidian': L}
