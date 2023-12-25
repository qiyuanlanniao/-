# -*- coding:utf-8 -*-
# @Time        : 2023/12/15
# @Author      : 12123040206何旻
# @Description : 将url转换为md5码

import hashlib
import re


def get_md5(url):
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


if __name__ == "__main__":
    print(get_md5("https://news.cnblogs.com/".encode("utf-8")))
