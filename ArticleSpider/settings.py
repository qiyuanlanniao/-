# -*- coding:utf-8 -*-
# @Time        : 2023/12/14
# @Author      : 12123040206何旻
# @Description : 这段代码是一个用于爬取文章信息的Scrapy项目配置文件。
# 配置中包括了爬虫的基本设置，如爬虫名称、模块信息、爬取规则的遵循与否等。
# 同时，它设置了并发请求的数量、请求延迟时间、是否启用Cookie等网络请求参数。
# 该项目还定义了数据处理的管道，包括保存图片、生成JSON文件、将数据存储到MySQL数据库和Elasticsearch中等功能。
# 此外，还指定了图片的存储路径和MySQL数据库的连接信息。最后，提供了登录网站所需的用户账号和密码。
import os
import random


BOT_NAME = 'ArticleSpider'

SPIDER_MODULES = ['ArticleSpider.spiders']
NEWSPIDER_MODULE = 'ArticleSpider.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 2

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = random.randint(1, 5)
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

ITEM_PIPELINES = {
    # 'ArticleSpider.pipelines.ArticleImagePipeline': 1,
    # 'ArticleSpider.pipelines.JsonWithEncodingPipeline': 2,
    # 'ArticleSpider.pipelines.JsonExporterPipeline': 3,
    # 'ArticleSpider.pipelines.MysqlTwistedPipeline': 4,
    'ArticleSpider.pipelines.ElasticsearchPipeline': 5,
    # 'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
}

IMAGES_URLS_FIELD = "front_image_url"
project_dir = os.path.dirname(os.path.abspath(__file__))
IMAGES_STORE = os.path.join(project_dir, 'images')

MYSQL_HOST = "192.168.174.129"
MYSQL_DBNAME = "article_spider"
MYSQL_USER = "root"
MYSQL_PASSWORD = "root"

SQL_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
SQL_DATE_FORMAT = "%Y-%m-%d"

USER = "19507370354"
PASSWORD = "kcsj123456789"
