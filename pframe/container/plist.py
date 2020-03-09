# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 13:13'
# project
from pframe.util.exception import PFExtractionError
from .pobject import p_get


def p_index(array, index=None):
    """ 将字典数组或者多维数组中的数据按index进行提取

    Usage:
        >>> p_index([[0, 1], [2, 3], [4, 5]], index=0)
        [0, 2, 4]
        >>> p_index([{"key1": "value1"}, {"key1": "value2"}], index="key1")
        ["value1", "value2"]

    :param array: 原始数组
    :param index: 提取的索引
    :rtype: list
    """
    if not isinstance(array, (list, tuple)):
        raise TypeError("input params `array` must be type of list or tuple")

    fmt_rst = list()
    for idx, item in enumerate(array):
        # try to extract data from the array or tuple
        if isinstance(item, (list, tuple)) and isinstance(index, int):
            if len(item) <= index:
                raise IndexError("item index out of index at `%d`" % idx)
            fmt_rst.append(item[index])

        # try to extract data from the dictionary
        elif isinstance(item, dict):
            if index not in item:
                raise KeyError("`%s` not in item at index `%d`" % (index, idx))
            fmt_rst.append(item[index])

        # try to extract data from the object
        elif hasattr(item, index):
            fmt_rst.append(getattr(item, index))

        else:
            raise PFExtractionError("can't extract from array at index `%d`" % idx)

    return fmt_rst


def p_index_column(array, index=None, append=False):
    """ 将数组中的数据提取成以value值作为key的字典

    Usage:
        >>> p_index_column([{"id": "5"}, {"id": "6"}], index="id", append=False)
        {"5": {"id": "5"}, "6": {"id": "6"}}
        >>> p_index_column([{"id": "5"}, {"id": "6"}], index="id", append=False)
        {"5": [{"id": "5"}], "6": [{"id": "6"}]}

    :param array: 原始数据
    :param index: 提取的key值
    :param append: 如果遇到key重复，是否将数据进行追加
    :rtype: dict
    """
    if not isinstance(array, (list, tuple)):
        raise TypeError("input params `array` must be type of list or tuple")

    fmt_rst = dict()
    for _, item in enumerate(array):
        value = p_get(item, key=index, default=None)

        # None value can not be key as dict
        if value is None:
            continue

        # append result
        if append:
            exit_value = fmt_rst.get(value, list())
            exit_value.append(item)
            fmt_rst[value] = exit_value

        # return simple dict
        else:
            fmt_rst[value] = item

    return fmt_rst
