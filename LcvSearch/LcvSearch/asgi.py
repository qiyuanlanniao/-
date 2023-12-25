# -*- coding:utf-8 -*-
# @Time        : 2023/12/17
# @Author      : 12123040206何旻
# @Description :
# 这段代码是一个基于Django框架的ASGI应用程序的配置脚本，通过设置环境变量和获取ASGI应用程序，
# 将指定的Django项目设置模块应用于ASGI服务器，以便启动和运行该Django应用程序。
"""
ASGI config for LcvSearch project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LcvSearch.settings')

application = get_asgi_application()
