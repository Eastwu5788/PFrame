# !/usr/local/python/bin/python
# -*- coding: utf-8 -*-
# (C) Wu Dong, 2019
# All rights reserved
# @Author: 'Wu Dong <wudong@eastwu.cn>'
# @Time: '2020-03-09 14:11'
# sys
import time


def current_timestamp():
    """ 获取当前秒级时间戳
    """
    return int(time.time())


def current_timestamp_ms():
    """ 获取当前毫秒级时间戳
    """
    return int(round(time.time() * 1000))


def timestamp_2_datetime(timestamp, fmt):
    """ 将时间戳转换成指定格式的日期字符串

    :param timestamp: 原始时间戳
    :param fmt: 时间格式
    """
    return time.strftime(fmt, time.localtime(timestamp))


def datetime_2_timestamp(p_datetime):
    """ 将datetime转换成时间戳

    :param p_datetime: 原始日期
    """
    return time.mktime(p_datetime.timetuple())
