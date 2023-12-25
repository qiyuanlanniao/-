# -*- coding:utf-8 -*-
# @Time        : 2023/12/14
# @Author      : 12123040206何旻
# @Description : 这段代码是一个Scrapy中间件的实现，
# 包括Spider Middleware（ArticlespiderSpiderMiddleware）和Downloader Middleware（ArticlespiderDownloaderMiddleware）。
# Spider Middleware用于在爬虫运行期间拦截和处理Spider的输入、输出和异常，其中包括在爬虫启动时记录日志。
# Downloader Middleware则用于在发出请求和处理响应的过程中进行预处理，同样包括在爬虫启动时记录日志。
# 这些中间件通过Scrapy的信号系统与爬虫（Spider）进行连接，以在不同阶段介入爬虫的执行过程，实现定制化的请求和响应处理逻辑。
from scrapy import signals


class ArticlespiderSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        return None

    def process_spider_output(self, response, result, spider):
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        pass

    def process_start_requests(self, start_requests, spider):
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ArticlespiderDownloaderMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
