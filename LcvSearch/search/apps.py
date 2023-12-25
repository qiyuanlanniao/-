# -*- coding:utf-8 -*-
# @Time        : 2023/12/17
# @Author      : 12123040206何旻
# @Description : 这段代码是一个Django应用配置（AppConfig），其中定义了一个名为SearchConfig的配置类。
# 该配置类指定了默认的自动字段类型（default_auto_field）为django.db.models.BigAutoField，并将应用命名为'search'。
from django.apps import AppConfig


class SearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'search'
