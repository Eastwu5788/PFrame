# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 14:14'
# sys
import datetime


def current_datetime():
    """ 获取当前datetime
    """
    return datetime.datetime.now()


def current_time(fmt="%Y-%m-%d %H:%M:%S"):
    """ 获取当前时间字符串
    """
    return current_datetime().strftime(fmt)


def datetime_2_str(p_datetime, fmt="%Y-%m-%d %H:%M:%S"):
    """ 将日期转换成字符串

    :param p_datetime: 原始datetime日期
    :param fmt: 时间格式
    :rtype: str
    """
    if not isinstance(p_datetime, datetime.datetime):
        raise TypeError("params `p_datetime` must be type of datetime")

    return p_datetime.strftime(fmt)


def str_2_datetime(p_str, fmt="%Y-%m-%d %H:%M:%S"):
    """ 将字符串转换成日期

    :param p_str: 原始时间字符串
    :param fmt: 时间格式
    :rtype: datetime.datetime
    """
    # don't need to transform
    if isinstance(p_str, datetime.datetime):
        return p_str

    if not isinstance(p_str, str):
        raise TypeError("params `p_str` must be type of str")

    return datetime.datetime.strptime(p_str, fmt)
