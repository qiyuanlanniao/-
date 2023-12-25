# -*- coding:utf-8 -*-
# @Time        : 2023/12/17
# @Author      : 12123040206何旻
# @Description : 这段代码是使用Elasticsearch的Python客户端库elasticsearch-dsl定义了一个名为ArticleType的文档类型（DocType），
# 用于表示具有特定字段（如标题、创建日期、URL等）的文章数据。通过自定义分析器（Analyzer）ik_max_word，实现了对文章标题、标签和内容的中文分词，
# 并配置了Completion类型的suggest字段用于实现搜索建议功能。最后，通过调用ArticleType.init()方法，将该文档类型映射初始化到Elasticsearch索引中，
# 索引名为"jobbole"，文档类型名为"article"。
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer, InnerObjectWrapper, Completion, Keyword, Text, Integer

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["localhost"])


class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])


class ArticleType(DocType):
    suggest = Completion(analyzer=ik_analyzer)
    title = Text(analyzer="ik_max_word")
    create_date = Date()
    url = Keyword()
    url_object_id = Keyword()
    front_image_url = Keyword()
    front_image_path = Keyword()
    praise_nums = Integer()
    comment_nums = Integer()
    fav_nums = Integer()
    tags = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")

    class Meta:
        index = "jobbole"
        doc_type = "article"


if __name__ == "__main__":
    ArticleType.init()

