# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    novel_name = scrapy.Field()
    novel_author = scrapy.Field()
    novel_abstract = scrapy.Field()
    last_update = scrapy.Field()
    last_chapter = scrapy.Field()
    chapter_count = scrapy.Field()
    novel_id = scrapy.Field()
    status = scrapy.Field()
    chapters = scrapy.Field()

    pass


class ChapterItem(scrapy.Item):
    chapter_id = scrapy.Field()
    chapter_name = scrapy.Field()
    chapter_cent = scrapy.Field()