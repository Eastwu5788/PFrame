# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-13 15:00'
import collections


def p_merge(from_dict, to_dict):
    """ 合并两个字典，支持深度合并

    Usage:
        >>> p_merge({"1": "2", "3": "4"}, {"3": "5"})
        {"1": "2", "3": "4"}

        >>> p_merge({"1": {"2": 3, "4": 5}}, {"1": {"5": 5}})
        {"1": {"2": 3, "4": 5, "5": 5}}

    :param from_dict: 原始字典
    :param to_dict: 目标字典
    """
    for key, value in from_dict.items():
        # 如果value和目标dict中的值都为dict时，进行深度合并
        if key in to_dict.keys()\
                and isinstance(to_dict[key], collections.Mapping) \
                and isinstance(value, collections.Mapping):
            p_merge(value, to_dict[key])
        else:
            to_dict[key] = value

    return to_dict
