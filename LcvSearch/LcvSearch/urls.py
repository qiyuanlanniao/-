# -*- coding:utf-8 -*-
# @Time        : 2023/12/17
# @Author      : 12123040206何旻
# @Description : 这段Django代码定义了网站的URL模式，其中包括管理员页面路径、首页路径、搜索建议路径和搜索结果路径，
# 并分别对应相应的视图类，其中IndexView用于展示网站首页，SearchSuggest用于处理搜索建议，而SearchView用于展示搜索结果。
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from search.views import SearchSuggest, SearchView,IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('suggest/', SearchSuggest.as_view(), name="suggest"),
    path('search/', SearchView.as_view(), name="search")
]
