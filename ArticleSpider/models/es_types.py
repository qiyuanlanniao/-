# -*- coding:utf-8 -*-
# @Time        : 2023/12/16
# @Author      : 12123040206何旻
# @Description : 这段代码是使用Elasticsearch的Python客户端库elasticsearch_dsl来定义一个文档类型（DocType）称为ArticleType，用于建立与Elasticsearch的索引"jobbole"相关联的文档。
# 该文档包括了一些字段，如标题（title）、创建日期（create_date）、URL（url）、点赞数（praise_nums）、评论数（comment_nums）、收藏数（fav_nums）等。
# 同时，针对中文文本的分词处理采用了IK分词器（ik_max_word），并且为搜索建议（suggest）字段使用了自定义分析器（CustomAnalyzer）。
# 最后，在程序的主函数中，通过执行ArticleType.init()来初始化该文档类型，确保与Elasticsearch建立正确的映射关系。
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
