# -*- coding:utf-8 -*-
# @Time        : 2023/12/17
# @Author      : 12123040206何旻
# @Description : 这段代码是一个 Django 项目的 WSGI 部分，通过导入必要的模块和设置项目的环境变量，
# 创建了一个 WSGI 应用对象，用于处理 Web 服务器与 Django 项目之间的通信，实现将 HTTP 请求转发给 Django 应用进行处理的功能。
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LcvSearch.settings')

application = get_wsgi_application()
