# -*- coding:utf-8 -*-
# @Time        : 2023/12/13
# @Author      : 12123040206何旻
# @Description : 这段代码使用 Scrapy 框架执行一个名为 "jobbole" 的爬虫。首先，通过导入必要的模块，
# 将项目路径添加到系统路径中。然后，使用 execute 函数调用 Scrapy 命令行工具，传递参数 ["scrapy", "crawl", "jobbole"]，
# 其中 "jobbole" 是要运行的爬虫的名称.

from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
execute(["scrapy", "crawl", "jobbole"])
