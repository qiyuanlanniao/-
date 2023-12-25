# -*- coding:utf-8 -*-
# @Time        : 2023/12/17
# @Author      : 12123040206何旻
# @Description : 这段代码使用Elasticsearch的搜索功能，
# 通过ArticleType模型中的'suggest'字段，针对包含"苹果"关键词的建议进行模糊匹配搜索，并返回匹配度前10的建议结果，最后提取出这些结果中的标题信息。
from search.models import ArticleType

s = ArticleType.search()
s = s.suggest('my-suggest', "苹果", completion={
    "field": "suggest", "fuzzy": {
        "fuzziness": 2
    },
    "size": 10
})

suggestions = s.execute()

for match in getattr(suggestions.suggest, "my-suggest")[0].options:
    source = match._source.title
