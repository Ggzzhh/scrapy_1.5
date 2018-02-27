Scrapy文档部分摘选
================
### [命令行工具](#命令行工具)
* [全局命令](#全局命令)
* [项目命令](#项目命令)
* [自定义命令](#自定义命令)

--------

命令行工具
----------------
#### 全局命令
* __startproject__
    * 句法: `scrapy startproject <project_name> [project_dir]`
    * 需要项目: None
    * 在`project_dir`下创建一个名为`project_name`的项目.如果没有指定`project_dir`。
    默认情况下`project_dir`跟`project_name`将会相同
    * 用法： `scrapy startproject myproject`
* __genspider__
    * 句法: `scrapy genspider [-t template] <name> <domain>`
    * 需要项目: No
    * 在当前文件夹或者是当前的项目文件夹下创建一个新爬虫，`name`就是爬虫的名字，`domain`
    则是用于生成蜘蛛的`allowed_domains`和`start_urls`属性。
    * 用法：
        ```python3
        $ scrapy genspider -l
        Available templates:
          basic
          crawl
          csvfeed
          xmlfeed

        $ scrapy genspider example example.com
        Created spider 'example' using template 'basic'

        $ scrapy genspider -t crawl scrapyorg scrapy.org
        Created spider 'scrapyorg' using template 'crawl'
        ```
        这只是一个便捷的快捷命令，用于根据预定义的模板创建蜘蛛，但当然不是创建蜘蛛的唯一方法。您可以自己创建蜘蛛源代码文件，而不是使用此命令。
* __settings__
    * 句法: `scrapy settings [options]`
    * 需要项目: No
    * 获取`scrapy`设置的值
    如果在项目中设置了将显示设置的值，否则会显示默认值
    * 用法：
        ```
        $ scrapy settings --get BOT_NAME
        scrapybot
        $ scrapy settings --get DOWNLOAD_DELAY
        0
        ```
* __runspider__
    * 句法: `scrapy runspider <spider_file.py>`
    * 需要项目: No
    * 运行一个自包含在Python文件中的蜘蛛，而不必创建一个项目。
* __shell__
    * 句法: `scrapy shell [url]`
    * 需要项目: No
    * 为指定的URL（如果给定）启动Scrapy shell，如果没有给出URL，则为空。
    同时支持UNIX风格的本地文件路径，无论是相对 ./或../前缀或绝对文件路径。
    有关更多信息，请参阅[Scrapy shell](#shell)
    * 支持的选项
        1. `--spider=SPIDER`： 绕过蜘蛛自动检测并强制使用特定的蜘蛛
        2. `-c code`： 评估shell中的代码，打印结果并退出
        3. `--no-redirect`： 不跟随HTTP 3xx重定向（默认是跟随它们）;
        这个选项只会影响您在命令行上作为参数传递的URL;
        一旦你在shell中使用`fetch(url)`，默认情况下仍然会跟随HTTP重定向。
    * 用法：
        ```
        $ scrapy shell http://www.example.com/some/page.html
        [ ... scrapy shell starts ... ]

        $ scrapy shell --nolog http://www.example.com/ -c '(response.status, response.url)'
        (200, 'http://www.example.com/')

        # 默认情况下，shell跟随HTTP重定向
        $ scrapy shell --nolog http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F -c '(response.status, response.url)'
        (200, 'http://example.com/')

        # 你可以用 --no-redirect 禁用它
        # 仅用于通过命令行参数传递的URL）
        $ scrapy shell --no-redirect --nolog http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F -c '(response.status, response.url)'
        (302, 'http://httpbin.org/redirect-to?url=http%3A%2F%2Fexample.com%2F')
        ```
* __fecth__
    * 句法: `scrapy fetch <url>`
    * 需要项目: No
    * 使用Scrapy下载器下载给定的URL并将内容写入标准输出。

        关于这个命令的有趣之处在于它提取了蜘蛛将如何下载它的页面。
        例如，如果蜘蛛有一个`USER_AGENT` 属性覆盖了User Agent，它将使用该属性。

        所以这个命令可以用来“看”你的蜘蛛如何获取某个页面。

        如果在项目之外使用，则不会应用特定的每个蜘蛛行为，它将仅使用默认的Scrapy下载器设置。
    * 支持的选项
        1. `--spider=SPIDER`： 绕过蜘蛛自动检测并强制使用特定的蜘蛛
        2. `--headers`： 打印响应的HTTP头信息而不是响应的正文
        3. `--no-redirect`： 不跟随HTTP 3xx重定向（默认是跟随它们）;
    * 用法：
        ```
        $ scrapy fetch --nolog http://www.example.com/some/page.html
        [ ... html content here ... ]

        $ scrapy fetch --nolog --headers http://www.example.com/
        {'Accept-Ranges': ['bytes'],
         'Age': ['1263   '],
         'Connection': ['close     '],
         'Content-Length': ['596'],
         'Content-Type': ['text/html; charset=UTF-8'],
         'Date': ['Wed, 18 Aug 2010 23:59:46 GMT'],
         'Etag': ['"573c1-254-48c9c87349680"'],
         'Last-Modified': ['Fri, 30 Jul 2010 15:30:18 GMT'],
         'Server': ['Apache/2.2.3 (CentOS)']}
        ```
* __view__
    * 句法: `scrapy view <url>`
    * 需要项目: No
    * 在浏览器中打开给定的URL，因为Scrapy蜘蛛会“看到”它。
    有时候，蜘蛛看到的网页与普通用户不同，所以这可以用来检查蜘蛛“看到”什么，并确认它是你期望的。
    * 支持的选项
        1. `--spider=SPIDER`： 绕过蜘蛛自动检测并强制使用特定的蜘蛛
        2. `--no-redirect`： 不跟随HTTP 3xx重定向（默认是跟随它们）;
    * 用法：
        ```
        $ scrapy view http://www.example.com/some/page.html
        [ ... browser starts ... ]
        ```
* __version__
    * 句法: `scrapy version [-v]`
    * 需要项目: No
    * 显示当前版本,如果与-v它一起使用，还会打印`Python`，Twisted`和`Platform`信息，这对于错误报告很有用。
    * 用法：
        ```
        $ scrapy runspider myspider.py
        [ ... spider starts crawling ... ]
        ```
#### 项目命令
* __crawl__
    * 句法: `scrapy crawl <spider>`
    * 需要项目: yes
    * 开始使用蜘蛛爬行，`spider`是蜘蛛的名字
    * 用法：
        ```
        $ scrapy crawl myspider
        [ ... myspider starts crawling ... ]
        ```
* __check__
    * 句法: `scrapy check [-l] <spider>`
    * 需要项目: yes
    * 开始检查scrapy的项目？合同
    * 用法：
        ```
        $ scrapy check -l
        first_spider
          * parse
          * parse_item
        second_spider
          * parse
          * parse_item

        $ scrapy check
        [FAILED] first_spider:parse_item
        >>> 'RetailPricex' field is missing

        [FAILED] first_spider:parse
        >>> Returned 92 requests, expected 0..4
        ```
* __list__
    * 句法: `scrapy list`
    * 需要项目: yes
    * 列出当前项目中所有可用的蜘蛛。输出每行一个蜘蛛。
    * 用法：
        ```
        $ scrapy list
        spider1
        spider2
        ```
* __edit__
    * 句法: `scrapy edit <spider>`
    * 需要项目: yes
    * 使用`EDITOR`环境变量中定义的编辑器编辑给定的蜘蛛，或者（如果未设置）编辑该`EDITOR`设置。

        此命令仅作为最常见情况的便捷快捷方式提供，开发人员当然可以自由选择任何工具或IDE来编写和调试蜘蛛。
    * 用法：
        ```
        $ scrapy edit spider1
        ```
* __parse__
    * 句法: `scrapy parse <url> [options]`
    * 需要项目: Yes
    * 获取给定的URL并用处理它的蜘蛛解析它，使用`--callback`传递的方法，如果没有给出则使用`parse`。
    * 支持的选项
        1. `--spider=SPIDER`： 绕过蜘蛛自动检测并强制使用特定的蜘蛛
        2. `--a NAME=VALUE`： 设置蜘蛛参数（可能会重复）
        3. `--callback`或`-c`： 使用spider方法作为解析响应的回调
        4. `--meta`或`-m`： 将传递给回调函数的附加的meta。必须是有效的json字符串。例如：-meta ='{“foo”：“bar”}'
        5. `--pipelines`： 通过管道处理项目
        6. `--rules`或者`-r`：使用[CrawlSpider](#CrawlSpider) 规则来发现用于解析响应的回调（即蜘蛛方法）
        7. `--noitems`：不显示scrapy的items
        8. `--nolinks`：不显示scrapy提取的连接
        9. `--nocolour`：避免使用pygments来给输出上色？
        10. `--depth`或`-d`：跟踪的递归深度级别（默认值：1）
        11. `--verbose`或者`-v`：显示每个深度级别的信息
    * 用法：
        ```
        $ scrapy parse http://www.example.com/ -c parse_item
        [ ... scrapy 蜘蛛爬行 example.com 的日志 ... ]

        >>> STATUS DEPTH LEVEL 1 <<<
        # Scraped Items  ------------------------------------------------------------
        [{'name': u'Example item',
         'category': u'Furniture',
         'length': u'12 cm'}]

        # Requests  -----------------------------------------------------------------
        []
        ```
* __bench__
    * 句法: `scrapy bench`
    * 需要项目: No
    * 运行一个快速基准测试--[Benchmarking](#Benchmarking)
#### 自定义命令
您也可以使用该`COMMANDS_MODULE`设置添加自定义项目命令。
有关如何实现命令的示例，请参阅[scrapy/commands](https://github.com/scrapy/scrapy/tree/master/scrapy/commands)
##### COMMANDS_MODULE
默认:(`''`空字符串）

用于查找自定义Scrapy命令的模块。为您的Scrapy项目添加自定义命令。

例：
```python3
COMMANDS_MODULE  =  'mybot.commands'
```
---
<span id='two'>二、spiders</span>
----------------
暂无