# -*- coding:utf-8 -*-
# @Time        : 2023/12/13
# @Author      : 12123040206何旻
# @Description : 这段代码是一个用于配置Scrapy项目的Python脚本，使用了setuptools库来进行项目的打包和安装。


from setuptools import setup, find_packages

setup(
    name='project',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = ArticleSpider.settings']},
)
