# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 17:33'
# sys
import hashlib


def md5(ori_str):
    """ MD5加密算法

    :param ori_str: 原始字符串
    :return: 加密后的字符串
    """
    md5_obj = hashlib.md5()
    md5_obj.update(ori_str.encode("utf8"))
    return md5_obj.hexdigest()

