# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 账户状态
    account_status = scrapy.Field()
    # 回答数
    answer_count = scrapy.Field()
    # 文章数
    articles_count = scrapy.Field()
    # 头像地址
    avatar_url = scrapy.Field()
    # 头像模版
    avatar_url_template = scrapy.Field()
    # 徽章
    badge = scrapy.Field()
    # 盈利问题数
    commercial_question_count = scrapy.Field()
    # 封面地址
    cover_url = scrapy.Field()
    # 简介
    description = scrapy.Field()
    # 教育情况
    educations = scrapy.Field()
    # 工作情况
    employments = scrapy.Field()
    # 商业情况
    business = scrapy.Field()
    # 收藏数
    favorite_count = scrapy.Field()
    # 被收藏数
    favorited_count = scrapy.Field()
    # 被关注数
    follower_count = scrapy.Field()
    # 关注数
    following_count = scrapy.Field()
    # 性别
    gender = scrapy.Field()
    # 主页标签
    headline = scrapy.Field()
    # 激活
    is_active = scrapy.Field()
    # 居住地
    locations = scrapy.Field()
    # 通讯号？
    message_thread_token = scrapy.Field()
    # 用户名
    name = scrapy.Field()
    # 提问数
    question_count = scrapy.Field()
    # 唯一标识
    url_token = scrapy.Field()
    # 被感谢数
    thanked_count = scrapy.Field()
    # 获得的赞数
    voteup_count = scrapy.Field()
