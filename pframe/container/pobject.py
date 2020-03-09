# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 13:47'


def p_get(item, key, default=None):
    """ 根据key读取item中的数据，支持字典、数组、对象等

    :param item: 原始数据
    :param key: 用于提取的key
    :param default: 提取失败的默认值
    """
    # extract data from dict
    if isinstance(item, dict):
        return item.get(key, default)

    # extract data from array
    if isinstance(item, (list, tuple)) and isinstance(key, int):
        # index out of range
        if len(item) <= key:
            raise IndexError("index out of range")
        return item[key]

    # extract data from object
    if hasattr(item, key):
        return getattr(item, key)

    return default
