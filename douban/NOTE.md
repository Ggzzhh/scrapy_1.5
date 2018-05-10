笔记
---
* 说明：这个爬虫用来抓取豆瓣读书中的中文电子书，使用一个先抓取所有图书详情页的url，
之后使用第二个爬虫抓取详细信息，并采用redis充当存储器这样可以实现断点续传功能，
而后可以使用scrapy-redis或者自写功能实现分布式爬虫来爬取图书详情页，需要抓取的信息有：
    * 图书名称
    * 作者
    * 译者
    * 类别
    * 评价
    * 评价人数
    * 豆瓣评价
    * 豆瓣评价人数
    * 简介/导言
    * 标签
* 存储方式：redis用于充当队列，存储url，抓取后的信息存储在mongodb中
* 数量：初步估计约为6万+
* 难度：easy
* 步骤：
    1. douban_read这个爬虫用于抓取所有的图书详情页的url，只需解析[https://read.douban.com/kind/1?start=0&sort=hot&promotion_only=False&min_price=None&max_price=None&works_type=None](https://read.douban.com/kind/1?start=0&sort=hot&promotion_only=False&min_price=None&max_price=None&works_type=None)
    这个网址的内容, 并在xpath的帮助下抓取该书的地址即可。
    2. 找到下一页的地址，重复第一步。
    3. ...
    
    